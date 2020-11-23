# -*- coding: utf-8 -*-
# @Time    : 2020/11/22 21:11
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : OrgEditWidget.py
# @Software: PyCharm
from PyQt5 import QtCore
from PyQt5.QtCore import QStringListModel, QModelIndex
from PyQt5.QtWidgets import *
from base.baseOrgEdit import Ui_orgEdit
from db import *
from OrgAddStudentWidget import OrgAddStudentWidget


class OrgEditWidget(Ui_orgEdit, QWidget):

    def __init__(self, conn, parent=None):
        super().__init__()
        self.setupUi(self)
        # 保存数据库连接
        self.conn = conn
        # 初始化UI界面及各个控件
        self.initUI()
        self.org_name = ""
        # 显示widget
        self.show()

    def initOrgListView(self):
        """
        初始化组织列表
        """
        self.OrgModel = QStringListModel()
        self.orgList = self.loadOrganizationData()  # 加载所有的组织
        self.OrgModel.setStringList(self.orgList)
        self.orgListView.setModel(self.OrgModel)

    def initMemberListView(self):
        """
        初始化成员列表
        """
        self.MemberModel = QStringListModel()
        self.memberList = []
        self.MemberModel.setStringList(self.memberList)
        self.memberListView.setModel(self.MemberModel)

    def clearMember(self):
        """
        清空成员列表
        """
        self.memberList = []
        self.MemberModel.setStringList(self.memberList)

    def addMember(self, name, number):
        """
        在成员列表里面新增一个人员
        """
        self.memberList.append(name + "\t" + number)
        self.MemberModel.setStringList(self.memberList)

    def initUI(self):
        """
        初始化UI界面及各个控件
        """
        self.orgListView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑内容
        self.memberListView.setEditTriggers(QAbstractItemView.NoEditTriggers)  # 不可编辑内容
        self.initOrgListView()
        self.initMemberListView()
        self.orgListView.clicked.connect(self.displayStudent)
        self.addMemberBtn.clicked.connect(self.addOrgMember)

    def addOrgMember(self):
        org_name = self.org_name
        if org_name == "":
            QMessageBox(QMessageBox.Warning, '警告', '请先选择组织!').exec_()
            return
        self.OrgAddMember = OrgAddStudentWidget(self.conn, org_name, self)

    def displayStudent(self, index):
        """
        每次单击组织名称后更新右边的学生列表
        """
        self.clearMember()
        org_id = query_org_id_by_org_name(self.conn, index.data())
        org_name = index.data()
        self.org_name = org_name
        students = query_stus_by_org_id(self.conn, org_id)
        pairs = []
        for student in students:
            student_record = query_student_by_id(self.conn, student[1])
            pairs.append((student_record[1], student_record[4]))
        for pair in pairs:
            self.addMember(pair[0], pair[1])

    def loadOrganizationData(self):
        orgs = query_all_organization(self.conn)
        return [i[1] for i in orgs]
