import unittest
from unittest.mock import patch

from pythontools.utils.decorators import retry


class TestRetryDecorator(unittest.TestCase):

    def test_delay_negative_raises_value_error(self):
        """测试 delay 为负数时抛出 ValueError"""
        with self.assertRaises(ValueError):
            retry(delay=-1)

    def test_times_not_integer_raises_type_error(self):
        """测试 times 为非整数时抛出 TypeError"""
        with self.assertRaises(TypeError):
            retry(times=3.5)

    def test_times_negative_raises_value_error(self):
        """测试 times 为负数时抛出 ValueError"""
        with self.assertRaises(ValueError):
            retry(times=-1)

    def test_times_callable_returns_decorator(self):
        """测试 times 为可调用对象时返回装饰器"""

        @retry()
        def dummy_func():
            return "success"

        self.assertEqual(dummy_func(), "success")

    @patch('time.sleep')
    def test_function_success_no_retry(self, mock_sleep):
        """测试函数调用成功时不进行重试"""

        @retry(times=3, delay=1)
        def success_func():
            return "success"

        self.assertEqual(success_func(), "success")
        mock_sleep.assert_not_called()

    @patch('time.sleep')
    def test_function_failure_retries_and_raises(self, mock_sleep):
        """测试函数调用失败且达到最大重试次数时抛出异常"""

        @retry(times=3, delay=1)
        def fail_func():
            raise ValueError("failure")

        with self.assertRaises(ValueError):
            fail_func()
        self.assertEqual(mock_sleep.call_count, 2)  # 重试2次，每次等待1秒

    @patch('time.sleep')
    def test_function_failure_retries_and_succeeds(self, mock_sleep):
        """测试函数调用失败但未达到最大重试次数时成功"""
        call_count = 0

        @retry(times=3, delay=1)
        def fail_then_success_func():
            nonlocal call_count
            call_count += 1
            if call_count < 3:
                raise ValueError("failure")
            return "success"

        self.assertEqual(fail_then_success_func(), "success")
        self.assertEqual(mock_sleep.call_count, 2)  # 重试2次，每次等待1秒

    @patch('time.sleep')
    def test_function_raises_unspecified_error_no_retry(self, mock_sleep):
        """测试函数抛出非指定异常时不进行重试"""

        @retry(times=3, delay=1, error=TypeError)
        def fail_func():
            raise ValueError("failure")

        with self.assertRaises(ValueError):
            fail_func()
        mock_sleep.assert_not_called()


if __name__ == '__main__':
    unittest.main()
