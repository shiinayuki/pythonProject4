# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/5 14:30
@Author ： mewhaku
@File ：runmain.py
@IDE ：PyCharm
"""
import scripeclass
import fileclass

pachong = scripeclass.baidu_tieba()
page_html = pachong.get_data()
fileclass.save_file("笔记本贴吧首页.html",page_html)