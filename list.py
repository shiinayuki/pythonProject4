# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/30 14:47
@Author ： mewhaku
@File ：list.py
@IDE ：PyCharm
"""
list = [i for i in range(100)]
print(list)

vec = [[1,2,3],[4,5,6],[7,8,9]]
vec01 = [num for elem in vec for num in elem]
print(vec01)

list01 = [1,3,4,5,6,7,8,9]
list02 = [i for i in list01 if i > 5]
print(list02)
                                                    