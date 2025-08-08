import unittest
import numpy as np
from pythontools.modeling.base import mean

class TestMeanFunction(unittest.TestCase):

    def test_mean_with_numpy_array(self):
        """测试传入numpy数组的情况 - 应该调用数组的mean方法"""
        # 创建numpy数组
        data = np.array([1, 2, 3, 4, 5])
        # 调用函数
        result = mean(data)
        # 验证结果 - numpy数组有自己的mean方法
        expected = 3.0
        self.assertEqual(result, expected)

    def test_mean_with_list(self):
        """测试传入Python列表的情况 - 应该使用np.sum和len计算"""
        # 创建Python列表
        data = [1, 2, 3, 4, 5]
        # 调用函数
        result = mean(data)
        # 验证结果
        expected = 3.0
        self.assertEqual(result, expected)

    def test_mean_with_tuple(self):
        """测试传入元组的情况 - 应该使用np.sum和len计算"""
        # 创建元组
        data = (1, 2, 3, 4, 5)
        # 调用函数
        result = mean(data)
        # 验证结果
        expected = 3.0
        self.assertEqual(result, expected)

    def test_mean_with_custom_object_having_mean(self):
        """测试传入自定义具有mean方法的对象"""
        # 创建一个模拟具有mean方法的对象
        class MockObject:
            def mean(self):
                return 10.5

        data = MockObject()
        # 调用函数
        result = mean(data)
        # 验证结果 - 应该调用对象的mean方法
        expected = 10.5
        self.assertEqual(result, expected)

    def test_mean_with_single_element_list(self):
        """测试单元素列表的边界情况"""
        data = [5]
        result = mean(data)
        expected = 5.0
        self.assertEqual(result, expected)

    def test_mean_with_negative_numbers(self):
        """测试包含负数的情况"""
        data = [-2, -1, 0, 1, 2]
        result = mean(data)
        expected = 0.0
        self.assertEqual(result, expected)

    def test_mean_with_float_numbers(self):
        """测试浮点数的情况"""
        data = [1.5, 2.5, 3.5]
        result = mean(data)
        expected = 2.5
        self.assertEqual(result, expected)

if __name__ == '__main__':
    unittest.main()
