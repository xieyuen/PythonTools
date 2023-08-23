# -*- coding: utf-8 -*-

# Python Learning File

"""
# 爬虫--爬取网页源代码

# 导入请求模块
# import requests

# 网址
url = 'https://xieyuen.github.io/blog.github.io'

got_url = requests.get( url )
# 请求响应码
# 1xx -- 等待响应
# 2xx -- 正常
# 3xx -- 重定向
# 4xx -- 客户端出错 -> 404
# 5xx -- 服务器出错

print( got_url )

Source_Code = requests.get( url ).text

print( Source_Code )

# import requests
# import os


# https://pic3.zhimg.com/v2-4de16ff3e1185b26e0a808f0af49ad72_r.jpg
url="http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
root="D://pics//"
path=root+url.split('/')[-1]
try:
    if not os.path.exists(root): os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else: print("文件爬取关败")
except: print("爬取失败")
"""

from os import system as cmd

cmd('echo awa')
