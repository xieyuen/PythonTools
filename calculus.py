# Calculus
import time

from math import *
# from BetterPrint import bPrint

'''
    python 计算微积分（
    这个类里面所有的方法都有精度 n (默认为 2 ** 25 )
    由于微积分需要用到极限，但在 python 中无法实现极限运算，故选择一个大数以模拟极限情况.
    可以在参数末尾加入 `n = 一个整数` 以改变精度
    注意：n越大，计算时间越久！
    导入时建议使用这个：
    >>> from calculus import Calculus
    >>> calculus = Calculus()
'''

class Calculus:

    '''
        python 计算微积分（
        这个类里面所有的方法都有精度 n (默认为 2 ** 25 )
        由于微积分需要用到极限，但在 python 中无法实现极限运算，故选择一个大数以模拟极限情况.
        可以在参数末尾加入 `n = 一个整数` 以改变精度
        注意：n越大，计算时间越久！
        导入时建议使用这个：
        >>> from calculus import Calculus
        >>> calculus = Calculus()
    '''

    def __init__(self, func: callable = sin):
        self.func: callable = func

    def definite_integral(self, a, b, f = self.func, n = 2 ** 25):
        '''
            定积分/黎曼积分

            使用方法:
            >>> definite_integral(lambda x: 关于x的函数表达式, 积分下限, 积分上限, 精度)
        '''
        __dx = (b - a) / n
        __y = 0
        return self.sum(lambda x: __dx * f(a + x * __dx), 0, n)


    def derivative(self, x, f = self.func, n = 2 ** 25):
        '''
            导数/微分
            在函数上某点的导数值

            使用方法:
            >>> derivative(点的横坐标, lambda x: 关于x的函数表达式, 精度)
        '''
        __dx = 1 / n
        __dy1 = f(x + __dx) - f(x)
        __dy2 = f(x) - f(x - __dx)
        __dy = (__dy1 + __dy2) / 2
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


    def tangent_line(self, x, f = self.func, n = 2 ** 25):
        '''
            函数 f(x) 在点 (x, f(x)) 处的切线方程

            使用方法:
            >>> tangent_line(切点横坐标, lambda x: 关于x的函数表达式, 精度)
        '''
        __k = self.derivative(f, x, n)
        __m = f(x) - __k * x
        __result = {
            "斜率": __k,
            "y轴截距": __m,
            '直线方程': f'y={__k}x+{__m}'
        }
        return __result


    def normal_line(self, x, f = self.func, n = 2 ** 25):
        '''
            函数 f(x) 在点 (x, f(x)) 处切线的法线方程

            使用方法:
            >>> normal_line(切点横坐标, lambda x: 关于x的函数表达式, 精度)
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


# 测试
if __name__ == '__main__':
    def test(f):
        cal = Calculus()
        print(cal.definite_integral(f, 1, 10))
        print(cal.derivative(f, 1, 10))
        print(cal.convexity(f, 1, 10))
        print(cal.tangent_line(f, 1, 10))
        print(cal.normal_line(f, 1, 10))
        print(cal.sum(f, 1, 10))
        print()

    test(lambda x: 1 / x)
    test(lambda x: x ** 2)
    test(lambda x: exp(x))
    test(lambda x: sin(x))
    test(lambda x: cos(x))
    test(lambda x: sqrt(x))
    test(lambda x: log(x))
    test(lambda x: sqrt(x))
    test(lambda x: x)
