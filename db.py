'''
Description: 
version: 
Auther: protosskai
Date: 2020-11-13 12:10:33
LastEditTime: 2020-11-13 12:49:03
'''

import sqlite3


def insert_student(conn, name, number, sex, age, class_name="无"):
    """
    插入一条学生表的记录
    """
    cursor = conn.cursor()
    sql = "INSERT INTO Student (name, age, class, number, sex) VALUES (\"{name}\", {age}, \"{class_name}\", \"{number}\", \"{sex}\");".format(
        name=name,
        age=age, class_name=class_name, number=number, sex=sex)
    cursor.execute(sql)
    conn.commit()


def insert_organization(conn, name, owner):
    """
    插入一条组织表达记录
    """
    cursor = conn.cursor()
    sql = "INSERT INTO Organization (name, owner) VALUES (\"{name}\", \"{owner}\");".format(name=name, owner=owner)
    cursor.execute(sql)
    conn.commit()


def insert_map(conn, stu_id, org_id):
    """
    插入一条学生和组织映射表的记录
    """
    cursor = conn.cursor()
    sql = "INSERT INTO Stu_Org (stu_id, org_id) VALUES ({stu_id},{org_id});".format(stu_id=stu_id, org_id=org_id)
    cursor.execute(sql)
    conn.commit()


def query_id_by_number(conn, number):
    """
    通过学号查询学生id
    """
    students = query_student_by_number(conn, number)
    if len(students) != 0:
        student = students[0]
        return student[0]
    else:
        return None


def query_name_by_number(conn, number):
    """
    通过学号查询学生姓名
    """
    students = query_student_by_number(conn, number)
    if len(students) != 0:
        student = students[0]
        return student[1]
    return ""


def query_stus_by_org_id(conn, org_id):
    """
    查询map表里面指定组织的所有学生
    """
    cursor = conn.cursor()
    sql = "select * from Stu_Org where org_id={};".format(org_id)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    return result


def query_number_by_id(conn, id):
    """
    通过学生的id查询编号
    """
    student = query_student_by_id(conn, id)
    if student != None:
        return student[4]
    return None


def check_number_in_org(conn, number, org_id):
    """
    检查指定编号的学生是否在某个组织中
    """
    stu_ids = [i[1] for i in query_stus_by_org_id(conn, org_id)]
    numbers = []
    for stu_id in stu_ids:
        numbers.append(query_number_by_id(conn, stu_id))
    return number in numbers


def query_organization_by_name(conn, name):
    """
    通过名称查询组织
    """
    cursor = conn.cursor()
    sql = "select * from Organization where name=\"{name}\";".format(
        name=name)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    return result


def query_all_organization(conn):
    """
    查询所有的组织
    """
    cursor = conn.cursor()
    sql = "select * from Organization where 1=1;"
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    return result


def query_org_id_by_org_name(conn, org_name):
    """
    通过组织到名字查询组织的id
    """
    cursor = conn.cursor()
    sql = "select * from Organization where name=\"{org_name}\"".format(org_name=org_name)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    result = [i[0] for i in result]
    if len(result) > 0:
        return result[0]
    return None


def query_student_by_number(conn, number):
    """
    通过编号查询学生
    """
    cursor = conn.cursor()
    sql = "select * from Student where number=\"{number}\";".format(
        number=number)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    return result


def query_student_by_id(conn, id):
    """
    通过id查学生
    """
    cursor = conn.cursor()
    sql = "select * from Student where id={id};".format(
        id=id)
    cur = cursor.execute(sql)
    result = []
    # 构建结果列表
    for c in cur:
        result.append(c)
    if len(result) == 0:
        return None
    return result[0]


def update_student_by_number(conn, number, name=None, age=None, class_name=None, sex=None):
    """
    通过学号更新学生的信息
    """
    cursor = conn.cursor()
    # 查询原有的记录
    pre_record = query_student_by_number(conn, number)
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
    conn.commit()


def insert_t_record(conn, student_id, org_id):
    """
    插入一条签到的时间记录
    """
    cursor = conn.cursor()
    sql = "INSERT INTO t_record (student_id, org_id, current_time) VALUES ({student_id}, {org_id}, datetime('now',\'localtime'));".format(
        student_id=student_id, org_id=org_id)
    cursor.execute(sql)
    conn.commit()


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

# conn = openDatabase("./test.db")
