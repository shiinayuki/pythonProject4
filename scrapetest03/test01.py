# -*- coding: utf-8 -*-
"""
@Copyright (C) 2022 mewhaku . All Rights Reserved 
@Time ： 2022/7/7 9:48
@Author ： mewhaku
@File ：test01.py
@IDE ：PyCharm
"""
import requests
from lxml import etree
my_url = "https://baijiahao.baidu.com/s?id=1737537095447995112"
#添加UserAgent,使服务器不识别我们是爬虫
my_header = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.66 Safari/537.36 Edg/103.0.1264.44"}
#发送http请求，得到服务器响应
response = requests.get(my_url, headers=my_header)
#获取服务武器相应的html代码
mytext = response.text
#print(mytext)
#利用etree.HTML，将html字符串转化为Element对象
mytext = etree.HTML(mytext)
#xpath的使用方法，得到某个特定的节点或者包括某个特定值的节点
#注意 得到的是list，其中每个元素是Element
#//*[@id="fm7910529760"]/li[1]/a/img
mytext = mytext.xpath('//*[@id="ssr-content"]/div[2]/div/div[1]/div[2]/div[1]/div[12]/div/img')
#print(mytext)
#得到的element对象，使用text()可以得到标签包含的文字
mytext = mytext[0].xpath("./@src")
#使用etree.tostring(html)将element对象转换成html对象
#mytext = etree.tostring(mytext[0])
print(f"图片的url是：{mytext[0]}")
#将图片保存为本地文件
img_data = requests.get(mytext[0],headers=my_header).content
with open("图片1.jpg","wb") as f:
    f.write(img_data)
