# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/29 16:29
@Author ： mewhaku
@File ：guess_number.py
@IDE ：PyCharm
"""
import random
max = int(input("请输入随机范围（上限）"))
min = int(input("请输入随机范围（下限）"))
finish_number = random.randint(min,max)
guess_number = 0
while True:
    guess_number = guess_number + 1
    user_number = int(input("请输入数字："))
    if user_number > finish_number:
        print("你输入的数字大了")
    elif user_number <finish_number:
        print("你输入的数字小了")
    else:
        print("猜对了")
        break
print(f"一共猜测了{guess_number}次")
