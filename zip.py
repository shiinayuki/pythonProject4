# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/30 11:29
@Author ： mewhaku
@File ：zip.py
@IDE ：PyCharm
"""
list01 = ["张三","李四"]
list02 = ["班长","学习委员"]
list03 = list(zip(list01,list02))
print(list03)
for name,position in list03:
    print(position + ":" + name)


for i in list01:
    print(i)


for i in range(0,len(list01)):
    print(list01[i])

for i,j in enumerate(list01):
    print(str(i) + ":" + j )