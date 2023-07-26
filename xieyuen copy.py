# xieyuen 的 python 程序整合包
# -*- coding: utf-8 -*-

import requests
import jsonpath
import os
import fnmatch
import time
import io
import webbrowser
import win32api
import win32con
import math
import threading


class Information:

    '''
        这个 python 文件的信息
    '''

    __license = 'MIT License\n\nCopyright (c) 2023 HIM049\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.'

    def __init__(self, _info): # 初始化，没得说
        self._info = _info
        self.help = self.Help()


    # LICENSE 开源协议
    def LICENSE(self):
        print(self.__license)

    def license(self):
        self.LICENSE()


    def author(self):
        print('Copyright from xieyuen')


    def help(self):
        Help.information()


    def copyright_info(self):
        self.author()
        print('LICENSE：\n')
        self.LICENSE()


class Help:

    def __init__(self, _help): # 初始化，没得说
        self._help = _help
        self.Crawler = self.Crawler()
        self.Tools = self.Tools()


    def printHelpMassage(self, _help_massage):
        print(_help_massage)


    def list(self):
        print('Help类中有以下函数/类：')
        for i in dir(Help):

            if fnmatch.fnmatch(i, '__*__'): continue

            if fnmatch.fnmatchcase(i, '[A-Z]*'):
                print('类:', end='')
            else:
                print('函数:', end='')
            print(f'{ i }()')


    class List:
        def __init__(self, _list):
            self.list = _list

        def Crawler():
            pass


    def information(self):
        print('这个python包的信息')


    def crawler(self):
        _help_massage = '一堆爬虫\n使用爬虫记得调用 main_program\n\n现有:\n    1. Music\n        - 音乐爬虫，支持网易云、QQ等平台\n   2. Picture\n        - 也许是最简单的图片爬虫了'
        Help.printHelpMassage(_help_massage)


    def help(self):
        _help_massage = '这是这个python包的帮助页面'
        Help.printHelpMassage(_help_massage)



    class Crawler:

        def __init__(self, _crawler): # 初始化，没得说
            self._crawler = _crawler


        def main_program(self):
            _help_massage = '爬虫的主程序，要使用的话请调用它'
            Help.printHelpMassage(_help_massage)


        def music(self):
            _help_massage = '音乐爬虫awa\n使用爬虫请调用`Crawler.Music.main_program()`这个函数awa\n\n支持:\n    1. 网易云\n    2.QQ\n    3.酷狗\n    4.酷我:kuwo\n    5.百度:baidu\n    6.喜马拉雅:ximalaya'
            Help.printHelpMassage(_help_massage)


        def picture(self):
            _help_massage = '图片爬虫awa\n使用爬虫请调用`Crawler.Picture.main_program()`这个函数awa'
            Help.printHelpMassage(_help_massage)


    def tools(self):
        _help_massage = '简单的小工具'
        self.printHelpMassage(_help_massage)


    class Tools:

        def __init__(self, _tools):
            self._tools = _tools


        def chinese_count(self):
            _help_massage = '计算汉字数量并记录汉字位置\n返回值像这样：\n\n[{"汉字数量": 11,"字母数量": 45,"非字母汉字数量": 14},[1, 9, 19, 81 ...]]\n后面的列表是汉字所在字符串的索引'
            Help.printHelpMassage(_help_massage)


