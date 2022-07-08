# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/5 10:32
@Author ： mewhaku
@File ：myfun.py
@IDE ：PyCharm
"""
class Person:
    def __init__(self,na):
        self.name = na
    def eat(self):
        print(f"{self.name}吃饭")