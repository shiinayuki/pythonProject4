# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/30 10:07
@Author ： mewhaku
@File ：pop.py
@IDE ：PyCharm
"""
import random
student_name = ["张三0","李四0","王五0","赵六0","张三1","李四1","王五1","赵六1"]
for i in range(3):
    choose_student = random.randint(0,len(student_name)-1)
    student = student_name.pop(choose_student)
    print(student)
    print(student_name)