class Crawler:

    '''
        一堆爬虫
        使用爬虫要记得调用 main_program

        现有:
            1. Music
                - 音乐爬虫，支持网易云、QQ等平台
            2. Picture
                - 也许是最简单的图片爬虫了
    '''

    def __init__(self, _crawler): # 初始化，没得说
        self._crawler = _crawler
        self.music = self.Music()
        self.picture = self.Picture()

    def help(self):
        Help.crawler()

    class Music:

        """
            音乐爬虫awa
            使用爬虫请调用`Crawler.Music.main_program()`这个函数awa

            支持：
                1.网易云:netease
                2.QQ:qq
                3.酷狗:kugou
                4.酷我:kuwo
                5.百度:baidu
                6.喜马拉雅:ximalaya
        """

        """
            编程思路：
                1.url
                2.模拟浏览器请求
                3.解析网页源代码
                4.保存数据
        """

        def __init__(self, _music): # 初始化，没得说
            self._music = _music


        def help(self):
            Help.Crawler.music()


        def get_music_platfrom(self):
            print("1.网易云:netease\n2.QQ:qq\n3.酷狗:kugou\n4.酷我:kuwo\n5.百度:baidu\n6.喜马拉雅:ximalaya")
            _platfrom = input("输入音乐平台类型:")
            _inverted = self.invert_platfrom(_platfrom)
            return _inverted


        def invert_platfrom(self, platfrom = 'n'):

            """
                检测并转换平台参数(大小写均可识别)
            """

            if not isinstance(platfrom, str): platfrom = str(platfrom)
            _platfrom = str.lower(platfrom) # 将所有的大写字母转化为小写

            match _platfrom:

                # 网易云 netease
                case '1'|'n'|'net'|'wy'|'wyy'|'wangyi'|'wangyiyun'|'netease'|'网易'|'网易云'|'网易云音乐':
                    return 'netease'

                # QQ qq
                case '2'|'q'|'qq'|'qqmusic'|'qqyinyue'|'qq音乐'|'qq 音乐':
                    return 'qq'

                # 酷狗 kugou
                case '3'|'kg'|'ku'|'kou'|'gou'|'kugou'|'酷狗':
                    return 'kugou'

                # 酷我 kuwo
                case '4'|'kw'|'ko'|'wo'|'kuwo'|'酷我':
                    return 'kuwo'

                # 百度 baidu
                case '5'|'b'|'bd'|'bu'|'baidu'|'百度':
                    return 'baidu'

                # 喜马拉雅 ximalaya
                case '6'|'x'|'xi'|'xmly'|'xmla'|'ximalaya'|'喜马拉雅':
                    return 'ximalaya'

                # 无法识别
                case _:

                    print(f"【ERROR】\n无法识别到你输入的 '{ platfrom }' 平台")
                    __check = int(input('请选择操作：\n [1]重新输入参数\n [2]使用默认值'))
                    print("-------------------------------------------------------")
                    if __check == 1:
                        self.get_music_platfrom()
                    if __check == 2:
                        return 'netease'


        def download_music(self, url, title, author):

            # 创建文件夹(如果不存在的话)
            if not os.path.exists('.\\music\\'):
                os.makedirs("music",exist_ok=True)

            path = '.\\music\\{}.mp3'.format(title)

            print('歌曲:{0}-{1},正在下载...'.format(title,author))

            # 下载（这种读写文件的下载方式适合少量文件的下载）
            content = requests.get(url).content
            with open(file = '.\\music\\' + title + ' ' + author + '.mp3',mode='wb') as f:
                f.write(content)

            print('下载完毕,{0}-{1},请试听'.format(title,author))
            return True


        def main_program(name = None, platfrom = None):

            '''
                音乐爬虫主程序
            '''

            """
                搜索歌曲名称
                :return:
            """

            if name == None:
                name = input("请输入歌曲名称:")
            if platfrom == None:
                platfrom = self.get_music_platfrom() # 获取搜索的平台
            else:
                platfrom = self.invert_platfrom(platfrom)

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
                self.download_music(url[index],title[index],author[index])
            else:
                print("对不起，暂无搜索结果!")
                return False

    class Picture:

        """
            图片爬虫awa
            使用爬虫请调用`Crawler.Picture.main_program()`这个函数awa
        """


        def __init__(self, _picture): # 初始化，没得说
            self._picture = _picture


        def help(self):
            Help.Crawler.picture()


        def main_program(self, _url: str, _root: str):

            '''
                图片爬虫主程序
            '''

            _path = _root + _url.split('/')[-1]

            try:
                # 创建文件夹（如果 { _root } 不存在的话）
                if not os.path.exists(_root):
                    os.mkdir(_root)

                if not os.path.exists(_path):
                    _req = requests.get(_url)
                    with open(path, 'wb')as f:
                        f.write(_req.content)
                        f.close()
                        print('图片已保存')
                        return True
                else:
                    print('文件爬取失败')
                    return False
            except:
                print('爬取失败')
                return False


