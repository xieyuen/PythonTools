import unittest
import numpy as np
from unittest.mock import Mock
from pythontools.modeling.base import std

class TestStdFunction(unittest.TestCase):
    """测试std函数的标准差计算功能"""

    def test_std_with_object_having_std_method(self):
        """测试data具有std方法的情况"""
        # 创建mock对象，模拟具有std方法的数据对象
        mock_data = Mock()
        mock_data.std = Mock(return_value=2.5)

        # 调用函数
        result = std(mock_data, ddof=1)

        # 验证mock对象的std方法被正确调用
        mock_data.std.assert_called_once_with(ddof=1)
        self.assertEqual(result, 2.5)

    def test_std_with_single_element_list(self):
        """测试长度为1的列表情况"""
        data = [5.0]
        result = std(data)
        self.assertEqual(result, 0)

    def test_std_with_multiple_elements_ddof_0(self):
        """测试多个元素且ddof=0的情况"""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        # 手动计算期望值: sqrt((1+4+9+16+25)/5 - 3^2) = sqrt(11-9) = sqrt(2)
        expected = np.sqrt(2)
        result = std(data, ddof=0)
        self.assertAlmostEqual(result, expected, places=10)

    def test_std_with_multiple_elements_ddof_1(self):
        """测试多个元素且ddof=1的情况"""
        data = [1.0, 2.0, 3.0, 4.0, 5.0]
        # 手动计算期望值: sqrt((1+4+9+16+25)/4 - 3^2) = sqrt(13.75-9) = sqrt(4.75)
        expected = np.sqrt(4.75)
        result = std(data, ddof=1)
        self.assertAlmostEqual(result, expected, places=10)

    def test_std_with_tuple_data(self):
        """测试元组作为输入数据的情况"""
        data = (2.0, 4.0, 6.0)
        # 手动计算期望值: sqrt((4+16+36)/3 - 4^2) = sqrt(18.67-16) = sqrt(2.67)
        expected = np.sqrt(56/3 - 16)
        result = std(data)
        self.assertAlmostEqual(result, expected, places=10)

    def test_std_with_numpy_array(self):
        """测试numpy数组作为输入（会走mock分支）"""
        # 由于numpy数组有std方法，会调用其std方法
        data = np.array([1.0, 2.0, 3.0])
        result = std(data)
        # numpy的默认ddof是0，所以结果应该与numpy计算一致
        expected = np.std(data, ddof=0)
        self.assertAlmostEqual(result, expected, places=10)

    def test_std_empty_list_raises_exception(self):
        """测试空列表应该抛出异常"""
        data = []
        with self.assertRaises(Exception):
            std(data)

    def test_std_with_non_numeric_data_raises_exception(self):
        """测试包含非数值数据应该抛出异常"""
        data = ['a', 'b', 'c']
        with self.assertRaises(Exception):
            std(data)

if __name__ == '__main__':
    unittest.main()
