# xieyuen 的 python 程序整合包
# -*- coding: utf-8 -*-

import requests
import jsonpath
import os

class Crawler():
    
    def __init__(self, _crawler):
        self._crawler = _crawler

    def music():
        """
        音乐爬虫awa
        """

        """
        1.url
        2.模拟浏览器请求
        3.解析网页源代码
        4.保存数据
        """

        def get_music_platfrom():
            print("1.网易云:netease\n2.QQ:qq\n3.酷狗:kugou\n4.酷我:kuwo\n5.百度:baidu\n6.喜马拉雅:ximalaya")
            platfrom = input("输入音乐平台类型:")
            inverted = invert_platfrom(platfrom)
            return inverted

        def invert_platfrom(platfrom):
            """
            # 原来写的破烂检测
            if platfrom == 'n': platfrom = 'netease'
            if platfrom == 'kg': platfrom = 'kugou'
            if platfrom == 'kw': platfrom = 'kuwo'
            if platfrom == 'xi': platfrom = 'ximalaya'
            if platfrom == 'b': platfrom = 'baidu'
            """
            match platfrom:
                case 'netease'|'qq'|'kugou'|'kuwo'|'xiamlaya'|'baidu':
                    return platfrom
                case 'n'|'net':
                    return 'netease'
                case 'kg':
                    return 'kugou'
                case 'kw':
                    return 'kuwo'
                case 'x'|'xi':
                    return 'ximalaya'
                case 'bd':
                    return 'baidu'
                case _:
                    print(f"【ERROR】\n无法识别到你输入的 { platfrom } 平台，请重新输入.")
                    get_music_platfrom()

        def download_music(url, title, author):
            # 创建文件夹(如果不存在的话)
            if not os.path.exists('.\\music\\'): os.makedirs("music",exist_ok=True)
            path = '.\\music\\{}.mp3'.format(title)
            print('歌曲:{0}-{1},正在下载...'.format(title,author))
            # 下载（这种读写文件的下载方式适合少量文件的下载）
            content = requests.get(url).content
            with open(file = '.\\music\\' + title + ' ' + author + '.mp3',mode='wb') as f:
                f.write(content)
            print('下载完毕,{0}-{1},请试听'.format(title,author))
            return True

        # main program
        """
        搜索歌曲名称
        :return:
        """
        name = input("请输入歌曲名称:")
        platfrom = get_music_platfrom() # 搜索的平台
        print("-------------------------------------------------------")

        url = 'https://music.liuzhijin.cn/'
        headers = {
            "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
            # 判断请求是异步还是同步
            "x-requested-with":"XMLHttpRequest",
        }
        param = {
            "input":name,
            "filter":"name",
            "type": platfrom,
            "page": 1,
        }
        res = requests.post(url=url,data=param,headers=headers)
        json_text = res.json()

        title = jsonpath.jsonpath(json_text,'$..title')
        author = jsonpath.jsonpath(json_text,'$..author')
        url = jsonpath.jsonpath(json_text, '$..url')
        if title:
            songs = list(zip(title,author,url))
            for s in songs:
                print(s[0],s[1],s[2])
            print("-------------------------------------------------------")
            index = int(input("请输入您想下载的歌曲版本:"))
            download_music(url[index],title[index],author[index])
        else:
            print("对不起，暂无搜索结果!")
            return False
            
    def picture():

        """
        图片爬虫awa

        想要下载多个可以这样：

            for _ in {图片url}:
                while True:
                    xieyuen.crawler_picture.main_program(_, {保存路径})

        """

        def get_root():
            _root = input('请输入存储路径：')
            return _root
        
        def get_url():
            _url = input('请输入图片URL')
            return _url

        _root = get_root()
        _url = get_url()

        _path = _root + _url.split('/')[-1]
        
        try:
            if not os.path.exists(_root):
                os.mkdir(root)
            if not os.path.exists(_path):
                _req_result = requests.get(url)
                with open(path, 'wb')as f:
                    f.write(_req_result.content)
                    f.close()
                    print('图片已保存')
                    return True
            else:
                print('文件爬取失败')
                return False
        except:
            print('爬取失败')
            return False
