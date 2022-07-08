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
url = "https://baijiahao.baidu.com/s?id=1737670505078160135&wfr=spider&for=pc"
page_xpath = '//*[@id="ssr-content"]/div[2]/div/div[1]/div[2]/div[1]/div[3]/div/img'
img_xpath = "./@src"
#在线解析
tiebapachong = pachong.Scrape(url)
mytext = tiebapachong.get_data()
mytext = mytext.replace("<!--","")
imgurl = tiebapachong.parse_page(mytext, page_xpath, img_xpath)
imgdata = tiebapachong.get_byte(imgurl)
fileutil.save_text("html.html",mytext)
fileutil.save_img("直接保存图片图片.jpg",imgdata)