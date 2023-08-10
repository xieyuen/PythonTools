# Code Whisperer
import unittest
import random
import string

from math import *
from random import randint as ri, random as rd

class Decorators:
    '''
    装饰器
    '''
    def run_time(func):
        '''计算函数耗时'''
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            print(f'耗时：{time.time() - start}秒')
        return wrapper
    def 运行时间(func):
        def wrapper(*args, **kwargs):
            start = time.time()
            func(*args, **kwargs)
            print(f'耗时：{time.time() - start}秒')
        return wrapper

    run_time = staticmethod(run_time)


class Multi:
    # 写一个函数，生成九九乘法表
    def 九九乘法表():
        for i in range(1, 10):
            for j in range(1, i + 1):
                if j == i:
                    print(f'{j}*{i}={i * j}')
                    break
                print(f'{j}*{i}={i * j}', end='\t')
            print()


class Randoms:
    def __init__(self): ...


    def random_string(length):
        return ''.join(random.choice(string.ascii_lowercase) for i in range(length))


    def randstr(length):
        __alpha = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ!@#$%^&*()_+{}:"<>?[]\|`~-=,./;\'\"1234567890'
        __str = ''
        for i in range(length):
            __str += __alpha[random.randint(0, len(__alpha)-1)]
        return __str


    def randstr2(length):
        __randstring = ['abcdefghijklmnopqrstuvwxyz', 'ABCDEFGHIJKLMNOPQRSTUVWXYZ', '1234567890', '!@#$%^&*()_+{}:"<>?[]\|`~-=,./;\'\"']
        __str = ''
        for __ in range(length):
            __1 = random.randint(0, 3)
            __2 = random.randint(0, len(__randstring[__1])-1)
            __str += __randstring[__1][__2]
        return __str


