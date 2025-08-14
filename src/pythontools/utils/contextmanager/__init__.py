import time
import functools


class Timer:
    def __init__(self, formatter: str = "运行用时: {time}", printer=print, *, allow_decorator=False, **kwargs):
        if callable(formatter):
            raise TypeError(f"{self.__class__.__name__} 需要配置")
        self.formatter = formatter
        self.printer = printer
        self.arguments = kwargs
        self.__allow_decorator = allow_decorator

    def __call__(self, func):  # for decorator when allowed
        if not self.__allow_decorator:
            raise TypeError(f"'{self.__class__.__name__}' object is not callable")

        @functools.wraps(func)
        def wrapper(*args, **kwargs):
            start = time.perf_counter()
            result = func(*args, **kwargs)
            end = time.perf_counter()
            self.printer(self.formatter.format(name=func.__name__, time=end - start))
            return result

        return wrapper

    def __enter__(self):
        self.start = time.perf_counter()
        return self

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.end = time.perf_counter()
        self.printer(self.formatter.format(**self.arguments, time=self.end - self.start))

    def used(self):
        return time.perf_counter() - self.start
