from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CameraWidget import CameraWidget
from base.baseMainWindow import Ui_mainWindow
import cv2
from face_api import *
import time
from tools import *


class EntryWindow(Ui_mainWindow):

    def __init__(self, MainWindow):
        super().__init__()
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

    def updateUI(self):
        # 更新每次人脸检测耗时的标签
        timeCostStr = "耗时为:" + str(int(self.timeCost)) + "ms"
        self.curTimeCost.setText(timeCostStr)
        # 更新当前识别出的人的人脸图片和人名和编号
        imgViewSize = (self.curUserImg.size().width(),
                       self.curUserImg.size().height())
        if len(self.face_names) > 0 and self.face_names[0] != "Unknown":
            name = self.face_names[0]
            numbers = self.face_numbers[0]
            image_file_path = self.image_templates_dir + name + "_" + numbers +".jpg"
            image = load_image_file(image_file_path, imgViewSize)
            pixmap = QImage(
                image, imgViewSize[0], imgViewSize[1], QImage.Format_RGB888)
            pixmap = QPixmap.fromImage(pixmap)
            self.curUserImg.setPixmap(pixmap)
        # 更新名称和学号标签
        pass
    def initFaceDetect(self):
        # 加载人脸的模板图片
        self.known_face_encodings, self.known_face_tags = load_image_templates(
            self.image_templates_dir)
        self.known_face_names = [tag.split("_")[0] for tag in self.known_face_tags]
        self.known_face_numbers = [tag.split("_")[1] for tag in self.known_face_tags]
        self.face_locations = []
        self.face_names = []
        self.timeCost = 0.0
        # 标记位，用来降低人脸检测开销
        self.process_this_frame = True

    def initUI(self):
        self.openCameraBtn.clicked.connect(self.openCamera)
        self.recordBtn.clicked.connect(self.manuallyRecord)

    def openCamera(self):
        # 将摄像头部件附加到主界面上
        self.cameraWidget = CameraWidget(self.cameraView)
        # 设置摄像头获取到图像后的回调函数
        self.cameraWidget.setonGetFrameFunc(self.onGetFrameFunc)
        # 设置摄像头图像显示前的回调函数
        self.cameraWidget.setBeforeDisplayFrame(self.beforeDisplayFrame)
        self.openCameraBtn.hide()

    def manuallyRecord(self):
        print("manuallyRecord")

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
                cur_frame, self.known_face_encodings, self.known_face_names, self.known_face_numbers)
            # 记录人脸识别算法的结束时间
            end_time = time.time()
            # 计算算法耗时，并转为毫秒
            if len(self.face_locations) != 0:
                self.timeCost = (end_time-begin_time) * 1000
                print('人脸识别算法运行时间：%.1fms' % self.timeCost)
        self.process_this_frame = not self.process_this_frame
        # 不对图像做任何处理，直接返回
        return frame

    def beforeDisplayFrame(self, frame):
        """
        在显示摄像头的图像前调用此函数对一帧图像进行处理， 返回值为修改过的一帧图像
        """
        # Display the results
        for (top, right, bottom, left), name in zip(self.face_locations, self.face_names):
            # Scale back up face locations since the frame we detected in was scaled to 1/4 size
            top *= 4
            right *= 4
            bottom *= 4
            left *= 4

            # Draw a box around the face
            cv2.rectangle(frame, (left, top), (right, bottom), (0, 0, 255), 2)

            # Draw a label with a name below the face
            cv2.rectangle(frame, (left, bottom - 35),
                          (right, bottom), (0, 0, 255), cv2.FILLED)
            font = cv2.FONT_HERSHEY_DUPLEX
            cv2.putText(frame, name, (left + 6, bottom - 6),
                        font, 1.0, (255, 255, 255), 1)

        return frame


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = EntryWindow(MainWindow)
    MainWindow.show()
    sys.exit(app.exec_())
