# -*- coding: utf-8 -*-
# @Time    : 2020/11/13 15:19
# @Author  : protosskai
# @Site    : protosskai.github.io
# @File    : face_api.py
# @Software: PyCharm

import face_recognition
import numpy as np
import os


def load_image_templates(image_templates_dir):
    """
    从指定的模板目录获取到人脸模板照片，返回两个list
    第一个list为人脸图片数据encoding的列表，第二个list为相应的人名的列表
    """
    if os.path.isdir(image_templates_dir):
        images = os.listdir(image_templates_dir)
        face_encodings = []
        face_tags = []
        for image in images:
            path = os.path.join(image_templates_dir, image)  # 拼接每个图片的实际路径
            face_image = face_recognition.load_image_file(path)
            face_encoding = face_recognition.face_encodings(
                face_image)[0]  # 获取每个人脸图片的encoding
            face_tag = os.path.splitext(image)[0]  # 获取每个图片对应的用户的名字和学号
            face_encodings.append(face_encoding)
            face_tags.append(face_tag)
        return face_encodings, face_tags
    else:
        print("请输入一个有效的模板目录！")
        exit(-1)


def detect_frame(frame, known_face_encodings, known_face_names, known_face_numbers, tolerance=0.6, model="hog"):
    """
    从一张图片中检测人脸，返回人脸的边框信息和人脸的名字和编号
    """
    face_locations = face_recognition.face_locations(frame, model=model)
    face_encodings = face_recognition.face_encodings(frame, face_locations)
    face_names = []
    face_numbers = []
    for face_encoding in face_encodings:
        # See if the face is a match for the known face(s)
        matches = face_recognition.compare_faces(
            known_face_encodings, face_encoding)
        name = "Unknown"

        # # If a match was found in known_face_encodings, just use the first one.
        # if True in matches:
        #     first_match_index = matches.index(True)
        #     name = known_face_names[first_match_index]
        # Or instead, use the known face with the smallest distance to the new face
        face_distances = face_recognition.face_distance(
            known_face_encodings, face_encoding)
        result = list(face_distances <= tolerance)
        if True not in result:
            face_names.append(name)
            face_numbers.append("无")
            continue
        best_match_index = np.argmin(face_distances)
        if matches[best_match_index]:
            name = known_face_names[best_match_index]
            number = known_face_numbers[best_match_index]
        face_names.append(name)
        face_numbers.append(number)
    return face_locations, face_names, face_numbers
