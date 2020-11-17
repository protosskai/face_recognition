# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : tool.py
# @Software: PyCharm

import PIL.Image
import numpy as np
from PIL import ImageFile
import cv2
import shutil
import os


def load_image_file(file, size=(-1, -1), mode='RGB'):
    """
    读取将一张图片，并转为numpy数组

    :param file: 图片的文件名
    :param size: 如果size被赋值了，就将读入的图片按照size的宽高来修改大小
    :param mode: format to convert the image to. Only 'RGB' (8-bit RGB, 3 channels) and 'L' (black and white) are supported.
    :return: 图片的numpy数组
    """
    im = PIL.Image.open(file)
    (x, y) = im.size
    if size[0] != -1 and size[1] != -1:
        ratio = y / x
        new_x = size[0]
        new_y = int(size[0] * ratio)
        im = im.resize((new_x, new_y))
    if mode:
        im = im.convert(mode)
    return np.array(im)


def copy_file(src, dest):
    """
    将原文件复制到目标文件
    :param src: 原文件地址
    :param dest: 目标文件地址
    """
    shutil.copyfile(src, dest)


def get_file_extension_name(path):
    """
    获取文件扩展名
    :param path: 文件的路径
    """
    return os.path.splitext(path)[-1]
