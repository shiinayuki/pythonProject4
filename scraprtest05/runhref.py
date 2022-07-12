# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/11 11:19
@Author ： mewhaku
@File ：runhref.py
@IDE ：PyCharm
"""
import pachong
import fileutil
import time
li_path = '//*[@id="thread_list"]'
img_path = "//@bpic"
tieba_name = "原神内鬼"
page_xpath = '//a[@class="j_th_tit "]/@href'



tiebapachong = pachong.Scrape(tieba_name, 0)
#得到未处理html
fileutil.creat_dir(f"{tieba_name}贴吧未处理html")
for i in range(2):
    tiebapachong = pachong.Scrape(tieba_name, i * 50)
    mytext = tiebapachong.get_data()
    fileutil.save_text(f"{tieba_name}贴吧未处理html/{tieba_name}{i}.html", mytext)
    print(f"正在保存{tieba_name}{i}.html")

#得到已处理html
fileutil.creat_dir(f"{tieba_name}贴吧已处理html")
for i in range(2):
    mytext = fileutil.read_text(f"{tieba_name}贴吧未处理html/{tieba_name}{i}.html")
    mytext = mytext.replace('style="display:none;"><!--\n', 'style="display:none;">')
    ul_all = tiebapachong.parse_index_page(mytext, li_path)
    ul_text = ul_all.decode("utf-8").replace("\n", "")
    fileutil.save_text(f"{tieba_name}贴吧已处理html/{tieba_name}{i}.html", ul_text)
    print(f"已处理{tieba_name}{i}.html")

#得到详情页html
fileutil.creat_dir(f"{tieba_name}贴吧详情页")
for i in range(2):
    mytext = fileutil.read_text(f"{tieba_name}贴吧已处理html/{tieba_name}{i}.html")
    ul_all_url = tiebapachong.parse_index_url(mytext, page_xpath)
    fileutil.creat_dir(f"{tieba_name}贴吧详情页/详情{i}页")
    for index, url in ul_all_url:
        try:
            time.sleep(0.1)
            print(f"详情{i}页,详情页后缀为{url}")
            mytext = pachong.Scrape(url=f"https://tieba.baidu.com/{url}")
            mytext =tiebapachong.get_data()
            url = url[-10:]
            fileutil.save_text(f"{tieba_name}贴吧详情页/详情{i}页/详情{index}.html", mytext)
        except:
            print(f"爬取{url}爬取失败，正在跳过")

#爬取详情页图片
for i in range(10):
    for index in ul_all_url:
        mytext = fileutil.read_text(f"{tieba_name}贴吧详情页/详情{i}页/详情{index}.html")
        fileutil.creat_dir(f"{tieba_name}贴吧详情页/详情{i}页/详情{index}/详情图片")
        ul_all_imgs = tiebapachong.parse_page(mytext, li_path, img_path)
        for j, img in enumerate(ul_all_imgs):
                print(f"详情{index}.html共有{len(ul_all_imgs)}图片，这是第{j}张图片的url：{img}")
                imgdata = tiebapachong.get_byte(img)
                fileutil.save_img(f"{tieba_name}贴吧详情页/详情{i}页/详情{index}/详情图片/图片{j}.jpg", imgdata)
