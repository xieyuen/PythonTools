import unittest

from pythontools.utils.decorators import to_decorator


class TestToDecorator(unittest.TestCase):
    def test_basic_functionality(self):
        """测试 to_decorator 的基本功能"""

        # 定义一个简单的回调函数
        def callback(func, *args, **kwargs):
            result = func(*args, **kwargs)
            return result * 2

        # 使用 to_decorator 将回调函数转换为装饰器
        decorator = to_decorator(callback)

        # 定义一个目标函数
        def target_function(x):
            return x + 1

        # 应用装饰器
        decorated_function = decorator(target_function)

        # 验证装饰器是否正确工作
        self.assertEqual(decorated_function(3), 8)  # (3 + 1) * 2 = 8

    def test_argument_passing(self):
        """测试参数是否正确传递"""
        # 定义一个回调函数，记录传入的参数
        recorded_args = []
        recorded_kwargs = {}

        def callback(func, *args, **kwargs):
            recorded_args.extend(args)
            recorded_kwargs.update(kwargs)
            return func(*args, **kwargs)

        # 使用 to_decorator 将回调函数转换为装饰器
        decorator = to_decorator(callback)

        # 定义一个目标函数
        def target_function(a, b, c=3):
            return a + b + c

        # 应用装饰器
        decorated_function = decorator(target_function)

        # 调用装饰后的函数
        result = decorated_function(1, 2, c=4)

        # 验证参数是否正确传递
        self.assertEqual(result, 7)  # 1 + 2 + 4 = 7
        self.assertEqual(recorded_args, [1, 2])
        self.assertEqual(recorded_kwargs, {'c': 4})

    def test_preserve_function_metadata(self):
        """测试装饰器是否保留了目标函数的元信息"""

        # 定义一个简单的回调函数
        def callback(func, *args, **kwargs):
            return func(*args, **kwargs)

        # 使用 to_decorator 将回调函数转换为装饰器
        decorator = to_decorator(callback)

        # 定义一个带有文档字符串的目标函数
        @decorator
        def target_function():
            """This is a test function."""
            return 42

        # 验证函数名和文档字符串是否保留
        self.assertEqual(target_function.__name__, 'target_function')
        self.assertEqual(target_function.__doc__, 'This is a test function.')

    def test_exception_propagation(self):
        """测试异常是否能正确传播"""

        # 定义一个会抛出异常的回调函数
        def callback(func, *args, **kwargs):
            raise ValueError("Callback error")

        # 使用 to_decorator 将回调函数转换为装饰器
        decorator = to_decorator(callback)

        # 定义一个目标函数
        def target_function():
            return 42

        # 应用装饰器
        decorated_function = decorator(target_function)

        # 验证异常是否正确传播
        with self.assertRaises(ValueError) as context:
            decorated_function()

        self.assertEqual(str(context.exception), "Callback error")


if __name__ == '__main__':
    unittest.main()
