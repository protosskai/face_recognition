# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file './ui/ExportExcel.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(449, 227)
        self.widget = QtWidgets.QWidget(Form)
        self.widget.setGeometry(QtCore.QRect(10, 30, 391, 27))
        self.widget.setObjectName("widget")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.widget)
        self.horizontalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.label_3 = QtWidgets.QLabel(self.widget)
        self.label_3.setObjectName("label_3")
        self.horizontalLayout_2.addWidget(self.label_3)
        self.orgComboBox = QtWidgets.QComboBox(self.widget)
        self.orgComboBox.setObjectName("orgComboBox")
        self.horizontalLayout_2.addWidget(self.orgComboBox)
        self.widget1 = QtWidgets.QWidget(Form)
        self.widget1.setGeometry(QtCore.QRect(10, 170, 168, 33))
        self.widget1.setObjectName("widget1")
        self.horizontalLayout_3 = QtWidgets.QHBoxLayout(self.widget1)
        self.horizontalLayout_3.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout_3.setObjectName("horizontalLayout_3")
        self.exportBtn = QtWidgets.QPushButton(self.widget1)
        self.exportBtn.setObjectName("exportBtn")
        self.horizontalLayout_3.addWidget(self.exportBtn)
        self.exitBtn = QtWidgets.QPushButton(self.widget1)
        self.exitBtn.setObjectName("exitBtn")
        self.horizontalLayout_3.addWidget(self.exitBtn)
        self.widget2 = QtWidgets.QWidget(Form)
        self.widget2.setGeometry(QtCore.QRect(10, 100, 391, 28))
        self.widget2.setObjectName("widget2")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.widget2)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.label = QtWidgets.QLabel(self.widget2)
        self.label.setObjectName("label")
        self.horizontalLayout.addWidget(self.label)
        self.startDateEdit = QtWidgets.QDateEdit(self.widget2)
        self.startDateEdit.setObjectName("startDateEdit")
        self.horizontalLayout.addWidget(self.startDateEdit)
        self.label_2 = QtWidgets.QLabel(self.widget2)
        self.label_2.setObjectName("label_2")
        self.horizontalLayout.addWidget(self.label_2)
        self.endDateEdit = QtWidgets.QDateEdit(self.widget2)
        self.endDateEdit.setObjectName("endDateEdit")
        self.horizontalLayout.addWidget(self.endDateEdit)

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "导出excel"))
        self.label_3.setText(_translate("Form", "选择组织："))
        self.exportBtn.setText(_translate("Form", "导出"))
        self.exitBtn.setText(_translate("Form", "退出"))
        self.label.setText(_translate("Form", "开始时间："))
        self.label_2.setText(_translate("Form", "结束时间："))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
