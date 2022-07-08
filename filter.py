# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/4 11:33
@Author ： mewhaku
@File ：filter.py
@IDE ：PyCharm
"""
import random

x = [random.randint(1, 100) for x in range(10)]
print(x)

# 使用filter找出其中能把7整除的数
def divide(x):
    if x % 7 == 0:
        return x

print(list(filter(divide, x)))

print(list(filter(lambda x: x % 7 == 0, [random.randint(1, 100) for i in range(10)])))
