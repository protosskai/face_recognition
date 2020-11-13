'''
Description: 
version: 
Auther: protosskai
Date: 2020-11-13 12:10:33
LastEditTime: 2020-11-13 12:49:03
'''

import sqlite3


def insert_student(cursor, name, number, sex, class_name="无", age=0):
    sql = "INSERT INTO Student (name, age, class, number, sex) VALUES (\"{name}\", {age}, \"{class_name}\", \"{number}\", \"{sex}\");".format(
        name=name,
        age=age, class_name=class_name, number=number, sex=sex)
    cursor.execute(sql)


def query_student_by_number(cursor, number):
    sql = "select * from Student where number=\"{number}\";".format(
        number=number)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    return result


def update_student_by_number(cursor, number, name=None, age=None, class_name=None, sex=None):
    # 查询原有的记录
    pre_record = query_student_by_number(cursor, number)
    # 构造更新数据的sql
    sql = "update Student set name=\"{name}\", age={age}, class=\"{class_name}\", sex=\"{sex}\" where number=\"{number}\";"
    if len(pre_record) <= 0:
        return
    index = 0
    # 将元祖转化为列表，便于后面的修改
    for one in pre_record:
        pre_record[index] = list(one)
        index += 1
    for one in pre_record:
        if name is not None:
            one[1] = name
        if age is not None:
            one[2] = age
        if class_name is not None:
            one[3] = class_name
        if sex is not None:
            one[4] = sex
        sql = sql.format(
            number=number, name=one[1], age=one[2], class_name=one[3], sex=one[4])
        cursor.execute(sql)


def openDatabase(filename):
    """
    打开指定路径的数据库文件，并返回连接对象
    """
    conn = sqlite3.connect(filename)
    print("Opened database successfully")
    return conn


def closeDataBase(connection):
    """
    关闭数据库连接
    """
    if connection is not None:
        connection.commit()
        connection.close()

# 连接数据库(如果不存在则创建)
# conn = sqlite3.connect('test.db')
# print("Opened database successfully")
#
# # 创建游标
# cursor = conn.cursor()
#
# #  insert_student(cursor, "zhangjiajia", "2017081022", "男", "电子八班", 21)
# #  result = query_student_by_number(cursor, "2017081023")
# update_student_by_number(cursor, "2017081023", "zhangjiajia", 15)
# # 关闭游标
# cursor.close()
# # 提交事物
# conn.commit()
# # 关闭连接
# conn.close()
