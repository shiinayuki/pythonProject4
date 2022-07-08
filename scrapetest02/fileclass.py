# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/5 14:28
@Author ： mewhaku
@File ：fileclass.py
@IDE ：PyCharm
"""
def save_file(file_name,file_data):
    with open(file_name,"w",encoding = "utf-8") as f:
        f.write(file_data)