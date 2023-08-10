import requests
import re
import time
import json
from my_logger import logger



download_sucess = True
time.sleep(1.5)

pictures = input('你想下载多少张皮肤：')
while pictures.isdigit() == False:
    logger.warning("请输入数字！")
    pictures = input('你想下载多少张皮肤：')

Path = input('请输入保存的路径：')
print("请稍等......")
pictures = int(pictures)

for i in range(1,pictures+1):
    url = 'https://littleskin.cn/skinlib/data?' \
        'filter=skin&uploader=0&sort=likes&keyword=军&page=' + str(i)
    response = requests.get(url).json()
    ids = re.findall("'tid': (.*?),",str(response))
    for id in ids:
        picture_url = 'https://littleskin.cn/preview/' + id + '.png'
        picture_name = picture_url.strip('https://littleskin.cn/preview/')
        picture = requests.get(picture_url).content
        try:
            with open(Path + '//%s'%picture_name,'wb') as file:
                file.write(picture)
        except FileNotFoundError:
            download_sucess = False
            print('路径不存在！')
            break

if download_sucess == False:
    print("下载失败！")
elif download_sucess == True:
    print('下载完成！')