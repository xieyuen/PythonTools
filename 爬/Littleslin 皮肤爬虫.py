# Littleslin 皮肤爬虫

import os
import re
import time
import json
from my_logger import logger

import requests
from rich.progress import track


class SkinCrawler:
    def __init__(self):
        self.url = 'https://littleskin.cn/skinlib/data?filter=skin&uploader=0&sort=likes&'
        self.url_keyword = 'keyword='
        self.url_page = 'page='
        self.path: str|None = None
        self.page: int|None = None
    def __call__(
        self, *,
        path:    str|None = None,
        page:    int|None = None,
        keyword: str|None = None,
    ): return self.main(path=path, page=page, keyword=keyword)

    def main(
        self, *,
        path:    str|None = None,
        page:    int|None = None,
        keyword: str|None = None,
    ):
        self.path = path
        self.page = page

        logger.info('Littleskin 皮肤爬虫')
        while self.path is None:
            self.path = input('请在下面输入皮肤图片存储路径\n若空，则为默认值 "./skin/"\n')
            if self.path == '':
                self.path = './skin/'
                if not os.path.exists(self.path):
                    os.makedirs(self.path)
                break
            elif not os.path.exists(self.path):
                logger.error('路径不存在或者输入的路径不合法')
                continue
            self.path = path
            break
        while self.page is None:
            self.page = input('请输入下载的页数\n若空，则只下载首页皮肤\n')
            if self.page == '':
                self.page = 1
                break
            elif not self.page.isdigit():
                logger.error('请输入阿拉伯数字')
                continue

            try: self.page = int(self.page)
            except ValueError:
                logger.error('你家页码是小数')
                continue
            if self.page < 1:
                logger.error('你家页码小于1')
                continue
            break
            
        
        __url = self.url
        if keyword is not None:
            __url += self.url_keyword + keyword + '&'
        
        logger.info('请等待下载完成...')
        for i in track(range(1, self.page + 1)):
            pics_url = __url + self.url_page + str(i)
            response = requests.get(pics_url).json()
            breakpoint()
            ids = re.findall("'tid': (.*?),",str(response))

            for id in ids:
                download_url = 'https://littleskin.cn/preview/' + id + '.png'
                name = download_url.strip('https://littleskin.cn/preview/')
                pic = requests.get(download_url).content
                try:
                    with open(self.path + f'/{name}', 'wb') as f:
                        f.write(pic)
                except:
                    logger.error(f'图片 {name} 下载失败')
        
        logger.info('下载任务已完成')

if __name__ == '__main__':
    sc = SkinCrawler()
    sc(path='./skin/', keyword=input('keyword='))
