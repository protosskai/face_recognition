# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 13:56
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : AddOrganizationWidget.py
# @Software: PyCharm


from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from db import *
from base.baseAddOrgnization import Ui_AddOrgnizationWidget
from sqlite3 import IntegrityError


class AddOrganizationWidget(Ui_AddOrgnizationWidget, QWidget):

    def __init__(self, conn, parent=None):
        super().__init__()
        self.setupUi(self)
        # 初始化UI界面及各个控件
        self.initUI()
        # 保存数据库连接
        self.conn = conn
        self.show()

    def initUI(self):
        """
        初始化UI界面及各个控件
        """
        self.exitBtn.clicked.connect(self.closeSelf)
        self.saveBtn.clicked.connect(self.saveOrganization)

    def closeSelf(self):
        self.close()

    def saveOrganization(self):
        name = self.nameEdit.text()
        owner = self.ownerEdit.text()
        if name.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        if owner.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '姓名或编号不能为空').exec_()
            return
        try:
            insert_organization(self.conn, name, owner)
            QMessageBox.about(self, "成功", "添加成功")
        except IntegrityError:
            QMessageBox(QMessageBox.Warning, '警告', '已存在相同名称的组织').exec_()
        # 清除各个控件的内容和用到的变量
        self.clear()

    def clear(self):
        """
        清除各个控件的内容和用到的变量
        """
        self.nameEdit.setText("")
        self.ownerEdit.setText("")


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    conn = openDatabase("./test.db")
    addOrganizationWidget = AddOrganizationWidget(conn)
    sys.exit(app.exec_())
