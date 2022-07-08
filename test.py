# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/29 10:16
@Author ： mewhaku
@File ：test.py
@IDE ：PyCharm
"""
print("hello,world")
student_name = "{}张三,{}23"
str = student_name.format("姓名：","年龄：")
print(str)

name = "李四"
password = "123"
str = f"hello{name} world{password}"
print(str)

student_score = input("请输入你的分数：")
student_score = int(student_score)
if student_score == 100:
    print("爸爸给买辆车")
elif student_score >= 90:
    print("妈妈给买MP4")
elif student_score >= 60:
    print("妈妈买本参考书")
else:
    print("考这么差什么都不买！")

count = 1
while count < 5:
    print(count)
    count = count +1