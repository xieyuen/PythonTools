# 爬点图片

import requests
import os


url="https://pic4.zhimg.com/v2-ca6f0a47c42c6072bf8a13291185ef5f_r.jpg"
# "http://image.nationalgeographic.com.cn/2017/0211/20170211061910157.jpg"
# https://pic3.zhimg.com/v2-4de16ff3e1185b26e0a808f0af49ad72_r.jpg
# https://pic4.zhimg.com/v2-ca6f0a47c42c6072bf8a13291185ef5f_r.jpg


root=".\\img\\"

path=root+url.split('/')[-1]
try:
    if not os.path.exists(root):
        os.mkdir(root)
    if not os.path.exists(path):
        r=requests.get(url)
        with open(path,'wb')as f:
            f.write(r.content)
            f.close()
            print("文件保存成功")
    else: print("文件爬取关败")
except: print("爬取失败")
