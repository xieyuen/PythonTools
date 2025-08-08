import unittest

import pandas as pd

from pythontools.modeling.normalization import ZScoreNormalizer, ZScoreScaler, StandardScaler


class TestZScoreNormalizer(unittest.TestCase):
    def setUp(self):
        # 创建测试数据 - 确保使用浮点数避免类型问题
        self.train_data = pd.DataFrame({
            'A': [1.0, 2.0, 3.0, 4.0, 5.0],
            'B': [10.0, 20.0, 30.0, 40.0, 50.0]
        })
        self.test_data = pd.DataFrame({
            'A': [6.0, 7.0],
            'B': [60.0, 70.0]
        })

    def test_normalize_with_training_data(self):
        """测试使用训练数据归一化"""
        normalizer = ZScoreNormalizer(self.train_data)
        normalized = normalizer.normalize()

        # 验证每列的均值为0（容差1e-7）
        pd.testing.assert_series_equal(
            normalized.mean(),
            pd.Series({'A': 0.0, 'B': 0.0}, dtype=float),
            atol=1e-7,
            check_names=False
        )

        # 验证每列的标准差为1（ddof=0）
        pd.testing.assert_series_equal(
            normalized.std(ddof=0),
            pd.Series({'A': 1.0, 'B': 1.0}, dtype=float),
            atol=1e-7,
            check_names=False
        )

    def test_normalize_with_new_data(self):
        """测试使用新数据归一化"""
        normalizer = ZScoreNormalizer(self.train_data)
        normalized = normalizer.normalize(self.test_data)

        # 手动计算预期结果
        mean_A = self.train_data['A'].mean()
        std_A = self.train_data['A'].std(ddof=0)
        mean_B = self.train_data['B'].mean()
        std_B = self.train_data['B'].std(ddof=0)

        expected = pd.DataFrame({
            'A': (self.test_data['A'] - mean_A) / std_A,
            'B': (self.test_data['B'] - mean_B) / std_B
        })

        pd.testing.assert_frame_equal(normalized, expected, atol=1e-7)

    def test_denormalize(self):
        """测试反归一化"""
        normalizer = ZScoreNormalizer(self.train_data)
        normalized = normalizer.normalize(self.test_data)
        denormalized = normalizer.denormalize(normalized)

        # 验证反归一化后数据恢复原始值
        pd.testing.assert_frame_equal(
            denormalized,
            self.test_data,
            atol=1e-7,
            check_dtype=False  # 忽略数据类型检查
        )

    def test_ddof_parameter(self):
        """测试ddof参数影响"""
        # 测试ddof=0（默认）
        normalizer0 = ZScoreNormalizer(self.train_data, ddof=0)
        std0 = normalizer0.std
        normalized0 = normalizer0.normalize(self.test_data)

        # 测试ddof=1
        normalizer1 = ZScoreNormalizer(self.train_data, ddof=1)
        std1 = normalizer1.std
        normalized1 = normalizer1.normalize(self.test_data)

        # 验证不同ddof产生不同结果
        self.assertFalse(std0.equals(std1))
        self.assertFalse(normalized0.equals(normalized1))

        # 验证反归一化都能恢复原始数据
        denormalized0 = normalizer0.denormalize(normalized0)
        denormalized1 = normalizer1.denormalize(normalized1)

        pd.testing.assert_frame_equal(
            denormalized0,
            self.test_data,
            atol=1e-7,
            check_dtype=False  # 忽略数据类型检查
        )
        pd.testing.assert_frame_equal(
            denormalized1,
            self.test_data,
            atol=1e-7,
            check_dtype=False  # 忽略数据类型检查
        )

    def test_alias_classes(self):
        """测试别名类是否等效"""
        # 创建不同名称的归一化器
        normalizer = ZScoreNormalizer(self.train_data)
        scaler = ZScoreScaler(self.train_data)
        standard_scaler = StandardScaler(self.train_data)

        # 验证归一化结果相同
        normalized1 = normalizer.normalize(self.test_data)
        normalized2 = scaler.normalize(self.test_data)
        normalized3 = standard_scaler.normalize(self.test_data)

        pd.testing.assert_frame_equal(normalized1, normalized2, atol=1e-7)
        pd.testing.assert_frame_equal(normalized1, normalized3, atol=1e-7)


if __name__ == '__main__':
    unittest.main()