class Tools:

    """
        简单的小工具
    """


    def __init__(self, _tools): # 初始化，没得说
        self._tools = _tools
        self.list_sort = self.ListSort()
        self.sysCmd = self.SysCmd()
        self.math = self.Math()
        self.bPrint = BetterPrint()


    def help(self):
        Help.tools()


    def isExistChinese(self, string):

        '''
            检测字符串内是否存在汉字
        '''

        for char in string:
            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字
                return True

        return False


    def count(self, string = '加油华为，加油China'):

        '''
            计算字符数量并记录字符位置

            返回值说明：
            >>> Help.Tools.count()
            'count': 数量
            'index': 索引
            'chinese': 汉字
            'alpha': 字母
                'all': 全部字母
                'lowercase': 小写字母
                'uppercase': 大写字母
            ' ': 空格 space
            '_': 其他(相当于通配符)

            后面的列表是汉字所在字符串的索引

            返回值像这样：
            >>> count('加油华为 加油China')
            {
                'count': {
                    'chinese': 6,
                    'alpha': {
                        'all': 5,
                        'lowercase': 4,
                        'uppercase': 1,
                        '_': 0
                    },
                    ' ': 1,
                    '_': 0
                },
                'index': {
                    'chinese': [0, 1, 2, 3, 5, 6],
                    'alpha': {
                        'all': [7, 8, 9, 10, 11],
                        'lowercase': [8, 9, 10, 11],
                        'uppercase': [7]
                    },
                    ' ': [4]
                }
            }
            >>> count('加油华为，加油China')
            {
                'count': {
                    'chinese': 6,
                    'alpha': {
                        'all': 5,
                        'lowercase': 4,
                        'uppercase': 1,
                        '_': 0
                    },
                    ' ': 0,
                    '_': 1
                },
                'index': {
                    'chinese': [0, 1, 2, 3, 5, 6],
                    'alpha': {
                        'all': [7, 8, 9, 10, 11],
                        'lowercase': [8, 9, 10, 11],
                        'uppercase': [7]
                    },
                    '_': [4]
                }
            }
        '''

        __result = {
            'count': { # 数量
                'chinese': 0, # 汉字
                'alpha': { # 字母
                    'all': 0, # 全部
                    'lowercase': 0, # 小写
                    'uppercase': 0, # 大写
                    '_': 0 # 其他
                },
                ' ': 0, # 空格 space
                '_': 0 # 其他
            },
            'index': { # 索引，内容同上
                'chinese': [],
                'alpha': {
                    'all': [],
                    'lowercase': [],
                    'uppercase': [],
                    '_': []
                },
                ' ': [],
                '_': []
            }
        }

        print(f'检测的字符串："{ string }"')

        # 开始处理并计数
        for __index in range(len(string)):
            char = string[__index]

            if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字，在isalpha()方法之前判断

                __result['count']['chinese'] += 1
                __result['index']['chinese'].append(__index)

            elif char.isalpha():  # ！汉字也返回 true

                __result['count']['alpha']['all'] += 1
                __result['index']['alpha']['all'].append(__index)

                if char.islower(): # 小写字母

                    __result['count']['alpha']['lowercase'] += 1
                    __result['index']['alpha']['lowercase'].append(__index)

                elif char.isupper(): # 大写字母

                    __result['count']['alpha']['uppercase'] += 1
                    __result['index']['alpha']['uppercase'].append(__index)

                else:

                    __result['count']['alpha']['_'] += 1
                    __result['index']['alpha']['_'].append(__index)

            elif char == ' ': # 空格

                __result['count'][' '] += 1
                __result['index'][' '].append(__index)

            else: # 其他

                __result['count']['_'] += 1
                __result['index']['_'].append(__index)

        # 删除字典里值为 0 对应的索引
        for i in __result['count']:

            if isinstance(__result['count'][i], dict):

                for j in __result['count'][i]:
                    if __result['count'][i][j] == 0:
                        del __result['index'][i][j]
                        if j == 'all':
                            del __result['index'][i]
                            __result['count'][i] = 0
                            break
            else:
                if __result['count'][i] == 0:
                    del __result['index'][i]

        return __result


    def listDedup(self, _list): # List dedup

        '''
            给列表不打乱顺序地去重
        '''

        result = []
        for i in _list:

            if i not in result:
                result.append(i)

        return result


    class Math:

        def __init__(self, _math): # 初始化，没得说
            self._math = _math
            self.constant = self.Constant()


        def sum(self, _expressions, _start=0, _stop=10):

            '''
                sum(关于x的表达式(需要定义成函数), 起始值, 终值)

                起始值必须大于终值
                For example:
                1)
                >>> def f(x):
                ...     return 1/x
                ... sum(f, 1, 10)
                2.9289682539682538

                2)
                >>> def f(x):
                ...     y = 1 / x
                ...     return y
                ... sum(f, 1, 10)
                2.9289682539682538
            '''

            __sum = 0

            match _start:

                case '-infty'|'- infty'|'-\infty'|'-\\infty'|'- \infty'|'- \\infty':
                    print('暂时不支持从负无穷开始求和')
                    return None

            x = _start

            match _stop:

                case 'infty'|'\infty'|'\\infty'|'+infty'|'+ infty'|'+\infty'|'+ \infty'|'+\\infty'|'+ \\infty':

                    t = time.time()
                    while time.time() < t + 10:
                        if time.time() >= t + 10:
                            break

                        __sum += _expressions(x)
                        x += 1

                case _:

                    if _start > _stop:
                        _start, _stop = _stop, _start

                    while x <= _stop:
                        __sum += _expressions(x)
                        x += 1

            return __sum

        class Calculus:

            '''
                python 计算微积分（
                这个类里面所有的方法都有精度 n (默认为 2 ** 25 )
                由于微积分需要用到极限，但在 python 中无法实现极限运算，故选择一个大数以模拟极限情况.
                可以在参数末尾加入 `n = 一个整数` 以改变精度
                注意：n越大，计算时间越久！
                导入时建议使用这个：
                >>> from calculus import Calculus
            '''

            def __init__(self):
                ...

            def definite_integral(self, f, a, b, n = 2 ** 25):
                '''
                    定积分/黎曼积分

                    使用方法:
                    >>> definite_integral(lambda x: 关于x的函数表达式, 积分下限, 积分上限, 精度)
                '''
                __dx = (b - a) / n
                __y = 0
                return self.sum(lambda x: __dx * f(a + x * __dx), 0, n)


            def derivative(self, f, x, n = 2 ** 25):
                '''
                    导数/微分
                    在函数上某点的导数值

                    使用方法:
                    >>> derivative(lambda x: 关于x的函数表达式, 点的横坐标, 精度)
                '''
                __dx = 1 / n
                __dy = f(x + __dx) - f(x)
                return __dy / __dx


            # 分析函数 f(x) 在区间 (a, b) 的凹凸性
            def convexity(self, f, a, b):
                '''
                    分析函数的凹凸性

                    使用方法:
                    >>> convexity(lambda x: 关于x的函数表述式, 区间下限, 区间上限)
                '''
                __m1 = f((a + b) / 2)
                __m2 = (f(a) + f(b)) / 2

                # 通过凹凸性的定义判断
                if __m1 > __m2:
                    return '凸'
                elif __m1 < __m2:
                    return '凹'
                else:
                    return '无法判断'


            def tangent_line(self, f, x, n = 2 ** 25):
                '''
                    函数 f(x) 在点 (x, f(x)) 处的切线方程

                    使用方法:
                    >>> tangent_line(lambda x: 关于x的函数表达式, 切点横坐标, 精度)
                '''
                __k = self.derivative(f, x, n)
                __m = f(x) - __k * x
                __result = {
                    "斜率": __k,
                    "y轴截距": __m,
                    '直线方程': f'y={__k}x+{__m}'
                }
                return __result


            def normal_line(self, f, x, n = 2 ** 25):
                '''
                    函数 f(x) 在点 (x, f(x)) 处切线的法线方程

                    使用方法:
                    >>> normal_line(lambda x: 关于x的函数表达式, 切点横坐标, 精度)
                '''

                __k = - 1 / self.derivative(f, x, n)
                __m = f(x) - __k * x

                __result = {
                    "斜率": __k,
                    "y轴截距": __m,
                    '法线方程': f'y={__k}x+{__m}'
                }
                return __result


            def sum(self, f, _start=0, _stop=10):
                '''
                    sum(lambda x: 关于x的函数表达式, 起始值, 终值)
                    不支持无穷大的计算，起始值必须大于终值

                    For example:
                    1)
                        >>> def f(x):
                        ...     return 1/x
                        ... sum(f, 1, 10)
                        2.9289682539682538
                    2)
                        >>> sum(lambda x: 1 / x, 1, 10)
                        2.9289682539682538
                '''
                __sum = 0
                if _start > _stop:
                    _start, _stop = _stop, _start
                x = _start

                while x <= _stop:
                    __sum += f(x)
                    x += 1

                return __sum


    class ListSort:

        def __init_(self):
            ...


        # 选择排序
        def select(self, list):
            for i in range(len(list) - 1):
                min = i
                for j in range(i + 1, len(list)):
                    if list[j] < list[min]:
                        min = j
                list[i], list[min] = list[min], list[i]
            return list


        # 插入排序
        def insert(self, list):
            for i in range(1, len(list)):
                for j in range(i, 0, -1):
                    if list[j] < list[j - 1]:
                        list[j], list[j - 1] = list[j - 1], list[j]
            return list


        # 快速排序
        def quick(self, list):
            if len(list) <= 1:
                return list
            pivot = list[0]
            left = [i for i in list[1:] if i < pivot]
            right = [i for i in list[1:] if i >= pivot]
            return left + [pivot] + right


        # 冒泡排序
        def bubble(self, list):
            for i in range(len(list) - 1):
                for j in range(len(list) - 1 - i):
                    if list[j] > list[j + 1]:
                        list[j], list[j + 1] = list[j + 1], list[j]
            return list


        # 归并排序
        def merge(self, list):
            if len(list) <= 1:
                return list
            mid = len(list) // 2
            left = list[:mid]
            right = list[mid:]
            return merge(left) + merge(right)


        # 希尔排序
        def shell(self, list):
            gap = len(list) // 2
            while gap > 0:
                for i in range(gap, len(list)):
                    j = i
                    while j >= gap and list[j] < list[j - gap]:
                        list[j], list[j - gap] = list[j - gap], list[j]
                        j -= gap
                gap //= 2
            return list


        # 计数排序
        def count(self, list):
            max_num = max(list)
            count_list = [0] * (max_num + 1)
            for i in list:
                count_list[i] += 1
            result = []
            for i in range(len(count_list)):
                result += [i] * count_list[i]
            return result


        # 桶排序
        def bucket(self, list):
            max_num = max(list)
            bucket_list = [[] for _ in range(max_num + 1)]
            for i in list:
                bucket_list[i].append(i)
            result = []
            for i in bucket_list:
                result += i
            return result


    class SysCmd:

        '''
            系统命令包
            仅限 Windows
        '''


        def __init__(self, _SysCmd): # 初始化，没得说
            self._SysCmd = _SysCmd


        def cmd(self, command = 'help'):

            '''
                执行系统（cmd）命令
            '''

            os.system(self, command)


        def mkdir(self, _file_name):

            '''
                创建文件夹
            '''

            # os.makedirs(f'.\\{ _file_name }\\')
            Tools.SysCmd.cmd(f'mkdir ".\\{ _file_name }\\"')


        def md(self, _file_name):

            """
                mkdir 的别名
            """

            Tools.SysCmd.mkdir(_file_name)


        def cd(self, workpath = None):
            if workpath != None: os.chdir(workpath)
            print(os.getcwd())


        def del_file(self, path):
            os.remove(path)


        def rd(self, path):
            os.rmdir(path)

    class BetterPrint:
        '''
        更好的 print, 支持代码格式化
        可以关闭格式化

        需要启用格式化看下面：
        >>> bPrint = BetterPrint()
        >>> eg = [{'a':1, 'b':2}, {'a':3, 'b':4}]
        >>> bPrint(eg, format_=True)
        [
            {
                'a': 1,
                'b': 2
            },
            {
                'a': 3,
                'b': 4
            }
        ]
        '''

        def __init__(self): ...

        def __call__(
            self,
            *values: object,
            _sep: str = ...,
            _end: str = ...,
            _file: str = ...,
            _flush: bool = ...,
            format_: bool = False,
        ) -> None:
            if format_: self.formatPrint(*values, end=_end)
            else:
                print(
                    object_,
                    sep=_sep,
                    end=_end,
                    file=_file,
                    flush=_flush
                )

        def formatPrint(
            self,
            *values: object,
            end: str = ...
        ) -> None:
            # tabstr = '    ' # 这是 4 个空格
            tabstr = '	' # 这是 Tab 制表符 '\t'
            tab = 0

            for string in values:
                if type(string) != str: string = str(string)

                for index in range(len(string)):
                    char = string[index]

                    if char in '([{':
                        print(char, end='')
                        tab += 1
                        print('\n', end=tabstr * tab)
                    elif char in '}])':
                        print()
                        tab -= 1
                        print(tabstr * tab, end=char)
                    elif char == ',':
                        print(char)
                        print(tabstr * tab, end='')
                    elif char == ' ':
                        # 当前面是空格 ( ) 或者半角逗号 (,) 时跳过
                        match string[index -1]:
                            case ' '|',': continue
                        print(char, end='')
                    else: print(char, end='')
                
                print(' ', end='')
            print('',end=end)
            return None

        def __str__(self) -> str: return 'BetterPrint', self.__doc__


