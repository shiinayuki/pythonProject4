# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/30 11:50
@Author ： mewhaku
@File ：find_second_big_index.py
@IDE ：PyCharm
"""
list01 = [2, 45, 7, 5, 8, 9, 3, 7, 9]
list01.sort()
number = list01[len(list01)-2]
print(f"排列后{list01}")
print("第二大数字",list01[len(list01)-2])
times = 0
meet = 0
for i,j in enumerate(list01):
    if j != list01[len(list01)-2]:
        times += 1
    else:
        meet += 1
        print(f"第{meet}次遇到第二大数字{list01[len(list01)-2]}下标为{times + 1}")
        times += 1

