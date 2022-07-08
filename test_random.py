# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/29 16:25
@Author ： mewhaku
@File ：test_random.py
@IDE ：PyCharm
"""
import random

student_name = ["张三0", "李四0", "王五0", "赵六0", "张三1", "李四1", "王五1", "赵六1"]

name = random.randint(0, len(student_name)-1)

print(student_name[name])

