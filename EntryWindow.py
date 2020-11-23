# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : EntryWindow.py
# @Software: PyCharm

from PyQt5 import QtCore, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CameraWidget import CameraWidget
from PyQt5.QtWidgets import *
from base.baseMainWindow import Ui_mainWindow
from face_api import *
import time
from tools import *
from db import *
from AddFaceWidget import AddFaceWidget
from AddOrganizationWidget import AddOrganizationWidget
from ChooseOrgWidget import ChooseOrgWidget
from OrgEditWidget import OrgEditWidget


class EntryWindow(Ui_mainWindow):

    def __init__(self, MainWindow):
        super().__init__()
        self.mainWindow = MainWindow
        self.image_templates_dir = "./img_templates/"
        self.setupUi(MainWindow)
        # 初始化界面各个控件
        self.initUI()
        # 初始化人脸识别模块
        self.initFaceDetect()
        # 初始化定时器，用来更新UI
        self.timer = QtCore.QTimer(MainWindow)
        self.timer.timeout.connect(self.updateUI)
        self.timer.setInterval(15)
        self.timer.start()
        # 初始化本项目使用的数据库连接
        self.databaseConnection = None
        self.database_filename = ""
        # 初始化本次选择的组织
        self.organization = ""
        self.cur_org_id = None
        # 是否开始识别人脸的标记位
        self.start_detect = False

    def updateUI(self):
        """
        定时器回调函数，用于更新UI
        """
        # 更新每次人脸检测耗时的标签
        timeCostStr = "耗时为:" + str(int(self.timeCost)) + "ms"
        self.curTimeCost.setText(timeCostStr)
        # 更新当前识别出的人的人脸图片和人名和编号
        imgViewSize = (self.curUserImg.size().width(),
                       self.curUserImg.size().height())
        if len(self.face_names) > 0 and self.face_names[0] != "Unknown":
            name = self.face_names[0]
            numbers = self.face_numbers[0]
            image_file_path = self.image_templates_dir + name + "_" + numbers + ".jpg"
            image = load_image_file(image_file_path, imgViewSize)
            pixmap = QImage(
                image, imgViewSize[0], imgViewSize[1], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            self.curUserImg.setPixmap(pixmap)
        # 更新名称和学号标签
        if len(self.face_names) != 0 and len(self.face_numbers) != 0:
            self.curUserName.setText("姓名：" + self.face_names[0])
            self.curUserNumber.setText("编号：" + self.face_numbers[0])
        else:
            self.curUserName.setText("姓名：无")
            self.curUserNumber.setText("编号：无")
        if self.start_detect:
            # 将识别出的人加入已签到的列表，并更新UI的listview
            for i in range(len(self.face_names)):
                name = self.face_names[i]
                number = self.face_numbers[i]
                if name == "Unknown":
                    continue
                # 如果当前识别出的人脸不在已签到列表里面
                name_list = [i.split("\t")[0] for i in self.user_list]
                if name not in name_list:
                    query_res = query_student_by_number(self.databaseConnection, number)
                    stu_id = query_res[0][0]
                    if check_number_in_org(self.databaseConnection, stu_id, self.cur_org_id):
                        # 在listview里面添加已签到的学生，并且在数据库中记录
                        self.addUser(name, number)
                        # 将当前学生的签到记录插入数据库
                        student_id = query_student_by_number(self.databaseConnection, number)[0][0]
                        org_id = self.cur_org_id
                        insert_t_record(self.databaseConnection, student_id, org_id)

        # 更新状态栏显示的内容
        if self.databaseConnection is None:
            self.statusbar.showMessage("数据库未连接")
        else:
            self.statusbar.showMessage("数据库已连接：" + self.database_filename)

    def initFaceDetect(self):
        """
        初始化人脸识别模块
        """
        # 加载人脸的模板图片
        self.known_face_encodings, self.known_face_tags = load_image_templates(
            self.image_templates_dir)
        self.known_face_names = [tag.split("_")[0]
                                 for tag in self.known_face_tags]
        self.known_face_numbers = [
            tag.split("_")[1] for tag in self.known_face_tags]
        self.face_locations = []
        self.face_names = []
        self.timeCost = 0.0
        # 标记位，用来降低人脸检测开销
        self.process_this_frame = True

    def initUI(self):
        """
        初始化界面的各个控件
        """
        # 绑定按钮事件
        self.openCameraBtn.clicked.connect(self.openCamera)
        self.recordBtn.clicked.connect(self.manuallyRecord)
        # 绑定菜单事件
        self.openDatabaseMenu.triggered.connect(self.openDataBase)
        self.closeDatabaseMenu.triggered.connect(self.closeDatabase)
        self.saveDatabaseMenu.triggered.connect(self.saveDatabase)
        self.insertFaceTemplateMenu.triggered.connect(self.createFace)
        self.newOrganizationMenu.triggered.connect(self.createOrganization)
        self.editOrganizationMenu.triggered.connect(self.createOrgEdit)
        self.initListView()

    def initListView(self):
        """
        初始化已签到用户的QListView
        """
        self.model = QStringListModel()
        self.user_list = []
        self.model.setStringList(self.user_list)
        self.userListView.setModel(self.model)

    def addUser(self, name, number):
        """
        在已签到的用户的列表里面增加一个人员
        """
        if name not in self.user_list:
            self.user_list.append(name + "\t" + number)
            self.model.setStringList(self.user_list)

    def openCamera(self):
        if self.databaseConnection is None:
            QMessageBox(QMessageBox.Warning, '警告', '请先连接到数据库').exec_()
            return
        chooseOrgWidget = ChooseOrgWidget(self.databaseConnection, self)
        chooseOrgWidget.exec_()
        if self.organization == "":
            QMessageBox(QMessageBox.Warning, '警告', '未选择组织，请重新选择').exec_()
            return
        # 将摄像头部件附加到主界面上
        self.cameraWidget = CameraWidget(self.cameraView)
        # 设置摄像头获取到图像后的回调函数
        self.cameraWidget.setonGetFrameFunc(self.onGetFrameFunc)
        # 设置摄像头图像显示前的回调函数
        self.cameraWidget.setBeforeDisplayFrame(self.beforeDisplayFrame)
        self.openCameraBtn.hide()
        # 开启开始检测人脸的标志
        self.start_detect = True

    def manuallyRecord(self):
        """
        手动录入签到信息
        """
        name = self.nameEdit.text()
        number = self.numberEdit.text()
        if name.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        if number.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        self.addUser(name, number)

    def onGetFrameFunc(self, frame):
        """
        获取到摄像头一帧时调用此函数，在此函数中进行人脸识别
        """
        small_frame = cv2.resize(frame, (0, 0), fx=0.25, fy=0.25)
        cur_frame = cv2.cvtColor(small_frame, cv2.COLOR_BGR2RGB)
        # 每两帧检测一次，降低开销
        if self.process_this_frame:
            # 记录人脸识别算法的开始时间
            begin_time = time.time()
            self.face_locations, self.face_names, self.face_numbers = detect_frame(
                cur_frame, self.known_face_encodings, self.known_face_names, self.known_face_numbers, tolerance=0.4)
            # 记录人脸识别算法的结束时间
            end_time = time.time()
            # 计算算法耗时，并转为毫秒
            if len(self.face_locations) != 0:
                self.timeCost = (end_time - begin_time) * 1000
                # print('人脸识别算法运行时间：%.1fms' % self.timeCost)
        self.process_this_frame = not self.process_this_frame
        # 不对图像做任何处理，直接返回
        return frame

    def beforeDisplayFrame(self, frame):
        """
        在显示摄像头的图像前调用此函数对一帧图像进行处理， 返回值为修改过的一帧图像
        """
        # 绘制人脸的方框
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # 之前保存的坐标被缩小了四分之一，现在还原回去
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

        return frame

    def openDataBase(self):
        """
        打开指定的数据库文件
        """
        fname = QFileDialog.getOpenFileName(self.mainWindow, '打开数据库', './', "DataBaseFiles (*.db)")
        if fname[0] == "":
            return
        # 创建数据库连接
        self.databaseConnection = openDatabase(fname[0])
        # 更新状态栏
        filename = fname[0].split("/")[-1]
        self.database_filename = filename

    def closeDatabase(self):
        """
        关闭数据库连接
        """
        self.cameraWidget.close()
        self.cameraWidget = None
        self.openCameraBtn.show()
        closeDataBase(self.databaseConnection)
        self.databaseConnection = None
        # 关闭开始检测人脸的标志
        self.start_detect = False

    def saveDatabase(self):
        """
        保存数据库文件
        """
        pass

    def createFace(self):
        """
        新建人脸信息
        """
        if self.databaseConnection is None:
            QMessageBox(QMessageBox.Warning, '警告', '请先连接到数据库').exec_()
            return
        self.addFaceWidget = AddFaceWidget(self.databaseConnection)

    def createOrganization(self):
        """
        新增组织信息
        """
        if self.databaseConnection is None:
            QMessageBox(QMessageBox.Warning, '警告', '请先连接到数据库').exec_()
            return
        self.addFaceWidget = AddOrganizationWidget(self.databaseConnection)

    def createOrgEdit(self):
        if self.databaseConnection is None:
            QMessageBox(QMessageBox.Warning, '警告', '请先连接到数据库').exec_()
            return
        self.orgEditWidget = OrgEditWidget(self.databaseConnection)
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EntryWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
