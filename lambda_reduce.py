# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/4 11:06
@Author ： mewhaku
@File ：lambda_reduce.py
@IDE ：PyCharm
"""
from functools import reduce
def myfun(x,y):
    return x*y
mylist = [x for x in range(1,11)]

y = reduce(myfun,mylist)
print(y)
#1到100的累加和
z = reduce(lambda x,y: x+y, [x for x in range(1,101)])
print(z)