# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/8 9:31
@Author ： mewhaku
@File ：runparse.py
@IDE ：PyCharm
"""
import pachong
import fileutil
import runmain
#本地解析
tiebapachong = pachong.Scrape(runmain.url)
mytext = fileutil.read_text("html.html")
imgurl = tiebapachong.parse_page(mytext,runmain.page_xpath,runmain.img_xpath)
imgdata = tiebapachong.get_byte(imgurl)
fileutil.save_img("读html保存图片.jpg", imgdata)
