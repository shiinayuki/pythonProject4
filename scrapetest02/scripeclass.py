# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/5 14:26
@Author ： mewhaku
@File ：scripeclass.py
@IDE ：PyCharm
"""
import requests
class baidu_tieba:
    def __init__(self):
        self.url = "http://shiiina.top"

    def get_data(self):
        response = requests.get(self.url)
        return response.text