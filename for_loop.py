# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/29 15:27
@Author ： mewhaku
@File ：for_loop.py
@IDE ：PyCharm
"""
count = ["张三0","李四0","王五0","赵六0","张三1","李四1","王五1","赵六1"]
for item in count:
    print(item)



count = ["张三0","李四0","王五0","赵六0","张三1","李四1","王五1","赵六1"]
index = 0
while index < 7:
    print(count[index])
    index =index + 1


count = ["张三0","李四0","王五0","赵六0","张三1","李四1","王五1","赵六1"]
for index in range (0,8):
    if index%2 == 1:
        continue
    print (count[index])

