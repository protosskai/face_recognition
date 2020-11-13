# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    :
# @File    : AddFaceWidget.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from base.baseAddFace import Ui_AddFaceWidget
from tools import *
from db import *


class AddFaceWidget(Ui_AddFaceWidget, QWidget):

    def __init__(self, conn, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        # 初始化UI界面及各个控件
        self.initUI()
        # 保存数据库连接
        self.conn = conn
        # 显示widget
        self.show()
        # 初始化人脸模板路径
        self.filePath = ""

    def initUI(self):
        """
        初始化UI界面及各个控件
        """
        self.chooseImageBtn.clicked.connect(self.openImage)
        self.exitBtn.clicked.connect(self.closeSelf)
        self.saveBtn.clicked.connect(self.saveFace)

    def openImage(self):
        # 获取图片文件名
        fname = QFileDialog.getOpenFileName(self, '选择图片', './', "Images (*.png *.xpm *.jpg)")
        if fname[0] == "":
            return
        self.filePath = fname[0]
        # 获取图片显示框的大小
        imgViewSize = (self.userImageLabel.size().width(),
                       self.userImageLabel.size().height())
        # 加载好的图片的numpy数组
        image = load_image_file(self.filePath, imgViewSize)
        # 显示图片
        pixmap = QImage(
            image, imgViewSize[0], imgViewSize[1], QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.userImageLabel.setPixmap(pixmap)

    def closeSelf(self):
        self.close()

    def saveFace(self):
        name = self.nameEdit.text()
        number = self.numberEdit.text()
        if self.ageEdit.text().strip() != "":
            age = int(self.ageEdit.text())
        else:
            age = 0
        sex = self.sexComboBox.currentText()
        if name.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        if number.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        if self.filePath.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '请选择一张图片').exec_()
            return
        insert_student(self.conn, name, number, sex, age)
        destFilePath = "./img_templates/" + name + "_" + number + get_file_extension_name(self.filePath)
        copy_file(self.filePath, destFilePath)
        QMessageBox.about(self, "成功", "添加成功")
        # 清除各个控件的内容和用到的变量
        self.clear()

    def clear(self):
        """
        清除各个控件的内容和用到的变量
        """
        self.filePath = ""
        self.nameEdit.setText("")
        self.numberEdit.setText("")
        self.ageEdit.setText("")
        self.userImageLabel.setPixmap(QPixmap(""))


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    conn = openDatabase("./test.db")
    addFaceWidget = AddFaceWidget(conn)
    sys.exit(app.exec_())
