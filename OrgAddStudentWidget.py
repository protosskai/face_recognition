# -*- coding: utf-8 -*-
# @Time    : 2020/11/23 20:23
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : OrgAddStudentWidget.py
# @Software: PyCharm

from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel, QModelIndex
from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtWidgets import *
from PyQt5.QtWidgets import *
from base.baseOrgAddStu import Ui_Form
from db import *


class OrgAddStudentWidget(Ui_Form, QWidget):

    def __init__(self, conn, org_name, parent=None):
        super().__init__()
        self.setupUi(self)
        self.org_name = org_name
        self.parent = parent
        # 保存数据库连接
        self.conn = conn
        # 初始化UI界面及各个控件
        self.initUI()
        # 显示widget
        self.show()

    def initUI(self):
        self.numberEdit.textChanged.connect(self.displayName)
        self.addButton.clicked.connect(self.org_add_member)
        self.exitButton.clicked.connect(self.closeSelf)

    def closeSelf(self):
        self.close()

    def displayName(self):
        number = self.numberEdit.text()
        if number.strip() == "":
            return
        student = query_student_by_number(self.conn, number.strip())
        if student == []:
            return
        name = student[0][1]
        self.nameEdit.setText(name)

    def org_add_member(self):
        number = self.numberEdit.text()
        if number.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '请输入学号').exec_()
            return
        org_id = query_org_id_by_org_name(self.conn, self.org_name)
        student = query_student_by_number(self.conn, number.strip())
        if student == []:
            QMessageBox(QMessageBox.Warning, '警告', '不存在该学号对应的学生！').exec_()
            return
        stu_id = student[0][0]
        insert_map(self.conn, stu_id, org_id)
        QMessageBox.about(self, "成功", "添加成功")
