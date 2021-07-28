#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Mon Jul 27 06:10:33 2021

@author: Robinson Montes
"""


def top_students(mongo_collection):
    """
    students sorted by average score
    :param mongo_collection:
    :return:
    """
    students = mongo_collection.find()
    students_list = []
    for student in students:
        topics = student["topics"]

        score = 0
        for topic in topics:
            score += topic["score"]
        score /= len(topics)
        student["averageScore"] = score
        students_list.append(student)

    return sorted(students_list, key=lambda i: i["averageScore"], reverse=True)
