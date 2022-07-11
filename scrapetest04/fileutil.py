# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/7 12:06
@Author ： mewhaku
@File ：fileutil.py
@IDE ：PyCharm
"""
import os
def save_text(filename,data):
    with open(filename,'w',encoding='utf-8') as f:
        f.write(data)

def read_text(filename):
    with open(filename,'r',encoding='utf-8') as f:
        return f.read()

def save_img(imgname,data):
    with open(imgname,'wb') as f:
        f.write(data)

def creat_dir(path):
    os.makedirs(path)