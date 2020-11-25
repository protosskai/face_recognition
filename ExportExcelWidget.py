# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 22:37
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : ExportExcelWidget.py
# @Software: PyCharm

from PyQt5 import QtWidgets
from PyQt5.Qt import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from base.baseExportExcel import Ui_Form
from tools import *
from db import *
from excelTools import *


class ExportExcelWidget(Ui_Form, QWidget):

    def __init__(self, conn, parent=None):
        super().__init__()
        self.setupUi(self)
        # 保存数据库连接
        self.conn = conn
        # 初始化UI界面及各个控件
        self.initUI()
        # 显示widget
        self.show()

    def initUI(self):
        self.exportBtn.clicked.connect(self.export)
        self.exitBtn.clicked.connect(self.close)
        # 加载所有的组织名
        orgs = query_all_organization(self.conn)
        for org in orgs:
            self.orgComboBox.addItem(org[1])

    def export(self):
        start_time = self.startDateEdit.date().toString(Qt.ISODate)
        end_time = self.endDateEdit.date().toString(Qt.ISODate)
        org_name = self.orgComboBox.currentText()
        if org_name.strip() == "":
            QMessageBox(QMessageBox.Warning, '警告', '请选择一个组织').exec_()
            return
        # filename_url, filetype = QFileDialog.getSaveFileUrl(self, "导出文件", QUrl("./"), "表格文件(*.xls *.xlsx)")
        # filename = filename_url.fileName()
        # if not filename.endswith(".xls") or not filename.endswith("xlsx"):
        #     filename = filename + ".xlsx"
        org_id = query_org_id_by_org_name(self.conn, org_name)
        start_time = str2Date(start_time, "%Y-%m-%d")
        end_time = str2Date(end_time, "%Y-%m-%d")
        t_record_res = query_t_record_with_filter(self.conn, start_time, end_time, org_id)
        print(t_record_res)
        # 接下来导出表格
        output_date = []
        for i in t_record_res:
            student = query_student_by_id(self.conn, i[1])
            student_name = student[1]
            student_number = student[4]
            date_str = date2Str(i[3], "%Y-%m-%d %H:%M:%S")
            output_date.append([student_name, student_number, org_name, date_str])
        filename = "./output_excel/" + datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S") + "-" + org_name + ".xlsx"
        write_excel(output_date, filename)
        QMessageBox.about(self, "成功", "导出成功")
