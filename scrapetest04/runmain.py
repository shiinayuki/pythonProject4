# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/7 11:46
@Author ： mewhaku
@File ：runmain.py
@IDE ：PyCharm
"""
import pachong
import fileutil
#网页数据
url = "https://tieba.baidu.com/f?kw=%E5%8E%9F%E7%A5%9E%E5%86%85%E9%AC%BC"
page_xpath = '//*[@id="thread_list"]'
img_xpath = "./@src"
#在线解析
for i in range(10):
    tiebapachong = pachong.Scrape(url,i*50)
    mytext = tiebapachong.get_data()
    mytext = mytext.replace('style="display:none;"><!--\n', 'style="display:none;">')
    #imgurl = tiebapachong.parse_page(mytext)
    #imgdata = tiebapachong.get_byte(imgurl)
    fileutil.save_text("html.html",mytext)
    #fileutil.save_img("直接保存图片图片.jpg",imgdata)