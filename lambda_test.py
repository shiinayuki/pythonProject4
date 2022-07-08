# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/4 10:32
@Author ： mewhaku
@File ：lambda_test.py
@IDE ：PyCharm
"""
myla = lambda x: x * x
i = [x for x in range(1, 11)]
print(i)

y = list(map(myla, i))
print(y)

# 一行完成
print(list(map(lambda x: x * x, [x for x in range(1, 11)])))
