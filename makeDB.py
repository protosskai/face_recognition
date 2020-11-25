# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 21:13
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : makeDB.py
# @Software: PyCharm
import sqlite3
import sys
import os

if __name__ == '__main__':
    if len(sys.argv) != 2:
        print("请输入要创建的数据库文件的名称,以扩展名(.db)结尾")
        exit(-1)
    filename = sys.argv[1]
    filename = os.path.split(filename)[1]
    if os.path.splitext(filename)[1] != ".db":
        print("请以.db结尾！")
        exit(-1)
    conn = sqlite3.connect(filename)
    conn.close()