class Sorts:
    def __init__(self): ...


    # 写一个函数对列表进行选择排序
    def select(self, list):
        for i in range(len(list) - 1):
            min = i
            for j in range(i + 1, len(list)):
                if list[j] < list[min]:
                    min = j
            list[i], list[min] = list[min], list[i]
        return list


    # 写一个函数对列表进行插入排序
    def insert(self, list):
        for i in range(1, len(list)):
            for j in range(i, 0, -1):
                if list[j] < list[j - 1]:
                    list[j], list[j - 1] = list[j - 1], list[j]
        return list


    # 写一个函数对列表快速排序
    def quick(self, list):
        if len(list) <= 1:
            return list
        pivot = list[0]
        left = [i for i in list[1:] if i < pivot]
        right = [i for i in list[1:] if i >= pivot]
        return  quick(left) + [pivot] + quick(right)


    # 写一个函数对列表进行冒泡排序
    def bubble(self, list):
        for i in range(len(list) - 1):
            for j in range(len(list) - 1 - i):
                if list[j] > list[j + 1]:
                    list[j], list[j + 1] = list[j + 1], list[j]
        return list


    # 写一个函数对列表进行归并排序
    def merge(self, list):
        if len(list) <= 1:
            return list
        mid = len(list) // 2
        left = list[:mid]
        right = list[mid:]
        return merge(left) + merge(right)


    # 写一个函数对列表进行堆排序
    def heap(self, list):
        for i in range(len(list) // 2, -1, -1):
            __heap(list, i, len(list))
        for i in range(len(list) - 1, 0, -1):
            list[0], list[i] = list[i], list[0]
            __heap(list, 0, i)
        return list


    # 写一个函数对列表进行基数排序
    def radix(self, list):
        max_num = max(list)
        digit = len(str(max_num))
        for i in range(digit):
            __radix(list, i)
        return list


    # 写一个函数对列表进行希尔排序
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


    # 写一个函数对列表进行计数排序
    def count(self, list):
        max_num = max(list)
        count_list = [0] * (max_num + 1)
        for i in list:
            count_list[i] += 1
        result = []
        for i in range(len(count_list)):
            result += [i] * count_list[i]
        return result


    # 写一个函数对列表进行桶排序
    def bucket(self, list):
        max_num = max(list)
        bucket_list = [[] for _ in range(max_num + 1)]
        for i in list:
            bucket_list[i].append(i)
        result = []
        for i in bucket_list:
            result += i
        return result


# 写一个函数，求列表 li 的最大值、最小值、极差、方差、平均数、中位数和众数，并用拉格朗日插值法求通项公式
def statistics(li):
    __max = max(li)
    __min = min(li)
    __range = __max - __min
    __mean = sum(li) / len(li)
    __variance = sum([(i - __mean) ** 2 for i in li]) / len(li)
    __median = sorted(li)[len(li) // 2]
    __mode = max(set(li), key=li.count)
    __x_data = [i for i in range(len(li))]
    __y_data = li
    __result = {
        "最大値": __max,
        "最小値": __min,
        "总和": sum(li),
        "总数": len(li),
        "总秩": sum([(i - __mean) ** 2 for i in li]) / (len(li) - 1),
        "总方差": __variance,
        "极差": __range,
        "方差": __variance,
        "平均数": __mean,
        "中位数": __median,
        "众数": __mode,
        "拉样点法": LagrangeInterpolationDotN_F('x', __x_data, __y_data)
    }
    return __result


class NumListStatistics:
    # vars
    len:      int
    max:      int|float
    min:      int|float
    range:    int|float
    mean:     int|float
    variance: int|float
    median:   int|float
    mode:     int|float|list[int|float]

    # config
    启用汉字:   bool
    启用标准差: bool

    def __init__(self,
        numlist,
        启用标准差: bool = False,
        启用汉字:   bool = True,
    ):
        self.numlist = numlist
        self.general_term_formulas = \
            self.GeneralTermFormulas()
        if self.启用汉字:
            self.通项公式 = self.general_term_formulas

        self.len = len(self.numlist)

    def get_max(self) -> int|float:
        self.max = max(self.numlist)
        return self.max

    def get_min(self) -> int|float:
        self.min = min(self.numlist)
        return self.min

    def get_range(self) -> int|float:
        self.range = self.max - self.min
        return self.range

    def get_mean(self) -> int|float:
        self.mean = sum(self.numlist) / self.len
        return self.mean

    def get_variance(self) -> int|float:
        self.variance = (
            sum([i ** 2  for i in self.numlist])
            / self.len - (self.mean) ** 2
        )
        return self.variance

    def get_median(self) -> int|float:
        sorted_list = sorted(self.numlist)
        if self.len % 2 == 0:
            self.median = \
                sorted_list[self.len / 2]
        else:
            left = sorted_list[self.len // 2]
            right = sorted_list[self.len // 2 + 1]
            self.median = (left + right) / 2

        return self.median

    def get_mode(self) -> int|float|list[int|float]:
        count_dict = {
            i: 0  for i in set(self.numlist)
        }

        for num in self.numlist:
            count_dict[num] += 1

        max_count = max(count_dict[i] for i in count_dict)

        self.mode = []
        for key, value in count_dict.items():
            if value == max_count:
                self.mode.append(key)
        if len(self.mode) == 1:
            self.mode = self.mode[0]

        return self.mode
        # return max(set(self.numlist), key=self.numlist.count)

    def get_index(self, num: int) ->int|float|list[int|float]:
        res = []
        for index, n in zip(range(self.len), self.numlist):
            if n == num:
                res.append(index)
        if len(res) == 1:
            res = res[0]
        return res

    def clac_save(self):
        '''计算并保存'''
        self.get_max();      self.get_min()
        self.get_range();    self.get_mean()
        self.get_variance(); self.get_median()
        self.get_mode()

        if self.启用汉字:
            self.数据量 = self.len
            self.最大值 = self.max
            self.最小值 = self.min
            self.极差   = self.range
            self.平均数 = self.mean
            self.方差   = self.variance
            self.中位数 = self.median
            self.众数   = self.mode
            if self.启用标准差:
                from math import sqrt
                self.标准差 = sqrt(self.variance)

    def load_all_in_dict(self) -> dict:
        self.attr = {}
        while True:
            try:
                self.attr['len'] = self.len
                self.attr['max'] = self.max
                self.attr['min'] = self.min
                self.attr['range'] = self.range
                self.attr['mean'] = self.mean
                self.attr['variance'] = self.variance
                self.attr['median'] = self.median
                self.attr['mode'] = self.mode

                if self.启用汉字:
                    self.attr['数据量'] = self.len
                    self.attr['最大值'] = self.max
                    self.attr["最大值"] = self.max
                    self.attr["最小值"] = self.min
                    self.attr["极差"]   = self.range
                    self.attr["平均数"] = self.mean
                    self.attr["方差"]   = self.variance
                    self.attr["中位数"] = self.median
                    self.attr["众数"]   = self.mode
            except:
                self.clac_save()
                continue
            break

        return self.attr


    class GeneralTermFormulas:
        def __init__(self,
            x_data: list,
            y_data: list
        ):
            self.x_data = x_data
            self.y_data = y_data
        def __call__(self, x):
            return self.func(x)

        def base_func(self,
            x, x_data, y_data, k
        ):
            size = len(x_data)
            i = 0
            Ly = y_data[k]  # 初值为Yk
            while (i < size):
                if (i != k):
                    Ly = Ly * (x - x_data[i])/(x_data[k] - x_data[i])
                i += 1
            return (Ly)

        def func(self,
            x,
            x_data = self.x_data,
            y_data = self.y_data,
        ):
            size = len(x_data)
            k = 0
            sum = 0  # 刚倒为0
            while (k < size):
                sum += self.base_func(x, x_data, y_data, k)
                k += 1
            return (sum)

# 拉格朗日插值法
class LagrangeInterpolation:
    def __init__(self): ...

    # 通用的基函数的定义
    def Li(self, x, x_data, y_data, k):
        size = len(x_data)
        i = 0
        Ly = y_data[k]  # 初值为Yk
        while (i < size):
            if (i != k):
                Ly = Ly * (x - x_data[i])/( x_data[k] - x_data[i])
            i += 1
        return (Ly)

    # 通用的插值函数的定义
    def F(self, x, x_data, y_data):
        size = len(x_data)
        k = 0
        sum = 0  # 初值为0
        while (k < size):
            sum += self.Li(x, x_data, y_data, k)
            k += 1
        return (sum)


# 定义一个函数，计算函数 f(x) 当 x 是区间 [a, b] 里的任意整数时函数值的连乘积
def convolution(f, a, b):
    __result = 1
    for i in range(a, b + 1):
        __result *= f(i)
    return __result


class Calculus: # 微积分计算 copy from calculus.py
    def __init__(self): ...

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


# 写一个函数，将列表 li 打乱
def list_shuffle(li):
    return random.shuffle(li)


def multiply_strings(num1, num2):
    # 将输入的字符串转换为列表，并反转，方便从低位到高位进行计算
    num1 = num1[::-1]
    num2 = num2[::-1]

    # 初始化结果列表，并用0填充
    result = [0] * (len(num1) + len(num2))

    # 逐位相乘，并将结果累加到对应的位置
    for i in range(len(num1)):
        for j in range(len(num2)):
            result[i + j] += int(num1[i]) * int(num2[j])
            # 处理进位
            if result[i + j] >= 10:
                result[i + j + 1] += result[i + j] // 10
                result[i + j] %= 10

    # 将结果列表转换为字符串并反转，去除前导零
    result_str = ''.join(str(i) for i in result[::-1]).lstrip('0')
    return result_str if result_str else '0'


def divide_strings(dividend, divisor):
    # 将输入的字符串转换为整数
    dividend = int(dividend)
    divisor = int(divisor)

    # 处理除数为0的情况
    if divisor == 0:
        raise ValueError("除数不能为0喵")

    # 计算商和余数
    quotient = dividend // divisor
    remainder = dividend % divisor

    return quotient, remainder
