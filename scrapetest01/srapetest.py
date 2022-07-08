# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/5 11:19
@Author ： mewhaku
@File ：srapetest.py
@IDE ：PyCharm
"""

import requests

html = requests.get("http://shiiina.top")

print(html.text)
with open("笔记本贴吧首页.html","w", encoding = "utf-8") as f:
    f.write(html.text)