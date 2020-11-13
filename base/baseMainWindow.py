# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/MainWindow.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_mainWindow(object):
    def setupUi(self, mainWindow):
        mainWindow.setObjectName("mainWindow")
        mainWindow.resize(1133, 537)
        mainWindow.setAnimated(True)
        mainWindow.setDocumentMode(False)
        self.centralwidget = QtWidgets.QWidget(mainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.cameraView = QtWidgets.QLabel(self.centralwidget)
        self.cameraView.setGeometry(QtCore.QRect(0, 0, 640, 480))
        self.cameraView.setStyleSheet("background-color: rgb(0, 0, 0);")
        self.cameraView.setText("")
        self.cameraView.setObjectName("cameraView")
        self.openCameraBtn = QtWidgets.QPushButton(self.centralwidget)
        self.openCameraBtn.setGeometry(QtCore.QRect(230, 190, 161, 91))
        self.openCameraBtn.setObjectName("openCameraBtn")
        self.userListView = QtWidgets.QListView(self.centralwidget)
        self.userListView.setGeometry(QtCore.QRect(950, 30, 181, 411))
        self.userListView.setObjectName("userListView")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(950, -10, 131, 41))
        self.label.setAlignment(QtCore.Qt.AlignLeading|QtCore.Qt.AlignLeft|QtCore.Qt.AlignVCenter)
        self.label.setObjectName("label")
        self.userNumLabel = QtWidgets.QLabel(self.centralwidget)
        self.userNumLabel.setGeometry(QtCore.QRect(990, 440, 131, 41))
        self.userNumLabel.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.userNumLabel.setObjectName("userNumLabel")
        self.groupBox = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox.setGeometry(QtCore.QRect(650, 320, 291, 161))
        self.groupBox.setObjectName("groupBox")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(0, 40, 67, 17))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(0, 90, 67, 17))
        self.label_3.setObjectName("label_3")
        self.nameEdit = QtWidgets.QLineEdit(self.groupBox)
        self.nameEdit.setGeometry(QtCore.QRect(50, 30, 221, 31))
        self.nameEdit.setObjectName("nameEdit")
        self.numberEdit = QtWidgets.QLineEdit(self.groupBox)
        self.numberEdit.setGeometry(QtCore.QRect(50, 80, 221, 31))
        self.numberEdit.setObjectName("numberEdit")
        self.recordBtn = QtWidgets.QPushButton(self.groupBox)
        self.recordBtn.setGeometry(QtCore.QRect(100, 130, 89, 25))
        self.recordBtn.setObjectName("recordBtn")
        self.groupBox_2 = QtWidgets.QGroupBox(self.centralwidget)
        self.groupBox_2.setGeometry(QtCore.QRect(650, 0, 291, 311))
        self.groupBox_2.setObjectName("groupBox_2")
        self.curUserImg = QtWidgets.QLabel(self.groupBox_2)
        self.curUserImg.setGeometry(QtCore.QRect(10, 30, 256, 192))
        self.curUserImg.setStyleSheet("background-color: rgb(85, 87, 83);")
        self.curUserImg.setText("")
        self.curUserImg.setObjectName("curUserImg")
        self.curUserName = QtWidgets.QLabel(self.groupBox_2)
        self.curUserName.setGeometry(QtCore.QRect(100, 230, 161, 17))
        self.curUserName.setObjectName("curUserName")
        self.curUserNumber = QtWidgets.QLabel(self.groupBox_2)
        self.curUserNumber.setGeometry(QtCore.QRect(100, 260, 171, 17))
        self.curUserNumber.setObjectName("curUserNumber")
        self.curTimeCost = QtWidgets.QLabel(self.groupBox_2)
        self.curTimeCost.setGeometry(QtCore.QRect(0, 290, 271, 17))
        self.curTimeCost.setObjectName("curTimeCost")
        mainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(mainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 1133, 28))
        self.menubar.setObjectName("menubar")
        self.fileMenu = QtWidgets.QMenu(self.menubar)
        self.fileMenu.setObjectName("fileMenu")
        self.menu = QtWidgets.QMenu(self.menubar)
        self.menu.setObjectName("menu")
        self.menu_2 = QtWidgets.QMenu(self.menubar)
        self.menu_2.setObjectName("menu_2")
        self.menu_3 = QtWidgets.QMenu(self.menubar)
        self.menu_3.setObjectName("menu_3")
        mainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(mainWindow)
        self.statusbar.setObjectName("statusbar")
        mainWindow.setStatusBar(self.statusbar)
        self.openDatabaseMenu = QtWidgets.QAction(mainWindow)
        self.openDatabaseMenu.setObjectName("openDatabaseMenu")
        self.closeDatabaseMenu = QtWidgets.QAction(mainWindow)
        self.closeDatabaseMenu.setObjectName("closeDatabaseMenu")
        self.saveDatabaseMenu = QtWidgets.QAction(mainWindow)
        self.saveDatabaseMenu.setObjectName("saveDatabaseMenu")
        self.exportDatabaseMenu = QtWidgets.QAction(mainWindow)
        self.exportDatabaseMenu.setObjectName("exportDatabaseMenu")
        self.showFaceTemplateMenu = QtWidgets.QAction(mainWindow)
        self.showFaceTemplateMenu.setObjectName("showFaceTemplateMenu")
        self.insertFaceTemplateMenu = QtWidgets.QAction(mainWindow)
        self.insertFaceTemplateMenu.setObjectName("insertFaceTemplateMenu")
        self.editFaceTemplateMenu = QtWidgets.QAction(mainWindow)
        self.editFaceTemplateMenu.setObjectName("editFaceTemplateMenu")
        self.exitMenu = QtWidgets.QAction(mainWindow)
        self.exitMenu.setObjectName("exitMenu")
        self.documentMenu = QtWidgets.QAction(mainWindow)
        self.documentMenu.setObjectName("documentMenu")
        self.aboutMenu = QtWidgets.QAction(mainWindow)
        self.aboutMenu.setObjectName("aboutMenu")
        self.newOrganizationMenu = QtWidgets.QAction(mainWindow)
        self.newOrganizationMenu.setObjectName("newOrganizationMenu")
        self.showOrganizationMenu = QtWidgets.QAction(mainWindow)
        self.showOrganizationMenu.setObjectName("showOrganizationMenu")
        self.editOrganizationMenu = QtWidgets.QAction(mainWindow)
        self.editOrganizationMenu.setObjectName("editOrganizationMenu")
        self.fileMenu.addAction(self.openDatabaseMenu)
        self.fileMenu.addAction(self.closeDatabaseMenu)
        self.fileMenu.addAction(self.saveDatabaseMenu)
        self.fileMenu.addAction(self.exportDatabaseMenu)
        self.fileMenu.addAction(self.exitMenu)
        self.menu.addAction(self.showFaceTemplateMenu)
        self.menu.addAction(self.insertFaceTemplateMenu)
        self.menu.addAction(self.editFaceTemplateMenu)
        self.menu_2.addAction(self.documentMenu)
        self.menu_2.addAction(self.aboutMenu)
        self.menu_3.addAction(self.showOrganizationMenu)
        self.menu_3.addAction(self.newOrganizationMenu)
        self.menu_3.addAction(self.editOrganizationMenu)
        self.menubar.addAction(self.fileMenu.menuAction())
        self.menubar.addAction(self.menu.menuAction())
        self.menubar.addAction(self.menu_3.menuAction())
        self.menubar.addAction(self.menu_2.menuAction())

        self.retranslateUi(mainWindow)
        QtCore.QMetaObject.connectSlotsByName(mainWindow)

    def retranslateUi(self, mainWindow):
        _translate = QtCore.QCoreApplication.translate
        mainWindow.setWindowTitle(_translate("mainWindow", "人脸考勤系统"))
        self.openCameraBtn.setText(_translate("mainWindow", "打开摄像头"))
        self.label.setText(_translate("mainWindow", "已签到人员："))
        self.userNumLabel.setText(_translate("mainWindow", "0人/30人"))
        self.groupBox.setTitle(_translate("mainWindow", "手动录入"))
        self.label_2.setText(_translate("mainWindow", "姓名："))
        self.label_3.setText(_translate("mainWindow", "编号："))
        self.recordBtn.setText(_translate("mainWindow", "录入"))
        self.groupBox_2.setTitle(_translate("mainWindow", "当前信息"))
        self.curUserName.setText(_translate("mainWindow", "姓名："))
        self.curUserNumber.setText(_translate("mainWindow", "编号："))
        self.curTimeCost.setText(_translate("mainWindow", "耗时："))
        self.fileMenu.setTitle(_translate("mainWindow", "文件"))
        self.menu.setTitle(_translate("mainWindow", "人脸管理"))
        self.menu_2.setTitle(_translate("mainWindow", "帮助"))
        self.menu_3.setTitle(_translate("mainWindow", "组织管理"))
        self.openDatabaseMenu.setText(_translate("mainWindow", "打开数据库文件"))
        self.closeDatabaseMenu.setText(_translate("mainWindow", "关闭数据库文件"))
        self.saveDatabaseMenu.setText(_translate("mainWindow", "保存数据库文件"))
        self.exportDatabaseMenu.setText(_translate("mainWindow", "导出数据库文件"))
        self.showFaceTemplateMenu.setText(_translate("mainWindow", "人脸模板查看"))
        self.insertFaceTemplateMenu.setText(_translate("mainWindow", "人脸模板录入"))
        self.editFaceTemplateMenu.setText(_translate("mainWindow", "人脸模板编辑"))
        self.exitMenu.setText(_translate("mainWindow", "退出"))
        self.documentMenu.setText(_translate("mainWindow", "使用文档"))
        self.aboutMenu.setText(_translate("mainWindow", "关于本系统"))
        self.newOrganizationMenu.setText(_translate("mainWindow", "新建组织"))
        self.showOrganizationMenu.setText(_translate("mainWindow", "组织一览"))
        self.editOrganizationMenu.setText(_translate("mainWindow", "编辑组织"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    mainWindow = QtWidgets.QMainWindow()
    ui = Ui_mainWindow()
    ui.setupUi(mainWindow)
    mainWindow.show()
    sys.exit(app.exec_())
