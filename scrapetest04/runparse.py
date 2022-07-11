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
#网址信息
url = "https://tieba.baidu.com/f?kw=%E5%8E%9F%E7%A5%9E%E5%86%85%E9%AC%BC"
li_path = '//*[@id="thread_list"]'
img_path = "//@bpic"
tieba_name = "原神内鬼"
#本地解析
for i in range(10):
    tiebapachong = pachong.Scrape(tieba_name, i*50)
    mytext = tiebapachong.get_data()
    mytext = mytext.replace('style="display:none;"><!--\n', 'style="display:none;">')
    fileutil.save_text(f"{tieba_name}{i}.html", mytext)
    print(f"正在保存{tieba_name}{i}.html")
    mytext = fileutil.read_text(f"{tieba_name}{i}.html")
    fileutil.creat_dir(f"{tieba_name}{i}图片")
    ul_all_imgs = tiebapachong.parse_page(mytext, li_path, img_path)
    for index,img in enumerate(ul_all_imgs):
        print(f"{tieba_name}{i}.html共有{len(ul_all_imgs)}图片，这是第{index+1}张图片的url：{img}")
        imgdata = tiebapachong.get_byte(img)
        fileutil.save_img(f"{tieba_name}{i}图片/图片{index+1}.jpg", imgdata)
