# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/12 11:49
@Author ： mewhaku
@File ：runmain.py
@IDE ：PyCharm
"""
"""
壁纸种类
wallpaper_type：

电脑壁纸 = "dnbz"
手机壁纸 = "sjbz"
4K壁纸 = "4kbz"

细分种类
detail_type:

动漫原画 = "?q=--82--.html"
卡通动漫 = "?q=--81--.html"
航天飞机 = "?q=--80--.html"
自然风景 = "?q=--79--.html"
花卉植物 = "?q=--78--.html"
绘画创意 = "?q=--77--.html"
动物萌宠 = "?q=--76--.html"
家居陈设 = "?q=--75--.html"
静物特写 = "?q=--74--.html"
肌理纹理 = "?q=--89--.html"
军事科技 = "?q=--72--.html"
明星大咖 = "?q=--71--.html"
太空科幻 = "?q=--70--.html"
禅意古风 = "?q=--69--.html"
体育运动 = "?q=--85--.html"
美女写真 = "?q=--65--.html"
人文风土 = "?q=--87--.html"
美食甜品 = "?q=--88--.html"
城市建筑 = "?q=--83--.html"
汽车船舶 = "?q=--84--.html"
影视剧照 = "?q=--90--.html"
情感文艺 = "?q=--91--.html"

页面 
page = "i"

"""
import fileutil
import webcrawler

wallpaper_type = ["none", "dnbz", "sjbz", "4kbz"]

zh_wt = ["none", "电脑壁纸", "手机壁纸", "4k壁纸"]

detail_type = ["?q=----.html", "?q=--82--.html", "?q=--81--.html", "?q=--80--.html", "?q=--79--.html",
               "?q=--78--.html", "?q=--77--.html", "?q=--76--.html", "?q=--75--.html",
               "?q=--74--.html", "?q=--89--.html", "?q=--72--.html", "?q=--71--.html",
               "?q=--70--.html", "?q=--69--.html", "?q=--85--.html", "?q=--65--.html",
               "?q=--87--.html", "?q=--88--.html", "?q=--83--.html", "?q=--84--.html",
               "?q=--90--.html", "?q=--91--.html"]

zh_dt = ["全部", "游戏原画", "卡通动漫", "飞机航天", "自然风景", "花卉植物",
         "绘画创意", "动物萌宠", "家居陈设", "静物特写", "肌理纹理",
         "军事科技", "明星大咖", "太空科幻", "禅意古风",
         "体育运动", "美女写真", "人文风土", "美食甜品",
         "城市建筑", "汽车船舶", "影视剧照", "情感文艺"
         ]

pa = webcrawler.Scrape.variate(1, 1, 10)
choose_detail = pa(choose)
img_count = 1

# html定位信息
li_path = '//*[@class="clearfix pic-list gallery"]'
img_path = "//@data-original"

# 得到未处理html
dt = detail_type[int(choose_detail_type)]
wt = wallpaper_type[int(choose_wallpaper_type)]
fileutil.creat_dir(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}未处理html")
count = 0
for i in range(92):
    wp_crawler = webcrawler.Scrape(wt, dt, i+1)
    mytext = wp_crawler.get_data()
    fileutil.save_text(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}未处理html/第{i+1}页.html", mytext)
    if wp_crawler.file_check(f"{zh_wt[int(choose_wallpaper_type)]}", f"{zh_dt[int(choose_detail_type)]}",i+1) == True:
        break
    else:
        print(f"正在保存第{i + 1}页.html")
        count = count + 1
        continue
print(count)
#得到已处理html
fileutil.creat_dir(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}已处理html")
for i in range(0, count):
    mytext = fileutil.read_text(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}未处理html/第{i+1}页.html")
    mytext = mytext.replace('style="display:none;"><!--\n', 'style="display:none;">')
    ul_all = wp_crawler.parse_index_page(mytext, li_path)
    ul_text = ul_all.decode("utf-8").replace("\n", "")
    fileutil.save_text(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}已处理html/第{i+1}页.html", ul_text)
    print(f"已处理{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}第{i+1}页.html")

"""
#得到详情页html
fileutil.creat_dir(f"{tieba_name}贴吧详情页")
for i in range(2):
    mytext = fileutil.read_text(f"{tieba_name}贴吧已处理html/{tieba_name}{i}.html")
    ul_all_url = wp_crawler.parse_index_url(mytext, page_xpath)
    fileutil.creat_dir(f"{tieba_name}贴吧详情页/详情{i}页")
    for index, url in ul_all_url:
        try:
            time.sleep(0.1)
            print(f"详情{i}页,详情页后缀为{url}")
            mytext = webcrawler.Scrape(url=f"https://tieba.baidu.com/{url}")
            mytext =wp_crawler.get_data()
            url = url[-10:]
            fileutil.save_text(f"{tieba_name}贴吧详情页/详情{i}页/详情{index}.html", mytext)
        except:
            print(f"爬取{url}爬取失败，正在跳过")
"""
#爬取图片
for i in range(0, count):
    mytext = fileutil.read_text(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}已处理html/第{i+1}页.html")
    fileutil.creat_dir(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}爬取图片/第{i+1}页")
    ul_all_imgs = wp_crawler.parse_page(mytext, li_path, img_path)
    for index, img in enumerate(ul_all_imgs):
        if int(img_total) >= int(img_count):
            img_count = img_count + 1
            print(f"第{i+1}页共有{len(ul_all_imgs)}图片，这是第{index+1}张图片的url：https://www.toopic.cn{img}")
            imgdata = wp_crawler.get_byte(img)
            fileutil.save_img(f"{zh_wt[int(choose_wallpaper_type)]}{zh_dt[int(choose_detail_type)]}爬取图片/第{i+1}页/图片{index+1}.jpg", imgdata)
        else:
            break
#开启文件夹
open = wp_crawler.open_file()