# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/6/29 16:35
@Author ： mewhaku
@File ：rock_paper_scissors.py
@IDE ：PyCharm
"""
import random
user_01 = ["石头","剪刀","布"]
user_02 = ["石头","剪刀","布"]
#battle
#石头 = 0 剪刀 = 1 布 = 2
user01_mov = random.randint(0,len(user_01)-1)
user02_mov = random.randint(0,len(user_02)-1)
print(f"玩家一出：{user_01[user01_mov]},玩家二出：{user_02[user02_mov]}")
#judge
if user01_mov == user02_mov:
    print("平局")
elif user01_mov == 0 and user02_mov == 1:
    print("玩家一获胜")
elif user01_mov == 1 and user02_mov == 2:
    print("玩家一获胜")
elif user01_mov == 2 and user02_mov == 0:
    print("玩家一获胜")
else:
    print("玩家二获胜")