class Script:

    def __init__(self, _script): # 初始化，没得说
        self._script = _script
        self.autostudy = self.AutoStudy()


    class AutoStudy:

        def __init__(self, _autostudy): # 初始化，没得说
            self._autostudy = _autostudy

            class baomi: # www.baomi.org.cn

                def __init__(self, _baomi): # 初始化，没得说
                    self._baomi = _baomi

                __urlAndTime = { # 不看的直接注释掉就好了
                    0: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396235&siteId=95&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=4b301a70-ab97-487c-ab58-9099113fa0c4', 'time': 3.34},
                    1: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&docId=9396237&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=86439328-95e7-4423-a112-9cd7b27d539a', 'time': 3.39},
                    2: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&docId=9396241&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=b29f535f-19eb-4568-ae64-308dcf0ad10b', 'time': 4.09},
                    3: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396245&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=406cb6c6-3fe8-4ade-a1b7-f0669e13e5ba', 'time': 2.57},
                    4: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396247&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=02ad4bf6-5f14-4d4b-8b46-d215f409437a&resourceId=9a75a4cc-170c-4e69-aeb7-843fe039af56', 'time': 3.0},
                    5: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396261&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=aa17bff0-4f56-41a4-a48b-36a3e225e4c5&resourceId=15e45aa7-b12e-43c3-8594-ae9ae9f03b2e', 'time': 1.0},
                    6: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396263&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=aa17bff0-4f56-41a4-a48b-36a3e225e4c5&resourceId=b0418362-a656-45e0-817a-2d29e984332b', 'time': 1.0},
                    7: {'url': 'http://www.baomi.org.cn/bmImage?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396291&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&resourceId=ce4915d1-24a2-4231-b917-1c3f1e0025b5', 'time': 0.05},
                    8: {'url': 'http://www.baomi.org.cn/bmImage?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396297&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&resourceId=3e41c7c6-df7d-4eff-aaa9-d99185c1a9fa', 'time': 0.05},
                    9: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396610&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=c598cb7a-1ca1-4475-a287-913a6d893e9e', 'time': 1.14},
                    10: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396662&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=b298555c-a51b-43ab-bfb8-637c4336f5fe', 'time': 2.36},
                    11: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396614&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=48a7fc91-ee46-4eae-83a0-b01c8971f42d', 'time': 1.11},
                    12: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396652&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6b225d59-b72c-494c-b723-2e4776734afb', 'time': 1.55},
                    13: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396644&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=381bd65e-3e5b-437e-af0f-2ab838a87289', 'time': 1.33},
                    14: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396618&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=e17fc6e7-501d-440e-9b4d-1452d45e51f1', 'time': 1.05},
                    15: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396626&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=401d774a-2026-44f4-ae77-5934de870347', 'time': 1.08},
                    16: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396642&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=f96fe100-a30c-465b-8b36-782ab4784af5', 'time': 1.36},
                    17: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396656&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6afdbd42-cd8d-489b-9a44-26a1303e77af', 'time': 2.5},
                    18: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396606&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=31abd8cc-c01a-4430-b916-f5c91ad71238', 'time': 1.05},
                    19: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396620&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=9aa1be35-b47e-4f8a-8a86-3abe5cd3c17c', 'time': 1.31},
                    20: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396650&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=33b16902-1570-4b77-b833-30619af978e3', 'time': 2.44},
                    21: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396616&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=80d26d36-85f1-464a-b003-c73822521f23', 'time': 1.45},
                    22: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396636&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=36d99c10-82ba-441d-843a-ccb076e0c244', 'time': 1.31},
                    23: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396630&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=e1886f5e-77fa-4617-9a01-df7bf7074417', 'time': 1.32},
                    24: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396624&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=66c5fcea-dd8e-45ee-b2ff-3c9a70219e63', 'time': 1.26},
                    25: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396608&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=473f2772-f354-438b-b87f-7226a8fcdd89&resourceId=6d3f2b2d-5c55-4f97-822b-0f20511565f3', 'time': 1.35},
                    26: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396667&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=677cb38c-05c4-4319-9a07-28a0041261ff', 'time': 5.12},
                    27: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396669&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=57778a2c-5dbd-4865-9f00-f464ec99bd8d', 'time': 15.43},
                    28: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396664&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=84a676fd-d3fe-4c95-8645-0d31f4a75845', 'time': 4.39},
                    29: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396658&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=a27c6d09-eac5-4f7d-b7bc-cb6218c1035d', 'time': 3.28},
                    30: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396646&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=b495dc7b-ea00-4176-83d5-3d6a6c9242aa', 'time': 1.46},
                    31: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396660&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=dce76a57-cf3b-4c12-81ca-7101f92d80b9&resourceId=a757be22-73d4-4f5d-9691-c3c36f4f0e98', 'time': 3.48},
                    32: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396314&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=1d2fa8ea-45a5-48eb-900f-3686f4d3dbdc', 'time': 3.13},
                    33: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396312&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=e3966d75-811c-4acd-8078-86870b6f4c0e', 'time': 3.01},
                    34: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396309&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=faa6e69b-ea76-4a6e-95a6-5ee4a911de65', 'time': 2.57},
                    35: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396307&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=38745c0e-3170-40be-8b11-3314e3e71cc4&resourceId=96a17f45-67b8-4b84-b5e1-ef628b47cea7', 'time': 3.57},
                    36: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396323&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=c51a68a7-1967-4d98-8495-ff26c70c735d', 'time': 2.37},
                    37: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396321&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=10e8e72b-5322-4d13-9a61-399ef61045b2', 'time': 2.42},
                    38: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396319&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=8a475b1d-179e-4549-a28c-e5f3e348f11a', 'time': 3.46},
                    39: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396317&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=7e07aef4-dbe0-4315-9fd1-544ae0a2845b', 'time': 3.04},
                    40: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396690&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=b98980e3-eb45-43b5-89a3-c7adae15d0c3', 'time': 12.36},
                    41: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396682&docLibId=-15&pubId=&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=75a8d2c0-af69-4af6-aebb-0b77c1580f9a', 'time': 8.14},
                    42: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396688&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=09e3de26-efcc-42cc-a897-81fac3c3ed1b', 'time': 10.25},
                    43: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396692&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b94631f9-367c-4a43-8587-0281b8113c4e', 'time': 14.17},
                    44: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396684&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=1a00d8d3-a3cd-4f27-b7d0-d1b6003e2fb1', 'time': 8.19},
                    45: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396686&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b90f7753-6688-49d3-87ba-b4a4de0c698c', 'time': 8.58},
                    46: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396589&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=5d9d4a20-6a5b-42b8-8542-dab589b8d67b', 'time': 4.18},
                    47: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396591&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=05506b68-b97d-4c24-8ef2-a5ac95efd445', 'time': 4.33},
                    48: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396587&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b7c5fad6-6654-4cc1-ad0e-6ba6e1633b90', 'time': 4.01},
                    49: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396596&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=e0744709-90dd-43e5-b98c-5b243cb20fd9', 'time': 3.26},
                    50: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396598&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=276b6c77-e9d4-42d6-80cf-83336bed10be', 'time': 3.54},
                    51: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396600&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b545c846-44b4-46f4-ad3b-cb7c287b2484', 'time': 4.14},
                    52: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396321&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=10e8e72b-5322-4d13-9a61-399ef61045b2', 'time': 2.42},
                    53: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396319&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=8a475b1d-179e-4549-a28c-e5f3e348f11a', 'time': 3.46},
                    54: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396317&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=770c6f80-1836-49eb-a80d-ea729fd92659&resourceId=7e07aef4-dbe0-4315-9fd1-544ae0a2845b', 'time': 3.04},
                    55: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396690&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=b98980e3-eb45-43b5-89a3-c7adae15d0c3', 'time': 12.36},
                    56: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396682&docLibId=-15&pubId=&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&doclibId=3&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=75a8d2c0-af69-4af6-aebb-0b77c1580f9a', 'time': 8.14},
                    57: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396688&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=16757c09-3670-4afd-b879-e30f2c66859a&resourceId=09e3de26-efcc-42cc-a897-81fac3c3ed1b', 'time': 10.25},
                    58: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396692&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b94631f9-367c-4a43-8587-0281b8113c4e', 'time': 14.17},
                    59: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396684&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=1a00d8d3-a3cd-4f27-b7d0-d1b6003e2fb1', 'time': 8.19},
                    60: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396686&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=5b214b93-b723-4894-8ea1-fab3b4375233&resourceId=b90f7753-6688-49d3-87ba-b4a4de0c698c', 'time': 8.58},
                    61: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396589&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=5d9d4a20-6a5b-42b8-8542-dab589b8d67b', 'time': 4.18},
                    62: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396591&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=05506b68-b97d-4c24-8ef2-a5ac95efd445', 'time': 4.33},
                    63: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396587&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b7c5fad6-6654-4cc1-ad0e-6ba6e1633b90', 'time': 4.01},
                    64: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396596&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=e0744709-90dd-43e5-b98c-5b243cb20fd9', 'time': 3.26},
                    65: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396598&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=276b6c77-e9d4-42d6-80cf-83336bed10be', 'time': 3.54},
                    66: {'url': 'http://www.baomi.org.cn/bmVideo?id=897ed48c-b420-4b43-844b-280147eb422a&docId=9396600&siteId=95&title=2023%E5%B9%B4%E5%BA%A6%E4%BF%9D%E5%AF%86%E6%95%99%E8%82%B2%E7%BA%BF%E4%B8%8A%E5%9F%B9%E8%AE%AD&IsAudition=false&flag=false&status=1&isAllowToEndCourse=1&doclibId=3&pubId=&coursePacketId=897ed48c-b420-4b43-844b-280147eb422a&directoryId=e341d308-35c2-4d82-b9f5-82c5df521875&resourceId=b545c846-44b4-46f4-ad3b-cb7c287b2484', 'time': 4.14}
                }


                def image2byte(image):
                    '''
                    图片转byte
                    image: 必须是PIL格式
                    image_bytes: 二进制
                    '''
                    # 创建一个字节流管道
                    img_bytes = io.BytesIO()
                    # 将图片数据存入字节流管道， format可以按照具体文件的格式填写
                    image.save(img_bytes, format="JPEG")
                    # 从字节流管道中获取二进制
                    image_bytes = img_bytes.getvalue()
                    return image_bytes


                # 模拟鼠标点击
                def mouse_click(x = 230, y = 760):
                    win32api.SetCursorPos([x, y])
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN, 0, 0, 0, 0)
                    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP, 0, 0, 0, 0)


                # 主线程
                class mainThread (threading.Thread): #继承父类 threading.Thread

                    def __init__(self, url):
                        threading.Thread.__init__(self)
                        self.url = url


                    def run(self):

                        # 先确保chrome被关闭了
                        if typing == 'edge':
                            os.system("taskkill /im msedge.exe /f")
                        elif typing == 'chrome':
                            os.system("taskkill /im chrome.exe /f")
                        else:
                            if kill == None:
                                print(f'【ERROR】无法识别参数 “{ typing }”')
                                return None
                            else:
                                os.system(f'taskkill /f /im { kill }')

                        time.sleep(2)

                        # 创建子线程
                        thread1 = self.childThread(1, "chrome", self.url)
                        thread2 = self.childThread(2, "play", self.url)

                        # 开启线程
                        thread1.start()
                        thread2.start()


                # 子线程
                class childThread (threading.Thread):   #继承父类threading.Thread

                    def __init__(self, threadID, name, url):
                        threading.Thread.__init__(self)
                        self.threadID = threadID
                        self.name = name
                        self.url = url


                    def run(self):                   #把要执行的代码写到run函数里面 线程在创建后会直接运行run函数

                        if (self.name == "chrome"):
                            time.sleep(0.1)
                            url = self.url

                            # 老方法需要填写用户本地浏览器地址，新方法直接调用用户默认浏览器
                            # chrome_path = 'C://Users//CZY//AppData//Local//Google//Chrome//Application//chrome.exe %s'
                            # webbrowser.get(chrome_path).open(url)

                            # 新方法，用户默认打开网页就行了
                            webbrowser.open(url)

                            print("chrome threading over")

                        elif (self.name == "play"):

                            # # 先给线程加一个锁
                            # threading.Lock().acquire()

                            # 休眠一段时间，确保 chrome 完全加载完成
                            time.sleep(10)

                            # 模拟鼠标点击
                            Script.AutoStudy.baomi.mouse_click(x, y) # 点击开始播放图标 不同的人可能不太一样，我是根据我的屏幕浏览器全屏

                            # 获取sleep时间
                            video_time = Script.AutoStudy.baomi.__urlAndTime[i]['time']
                            sleep_time = int(video_time)*60 + int(math.modf(video_time)[0]*100)
                            print("sleep time = %f"%sleep_time)
                            time.sleep(sleep_time + 8) # 多看 8 秒钟，确保容错


                            ###
                            # OCR准确率不够，手写吧
                            ###

                            # win32api.keybd_event(17,0,0,0) #ctrl键位码是17
                            # win32api.keybd_event(65,0,0,0) #A键位码是65
                            # time.sleep(0.1)
                            # win32api.keybd_event(65,0,win32con.KEYEVENTF_KEYUP,0) #释放按键
                            # win32api.keybd_event(17,0,win32con.KEYEVENTF_KEYUP,0)

                            # img = pyautogui.screenshot(region=(450,990, 110, 34)) # 得到截图区域
                            # img.save("./1.jpg")

                            # ocr = ddddocr.DdddOcr()
                            # video_time = ocr.classification(image2byte(img)) # 得到截图区域文本
                            # print("get video time%s"%video_time)

                            # 关闭chrome
                            if typing == 'edge':
                                os.system("taskkill /im msedge.exe /f")
                            elif typing == 'chrome':
                                os.system("taskkill /im chrome.exe /f")
                            else:
                                if kill == None:
                                    print(f'【ERROR】无法识别参数 “{ typing }”')
                                    return None
                                else:
                                    os.system(f'taskkill /f /im { kill }')

                            # # 释放锁，开启下一个线程
                            # threading.Lock().release()


                def main_program(self, x = 230, y = 760, typing = 'edge', kill = None):

                    """
                        你至少需要提供两个参数作为鼠标点击位置(即播放按钮的坐标)
                        这两个参数的默认值为 230, 760
                        在这之后还有一个参数作为浏览器的指示，暂时仅支持 Edge 和 Chrome 的自动开启和关闭
                        需要其他的浏览器可以选择在参数末尾加上 `type='other', kill='浏览器进程名'`
                        浏览器进程名一般后面有 `.exe`
                        For example:
                        1)
                        >>> main_program(typing='chrome')
                        chrome threading over
                        sleep time = 100
                        ...
                    """

                    # x, y = 230, 760

                    for i in Script.AutoStudy.baomi.__urlAndTime:

                        url = Script.AutoStudy.baomi.__urlAndTime[i]['url']
                        # main_thread = childThread(2, "play", url)
                        # main_thread.start()
                        # main_thread.join()

                        # 先确保chrome被关闭了
                        if typing == 'edge':
                            os.system("taskkill /im msedge.exe /f")
                        elif typing == 'chrome':
                            os.system("taskkill /im chrome.exe /f")
                        else:
                            if kill == None:
                                print(f'【ERROR】无法识别参数 “{ typing }”')
                                return None
                            else:
                                os.system(f'taskkill /f /im { kill }')
                        time.sleep(2.5)

                        # 创建子线程
                        thread1 = self.childThread(1, "chrome", url)
                        thread2 = self.childThread(2, "play", url)

                        # 开启线程
                        thread1.start()
                        thread2.start()

                        thread1.join()
                        thread2.join()

                    print("Exiting Main Thread")
                    print("请检查所有的必修是否都学完再考试")


if __name__ == "__main__":
    print('[xieyuen.py] 函数已经注册')
    print('[xieyuen.py] Please call `Information.copyright_info()` to view copyright information.')
print('[xieyuen.py] 若有 bug 请在 GitHub 上提交一个 PR')
print('[xieyuen.py] If you have a bug, please submit a PR on GitHub.')
print('[xieyuen.py] Github: https://github.com/xieyuen/Document')
