# -*- coding: utf-8 -*-
'''
xieyuen 的 python 程序整合包

导入方法：
>>> from xieyuen import package
>>> from xieyuen import package as x
:param:`package` 是文件内可调用的类对象
'''

import fnmatch
import io
import math
import os
import random
import time

import jsonpath
import requests


class Package:
    def __init__(self):
        self.tools = self.Tools()
        self.script = self.Script()
        self.info = self.Information()
        self.console = self.Console()

    class Information:
        '''
            这个 python 文件的信息
        '''
        self.help = self.Help()
        self.license = 'MIT License\n\nCopyright (c) 2023 HIM049\n\nPermission is hereby granted, free of charge, to any person obtaining a copy\nof this software and associated documentation files (the "Software"), to deal\nin the Software without restriction, including without limitation the rights\nto use, copy, modify, merge, publish, distribute, sublicense, and/or sell\ncopies of the Software, and to permit persons to whom the Software is\nfurnished to do so, subject to the following conditions:\n\nThe above copyright notice and this permission notice shall be included in all\ncopies or substantial portions of the Software.\n\nTHE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR\nIMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,\nFITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE\nAUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER\nLIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,\nOUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE\nSOFTWARE.'
        self.__version = '0.1.0'

        # LICENSE 开源协议
        def LICENSE(self):
            print(self.license)
        def license(self):
            self.LICENSE()

        def author(self):
            print('Copyright from xieyuen')

        def help(self):
            print(self.__doc__)

        def version(self):
            print('Varsion Num:' + self.__version)

        def copyright_info(self):
            self.author()
            print('\nLICENSE：\n')
            self.LICENSE()

    class Tools:
        def __init__(self):
            self.list = self.List()
            self.str = self.String()
            self.bPrint = self.BetterPrint()

        class List:
            def __init__(self):
                self.sort = self.Sort()

            def dedup(self, li: list) -> list:
                '''
                    给列表不打乱顺序地去重
                '''
                result = []
                for i in _list:
                    if i not in result:
                        result.append(i)
                return result

            class Sort:
                '''列表排序'''
                def __init__(self): ...
                def __call__(self, li: list) -> list:
                    return self.bubble(li)

                def bubble(self, li: list) -> list:
                    '''
                        冒泡排序
                    '''
                    for i in range(len(li)):
                        for j in range(len(li) - 1):
                            if li[j] > li[j + 1]:
                                li[j], li[j + 1] = li[j + 1], li[j]
                    return li

                def select(self, li: list) -> list:
                    '''
                        选择排序
                    '''
                    for i in range(len(li)):
                        min = i
                        for j in range(i + 1, len(li)):
                            if li[min] > li[j]:
                                min = j
                        li[i], li[min] = li[min], li[i]
                    return li

                def insert(self, li: list) -> list:
                    '''
                        插入排序
                    '''
                    for i in range(1, len(li)):
                        for j in range(i, 0, -1):
                            if li[j] < li[j - 1]:
                                li[j], li[j - 1] = li[j - 1], li[j]
                    return li

                def quick(self, li: list) -> list:
                    '''
                        快速排序
                    '''
                    if len(li) <= 1:
                        return li
                    pivot = li[0]
                    less = [i for i in li[1:] if i <= pivot]
                    greater = [i for i in li[1:] if i > pivot]
                    return self.quick(less) + [pivot] + self.quick(greater)

                def merge(self, li: list) -> list:
                    '''
                        归并排序
                    '''
                    if len(li) <= 1:
                        return li
                    mid = len(li) // 2
                    left = self.merge(li[:mid])
                    right = self.merge(li[mid:])
                    return self.merge(left)+ self.merge(right)

                def shell(self, li: list) -> list:
                    '''
                        希尔排序
                    '''
                    gap = len(li) // 2
                    while gap > 0:
                        for i in range(gap, len(li)):
                            temp = li[i]
                            j = i
                            while j >= gap and li[j - gap] > temp:
                                li[j] = li[j - gap]
                                j -= gap
                            li[j] = temp
                        gap //= 2
                    return li

                def count(self, li: list) -> list:
                    '''
                        计数排序
                    '''
                    max_num = max(li)
                    min_num = min(li)
                    count = [0] * (max_num - min_num + 1)
                    for i in li:
                        count[i - min_num] += 1
                    result = []
                    for i in range(len(count)):
                        result += [i + min_num] * count[i]
                    return result

                def bucket(self, li: list) -> list:
                    '''
                        桶排序
                    '''
                    max_num = max(li)
                    backet_list = [[] for i in range(max_num + 1)]
                    for i in li:
                        backet_list[i].append(i)
                    result = []
                    for i in backet_list:
                        result += i
                    return result

        class String:
            def __init__(self):
                self.randstr = self.RandomString()

            def isExistChinese(self, string: str) -> bool:
                '''检测字符串内是否存在汉字'''
                for char in string:
                    if u'\u4e00' <= char <= u'\u9fa5':  # 判断是否是汉字
                        return True
                return False

            def count(self, string = '加油华为，加油China') -> dict:
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

            class RandomString:
                def __init__(self): ...
                def __call__(self, length):
                    if random.randint(2):
                        return self.randstr1(length)
                    return self.randstr2(length)

                def randstr1(self, length):
                    __alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}:"<>?[]\|`~-=,./;\'\"1234567890'
                    __str = ''
                    for i in range(length):
                        __str += __alpha[random.randint(0, len(__alpha)-1)]
                    return __str

                def randstr2(self, length):
                    __randstring = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1234567890', '!@#$%^&*()_+{}:"<>?[]\|`~-=,./;\'"']
                    __str = ''
                    for _ in range(length):
                        __1 = random.randint(3)
                        __2 = random.randint(len(__randstring[__1])-1)
                        __str += __randstring[__1][__2]
                    return __str

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
        def __init__(self):
            self.al = self.auto_learning = self.AutoLearning()
            self.craw = self.crawler = self.Crawler()

        class AutoLearning:
            def __init__(self):
                import webbrowser
                import win32api
                import win32con
                import threading

                self.bao_mi = self.BaoMi()

            class BaoMi:
                def __init__(self):
                    self.urlAndTime = { # 视频链接，不看的直接注释掉就好了
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
                def __call__(
                    self,
                    x: int = 230,
                    y: int = 760,
                    typing: str = 'edge',
                    kill: str|None = None
                ): self.main(x, y, typing, kill)

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
                            if kill is None:
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
                class childThread (threading.Thread): #继承父类 threading.Thread

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
                            self.mouse_click(x, y) # 点击开始播放图标 不同的人可能不太一样，我是根据我的屏幕浏览器全屏

                            # 获取sleep时间
                            video_time = self.__urlAndTime[i]['time']
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
                                if kill is None:
                                    print(f'【ERROR】无法识别参数 “{ typing }”')
                                    return None
                                else:
                                    os.system(f'taskkill /f /im { kill }')

                            # # 释放锁，开启下一个线程
                            # threading.Lock().release()

                def main(
                    self,
                    x: int = 230,
                    y: int = 760,
                    typing: str = 'edge',
                    kill: str|None = None
                ):
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
                    for i in self.__urlAndTime:
                        url = self.__urlAndTime[i]['url']
                        # main_thread = childThread(2, "play", url)
                        # main_thread.start()
                        # main_thread.join()

                        # 先确保chrome被关闭了
                        if typing == 'edge':
                            os.system("taskkill /im msedge.exe /f")
                        elif typing == 'chrome':
                            os.system("taskkill /im chrome.exe /f")
                        else:
                            if kill is None:
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

        class Crawler:
            def __init__(self):
                self.pic = self.Picture()
                self.music = self.Music()

            class Picture:
                def __init__(self):
                    self.root = './img/'

                def change_root(self, root: str):
                    self.root = root

                def main(self, _url: str, _root: str = self.root):
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

            class Music:
                def __init__(self):
                    self.platfrom: str|None = None
                    self.name: str|None = None
                def __call__(
                    self,
                    name: str = self.name,
                    platfrom: str = self.platfrom,
                ): self.main(name, platfrom)


                def get_music_platfrom(self):
                    print("1.网易云:netease\n2.QQ:qq\n3.酷狗:kugou\n4.酷我:kuwo\n5.百度:baidu\n6.喜马拉雅:ximalaya")
                    self.platfrom = input("输入音乐平台类型:")
                    self.invert_platfrom()
                    return self.platfrom

                def invert_platfrom(self):
                    """
                        检测并转换平台参数(大小写均可识别)
                    """
                    if not isinstance(self.platfrom, str): self.platfrom = str(self.platfrom)
                    _platfrom = str.lower(self.platfrom) # 将所有的大写字母转化为小写
                    match _platfrom:
                        # 网易云 netease
                        case '1'|'n'|'net'|'wy'|'wyy'|'wangyi'|'wangyiyun'|'netease'|'网易'|'网易云'|'网易云音乐':
                            self.platfrom = 'neatese'
                        # QQ qq
                        case '2'|'q'|'qq'|'qqmusic'|'qqyinyue'|'qq音乐'|'qq 音乐':
                            self.platfrom = 'qq'
                        # 酷狗 kugou
                        case '3'|'kg'|'ku'|'kou'|'gou'|'kugou'|'酷狗':
                            self.platfrom = 'kugou'
                        # 酷我 kuwo
                        case '4'|'kw'|'ko'|'wo'|'kuwo'|'酷我':
                            self.platfrom = ''
                        # 百度 baidu
                        case '5'|'b'|'bd'|'bu'|'baidu'|'百度':
                            self.platfrom = 'baidu'
                        # 喜马拉雅 ximalaya
                        case '6'|'x'|'xi'|'xmly'|'xmla'|'ximalaya'|'喜马拉雅':
                            self.platfrom = 'ximalaya'
                        # 无法识别
                        case _:
                            print(f"【ERROR】\n无法识别到你输入的 '{ self.platfrom }' 平台")
                            __check = int(input('请选择操作：\n [1]重新输入参数\n [2]使用默认值'))
                            print("-------------------------------------------------------")
                            if __check == 1:
                                self.get_music_platfrom()
                            if __check == 2:
                                self.platfrom = 'netease'
                    return self.platfrom

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

                def main(
                    self,
                    name: str = self.name,
                    platfrom: str = self.platfrom,
                ):
                    '''
                        音乐爬虫主程序
                    '''
                    """
                        搜索歌曲名称
                        :return:
                    """
                    if name is None:
                        self.name = input("请输入歌曲名称:")
                    else: self.name = name
                    if platfrom is None:
                        self.get_music_platfrom() # 获取搜索的平台
                    else:
                        self.invert_platfrom()

                    print("-------------------------------------------------------")

                    url = 'https://music.liuzhijin.cn/'
                    headers = {
                        "user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/87.0.4280.141 Safari/537.36",
                        # 判断请求是异步还是同步
                        "x-requested-with":"XMLHttpRequest",
                    }
                    param = {
                        "input": self.name,
                        "filter":"name",
                        "type": self.platfrom,
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
                        index = int(input("请输入您想下载的歌曲版本(编号从 0 开始):"))
                        self.download_music(url[index],title[index],author[index])
                    else:
                        print("对不起，暂无搜索结果!")
                        return False

    class Console:
        def __init__(self):
            from mymodule import logger
            from mymodule import exceptions

            self.logger = logger.logger
            self.exce = self.exception = self.exceptions = exceptions

        def __repr__(self) -> 'Self':
            return self

package = Package()


command_tree = {
    'tools': {
        'self':               package.tools,
        'better_print':       package.tools.bPrint,
        'bPrint':             package.tools.bPrint,
        'list': {
            'dedup':          package.tools.list.dedup,
            'sort':           package.tools.list.sort,
            'bubble_sort':    package.tools.list.sort.bubble,
            'insert_sort':    package.tools.list.sort.insert,
            'merge_sort':     package.tools.list.sort.merge,
            'quick_sort':     package.tools.list.sort.quick,
            # 'heap_sort':      package.tools.list.sort.heap,
            # 'radix_sort':     package.tools.list.sort.radix,
            'select_sort':    package.tools.list.sort.select,
            'shell_sort':     package.tools.list.sort.shell,
            'count_sort':     package.tools.list.sort.count,
            'bucket_sort':    package.tools.list.sort.bucket,
        },
        'str': {
            'isExistChinese': package.tools.str.isExistChinese,
            'count':          package.tools.str.count,
            'randstr':        package.tools.str.randstr,
        },
    },
    'script': {
        'self':               package.script,
        'crawler': {
            'music':          package.script.crawler.music,
            'pic':            package.script.crawler.pic,
        },
        'auto_learning': {
            'bao_mi':         package.script.auto_learning.bao_mi,
        },
    },
    'info': {
        'self':               package.info,
        'copyright_info':     package.info.copyright_info,
        'version':            package.info.version,
        'author':             package.info.author,
        'license':            package.info.license,
    },
}

class RecursiveMethods:
    def __init__(self):
        self.logger = package.console.logger
        self.exce = self.exception = self.exceptions = package.console.exceptions

    def normalCommandParse(self,
        parse_list: list,
        map: dict,
        *, first: bool = True,
    ) -> callable:
        if len(parse_list) == 1:
            if parse_list[0] == 'exit' and first: raise SystemExit
            action = map.get(parse_list[0], None)
            if action is None: raise self.exce.CommandParseError(f'指令解析出错: {parse_list[0]} 不存在')
            return action
        else:
            if parse_list[0] not in map:
                raise CommandParseError(parse_list[0])
            return self.normalCommandParse(parse_list[1:], map[parse_list[0]], first=False)

RM = RecursiveMethods()

def main():
    package.console.logger.info('请在 >>> 后面输入命令')
    package.console.logger.info('一些常用的脚本:')
    package.console.logger.info('音乐爬虫：script crawler music')
    package.console.logger.info('图片爬虫：script crawler pic')
    package.console.logger.info('中国保密在线 自动学习：script auto_learning bao_mi')
    print()

    while True:
        input_str = input(">>> ")
        input_list = str.lower(input_str).split()
        mapped = [''] * 3

        if input_list[0] == 'exit': break
        elif input_list[0] == 'help':

            # help
            if input_list[1] is None:
                package.console.logger.info('help')
                package.console.logger.info('help 命令帮助：\n直接在命令前面加上help就行')
                continue

            mapped[0] = command_tree.get(input_list[1], None)
            if not mapped[0]:
                package.console.logger.info(f'无法解析 {input_list[1]}')
                continue

            try: input_list[2]
            except:
                print(mapped[0]['self'].__doc__)
                continue
            mapped[1] = mapped[0].get(input_list[2], None)
            if not mapped[1]:
                package.console.logger.info(f'无法解析 {input_list[2]}')
                continue

            try: input_list[3]
            except:
                print(mapped[1]['self'].__doc__)
                continue
            mapped[2] = mapped[1].get(input_list[3], None)
            if not mapped[2]:
                package.console.logger.info(f'无法解析 {input_list[3]}')
                continue

        mapped[0] = command_tree.get(input_list[0], None)
        if not mapped[0]:
            package.console.logger.catch_exc(f'无法识别你的输入 {input_list[0]}')
            continue

        mapped[1] = mapped[0].get(input_list[1], None)
        if not mapped[1]:
            package.console.logger.catch_exc(f'无法识别参数 {input_list[1]}')
            continue

        mapped[2] = mapped[1].get(input_list[2], None)
        if not mapped[2]:
            package.console.logger.catch_exc(f'无法识别参数 {input_list[2]}')
            continue

        if input_list[3] == 'start':
            if input_list[3:] == []: mapped[2].main()
            else: mapped[2].main(*input_list[3:])
            continue

        mapped[2](*input_list[2:])
        # like: package.mapped[0].mapped[1].mapped[2].main()

        package.console.logger.info('命令不存在')

    package.console.logger.info('Bye!')
    raise SystemExit(0)

if __name__ == '__main__':
    main()
