# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/7 11:35
@Author ： mewhaku
@File ：pachong.py
@IDE ：PyCharm
"""
import requests
from lxml import etree


class Scrape():
    # 初始化
    def __init__(self, url):
        self.url = url
        self.headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"
        }

    # 发送url，得到页面数据
    def get_data(self):
        response = requests.get(self.url, headers=self.headers)
        return response.text

    # 对页面数据进行解析
    def parse_page(self, data, page_xpath, img_xpath):
        mytext = etree.HTML(data)
        mytext = mytext.xpath(page_xpath)
        print(mytext)
        mytext = mytext[0].xpath(img_xpath)
        print(f"图片的url是：{mytext[0]}")
        return mytext[0]

    def get_byte(self, img_data):
        response = requests.get(img_data, headers=self.headers)
        return response.content