import functools
import time
from numbers import Integral
from typing import Callable, Generator

from pythontools.types.utils import GeneratorResult


def to_decorator(callback: Callable) -> Callable:
    """把一个函数变成装饰器

    Args:
        callback (Callable):
            回调函数，接受 ``func, *args, **kwargs``,
            其中 ``*args`` 和 ``**kwargs`` 是 ``func`` 的运行参数

    Returns:
        Callable: 直接可 @ 的装饰器

    Examples:
        >>> @to_decorator
        ... def print_result(func, *args, **kwargs)
        ...     result = func(*args, **kwargs)
        ...     print(f"result: {result}")
        ...     return result
        >>> @print_result
        ... def add(a, b):
        ...     return a + b
        >>> add(1, 2)
        result: 3
        3
    """

    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            return callback(func, *args, **kwargs)

        return wrapper

    return dec


def retry(
        times: int = 3,
        delay: float = 1,
        error: type(Exception) | tuple[type(Exception)] = Exception
) -> Callable:
    """当函数在被调用时抛出指定错误后重试

    Args:
        times: 重试次数
        delay: 每次重试之间的等待时间，单位为秒
        error: 遇到设定的错误才重试

    Raises:
        ValueError: 等待时间需为正
        ValueError: 重复次数需为正
        TypeError: 重复次数需为整数
    """

    if callable(times):
        return retry()(times)

    if delay < 0:
        raise ValueError("等待时间需为正")
    if not isinstance(times, Integral):
        raise TypeError("重复次数需为整数")
    if times < 0:
        raise ValueError("重复次数需为正")

    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            for i in range(1, times + 1):
                try:
                    return func(*args, **kwargs)
                except error:
                    if i == times:
                        raise
                    time.sleep(delay)
                    continue
            assert False, "不可能运行到这里"

        return wrapper

    return dec


def timer(formatter: str = "{name} 运行用时: {time}", printer=print):
    """计时器"""
    if callable(formatter):
        return timer()(formatter)

    def dec(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            printer(formatter.format(name=func.__name__, time=end - start))
            return result

        return wrapper

    return dec


'''
R = TypeVar("R")


@overload
def run(func: Callable[..., R]) -> R: ...


@overload
def run(func: Generator[R]) -> R: ...


@overload
def run(*args, **kwargs) -> Callable[[Callable[..., R]], R]: ...


@overload
def run(*args, **kwargs) -> Callable[[Generator[R]], R]: ...


def run(*args, **kwargs):
    """立即执行
    Args:
        *args: 被装饰函数的位置参数
                 如果直接 ``@run`` 不传参也鞥识别
        **kwargs: 被装饰函数的关键字参数
    
    Returns:
        Callable[[Callable[..., R]], R]: 接受函数后传参运行
    
    Examples:
        >>> @run
        ... def lst():
        ...     res = []
        ...     for i in range(10):
        ...         res.append(i)
        ...     return res
        >>> lst
        [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
        
        >>> @run(1, 2, c=4)
        ... def add_result(a, b, c):
        ...     return a + b + c
        >>> add_result
        7
        
        >>> @run(lambda *_, **_:None, 5)
        ... def lst2(f, x):
        ...     for i in range(1, x + 1):
        ...         yield f(i)
        >>> lst2
    """
    # 兼容 @run
    if not kwargs and len(args) == 1 and callable(args[0]):
        return args[0]()

    def wrapper(func):
        return func(*args, **kwargs)

    return wrapper
'''


class run:
    @classmethod
    def __new__(cls, *args, **kwargs):
        if not kwargs and len(args) == 1 and callable(args[0]):
            return run()(args[0])
        self = super().__new__(cls)
        self.__init__(*args, **kwargs)
        return self

    def __init__(self, *args, **kwargs):
        self.arguments = args, kwargs

    def __call__(self, func):
        self.is_generator = isinstance(func, Generator)
        self.result = func(*self.arguments[0], **self.arguments[1])
        return self.result if not self.is_generator else self

    def __next__(self):
        return self.next()

    def __iter__(self):
        if not self.is_generator:
            raise TypeError("不是生成器")
        return self

    def next(self):
        try:
            return GeneratorResult(next(self.result), done=False)
        except StopIteration:
            return GeneratorResult(None, done=True)

    def is_done(self):
        if not self.is_generator:
            raise TypeError("不是生成器")
