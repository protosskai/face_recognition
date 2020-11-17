# -*- coding: utf-8 -*-
# @Time    : 2020/11/17 16:41
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : ChooseOrgWidget.py
# @Software: PyCharm

from PyQt5.QtWidgets import *
from base.baseChooseOrgWidget import Ui_chooseOrgWidget
from db import *


class ChooseOrgWidget(Ui_chooseOrgWidget, QDialog):

    def __init__(self, conn, parent):
        super().__init__()
        # 保存指向父窗口的引用
        self.parent = parent
        self.setupUi(self)
        # 保存数据库连接
        self.conn = conn
        # 初始化UI界面及各个控件
        self.initUI()

    def initUI(self):
        # 加载所有的组织名
        orgs = query_all_organization(self.conn)
        for org in orgs:
            self.organizationComboBox.addItem(org[1])
        # 绑定按钮事件
        self.okButton.clicked.connect(self.ok)
        self.cancelButton.clicked.connect(self.closeSelf)

    def ok(self):
        self.parent.organization = self.organizationComboBox.currentText()
        self.parent.cur_org_id = query_org_id_by_org_name(self.conn, self.parent.organization)
        self.close()

    def closeSelf(self):
        self.close()
