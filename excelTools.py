# -*- coding: utf-8 -*-
# @Time    : 2020/11/25 21:30
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : excelTools.py
# @Software: PyCharm


import xlwt


# 设置表格样式
def set_stlye(name, height, colour_index, bold=False):
    # 初始化样式
    style = xlwt.XFStyle()
    # 创建字体
    font = xlwt.Font()
    font.bold = bold
    font.colour_index = colour_index
    font.height = height
    font.name = name
    style.font = font
    return style


# 写入数据
def write_excel(data, filename):
    f = xlwt.Workbook()
    sheet1 = f.add_sheet('sheet1', cell_overwrite_ok=True)
    row0 = ['姓名', '学号', '组织', '签到日期']
    for i in range(0, len(row0)):
        sheet1.write(0, i, row0[i], set_stlye("宋体", 220, 0, True))
    row = 1
    for i in data:
        for t, v in enumerate(i):
            sheet1.write(row, t, v, set_stlye("宋体", 220, 0, True))
        row += 1
    f.save(filename)

# if __name__ == '__main__':
#     write_excel()
