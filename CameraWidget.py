# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : CameraWidget.py
# @Software: PyCharm

from PyQt5 import QtCore
from PyQt5.Qt import *
from PyQt5.QtGui import *
import cv2


class CameraWidget(QWidget):

    def __init__(self, parent=None):
        super().__init__(parent)
        if parent is not None:
            width = parent.size().width()
            height = parent.size().height()
        else:
            width = 640
            height = 480
        self.resize(width, height)
        self.camera = cv2.VideoCapture(0)
        self.labelCamera = QLabel(self)
        self.labelCamera.resize(width, height)
        # 定时器
        self._timer = QtCore.QTimer(self)
        self._timer.timeout.connect(self._queryFrame)
        self._timer.setInterval(15)
        self._timer.start()
        self.show()
        # 回调函数，在外部实现，用来对获取的视频帧进行处理
        self.onGetFrameFunc = None  # 当opencv获取到一帧图像后调用此函数
        self.beforeDisplayFrame = None  # 在显示图像前调用此函数

    def setonGetFrameFunc(self, func):
        self.onGetFrameFunc = func

    def setBeforeDisplayFrame(self, func):
        self.beforeDisplayFrame = func

    def changeTimerInterval(self, number):
        self._timer.stop()
        self._timer.setInterval(number)
        self._timer.start()

    @QtCore.pyqtSlot()
    def _queryFrame(self):
        '''
        循环捕获图片
        '''
        ret, img = self.camera.read()
        cv2.flip(img, 1, img)
        if self.onGetFrameFunc is not None:
            img = self.onGetFrameFunc(img)
        cur_frame = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        heigt, width = cur_frame.shape[:2]
        if self.beforeDisplayFrame is not None:
            cur_frame = self.beforeDisplayFrame(cur_frame)
        pixmap = QImage(cur_frame, width, heigt, QImage.Format_RGB888)
        pixmap = QPixmap.fromImage(pixmap)
        self.labelCamera.setPixmap(pixmap)
