import unittest

from pythontools.utils.math import Interval  # 假设代码保存在interval.py中


class TestInterval(unittest.TestCase):
    """Interval类的单元测试"""

    def test_init_normal_interval(self):
        """测试正常区间的初始化"""
        interval = Interval(1, 5)
        self.assertEqual(interval.interval, (1, 5))
        self.assertEqual(interval.closed, (True, True))
        self.assertFalse(interval.is_empty)

    def test_init_empty_interval(self):
        """测试空区间的初始化"""
        interval = Interval(3, 3, (False, False))
        self.assertEqual(interval.interval, (3, 3))
        self.assertTrue(interval.is_empty)

    def test_init_invalid_interval(self):
        """测试无效区间的初始化（应抛出异常）"""
        with self.assertRaises(ValueError) as context:
            Interval(5, 1)
        self.assertIn("Invalid interval", str(context.exception))

    def test_init_with_different_closure(self):
        """测试不同闭包类型的初始化"""
        # 开区间
        interval = Interval(1, 5, (False, False))
        self.assertEqual(interval.closed, (False, False))

        # 左闭右开
        interval = Interval(1, 5, (True, False))
        self.assertEqual(interval.closed, (True, False))

        # 左开右闭
        interval = Interval(1, 5, (False, True))
        self.assertEqual(interval.closed, (False, True))

    def test_eq_with_same_intervals(self):
        """测试相同区间的相等性"""
        interval1 = Interval(1, 5)
        interval2 = Interval(1, 5)
        self.assertEqual(interval1, interval2)

    def test_eq_with_empty_intervals(self):
        """测试空区间的相等性"""
        interval1 = Interval(3, 3)
        interval2 = Interval(3, 3)
        self.assertEqual(interval1, interval2)

    def test_eq_with_different_intervals(self):
        """测试不同区间的相等性"""
        interval1 = Interval(1, 5)
        interval2 = Interval(2, 6)
        self.assertNotEqual(interval1, interval2)

    def test_eq_with_empty_and_non_empty(self):
        """测试空区间与非空区间的相等性"""
        empty_interval = Interval(1, 1)
        normal_interval = Interval(1, 2)
        self.assertNotEqual(empty_interval, normal_interval)

    def test_eq_with_same_values_different_closure(self):
        """测试相同值但不同闭包的区间相等性"""
        interval1 = Interval(1, 5, (True, True))  # [1, 5]
        interval2 = Interval(1, 5, (False, False))  # (1, 5)
        self.assertNotEqual(interval1, interval2)

    def test_gt_with_containing_interval(self):
        """测试包含关系的大于比较"""
        outer = Interval(1, 5)  # [1, 5]
        inner = Interval(2, 4)  # [2, 4]
        self.assertGreater(outer, inner)

    def test_gt_with_empty_interval(self):
        """测试空区间的大于比较"""
        empty = Interval(1, 1)  # []
        normal = Interval(1, 5)  # [1, 5]
        self.assertGreater(normal, empty)

    def test_gt_with_same_interval_different_closure(self):
        """测试相同区间但不同闭包的大于比较"""
        closed = Interval(1, 5, (True, True))  # [1, 5]
        open = Interval(1, 5, (False, False))  # (1, 5)
        self.assertGreater(closed, open)

    def test_lt_with_contained_interval(self):
        """测试被包含关系的小于比较"""
        inner = Interval(2, 4)  # [2, 4]
        outer = Interval(1, 5)  # [1, 5]
        self.assertLess(inner, outer)

    def test_lt_with_empty_interval(self):
        """测试空区间的小于比较"""
        empty = Interval(1, 1)  # []
        normal = Interval(1, 5)  # [1, 5]
        self.assertLess(empty, normal)

    def test_ge_le_operators(self):
        """测试>=和<=操作符"""
        interval1 = Interval(1, 5)
        interval2 = Interval(2, 4)
        interval3 = Interval(1, 5)

        # 包含关系
        self.assertGreaterEqual(interval1, interval2)
        self.assertLessEqual(interval2, interval1)

        # 相等关系
        self.assertGreaterEqual(interval1, interval3)
        self.assertLessEqual(interval1, interval3)

    def test_contains_with_number_in_closed_interval(self):
        """测试数字在闭区间内的包含关系"""
        interval = Interval(1, 5)
        self.assertIn(3, interval)
        self.assertIn(1, interval)  # 端点
        self.assertIn(5, interval)  # 端点

    def test_contains_with_number_in_open_interval(self):
        """测试数字在开区间内的包含关系"""
        interval = Interval(1, 5, (False, False))  # (1, 5)
        self.assertIn(3, interval)
        self.assertNotIn(1, interval)  # 开端点
        self.assertNotIn(5, interval)  # 开端点

    def test_contains_with_number_at_half_open_endpoints(self):
        """测试半开区间的端点包含关系"""
        interval = Interval(1, 5, (True, False))  # [1, 5)
        self.assertIn(1, interval)  # 闭端点
        self.assertNotIn(5, interval)  # 开端点

    def test_contains_with_empty_interval(self):
        """测试空区间对数字的包含关系"""
        empty = Interval(3, 3, (False, False))
        self.assertNotIn(3, empty)

    def test_contains_with_interval(self):
        """测试区间对区间的包含关系"""
        outer = Interval(1, 5)  # [1, 5]
        inner = Interval(2, 4)  # [2, 4]
        same = Interval(1, 5)  # [1, 5]

        self.assertIn(inner, outer)
        self.assertIn(same, outer)

    def test_repr_output(self):
        """测试字符串表示"""
        # 闭区间
        closed = Interval(1, 5)
        self.assertEqual(repr(closed), "[1, 5]")

        # 开区间
        open_interval = Interval(1, 5, (False, False))
        self.assertEqual(repr(open_interval), "(1, 5)")

        # 左闭右开
        left_closed = Interval(1, 5, (True, False))
        self.assertEqual(repr(left_closed), "[1, 5)")

        # 左开右闭
        right_closed = Interval(1, 5, (False, True))
        self.assertEqual(repr(right_closed), "(1, 5]")

    def test_edge_cases(self):
        """测试边界情况"""
        # 负数区间
        negative = Interval(-5, -1)
        self.assertIn(-3, negative)

        # 包含零的区间
        zero_included = Interval(-1, 1)
        self.assertIn(0, zero_included)

        # 单点闭区间
        single_point = Interval(2, 2, (True, True))
        self.assertFalse(single_point.is_empty)  # 实际上不应该是空的


if __name__ == '__main__':
    unittest.main()
