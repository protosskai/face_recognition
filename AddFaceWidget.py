# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    :
# @File    : AddFaceWidget.py
# @Software: PyCharm

from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.Qt import *
from PyQt5.QtCore import *
from PyQt5.QtGui import *
from CameraWidget import CameraWidget
from PyQt5.QtWidgets import *
from base.baseAddFace import Ui_AddFaceWidget


class AddFaceWidget(Ui_AddFaceWidget, QWidget):

    def __init__(self):
        super().__init__()
        self.setupUi(self)
        # 初始化UI界面及各个控件
        self.initUI()

    def initUI(self):
        """
        初始化UI界面及各个控件
        """
        pass


if __name__ == "__main__":
    import sys

    app = QtWidgets.QApplication(sys.argv)
    addFaceWidget = AddFaceWidget()
    addFaceWidget.show()
    sys.exit(app.exec_())
