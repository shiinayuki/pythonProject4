# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/30 10:41
@Author ： mewhaku
@File ：35_choose_7.py
@IDE ：PyCharm
"""
import random
MAX_NUM = 35
CHOOSE_NUMBER = 7
#35 number list
list = []
#Selected number list
choose_number_list = []
#create MAX_NUM list
for i in range(MAX_NUM):
    number = random.randint(0,100)
    list.append(number)
print(f"35个随机数数列：{list}")
#choose
for i in range(CHOOSE_NUMBER):
    select_number = random.randint(0, CHOOSE_NUMBER - 1)
    choose_number_list.append(list.pop(select_number))
print(f"7个被选择数列：{choose_number_list}")