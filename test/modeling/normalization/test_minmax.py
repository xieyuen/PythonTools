import unittest

import pandas as pd

from pythontools.modeling.normalization import MinMaxNormalizer


class TestMinMaxNormalizer(unittest.TestCase):
    def test_init_default_range(self):
        """Test initialization with default target range"""
        data = pd.DataFrame({'A': [1, 2, 3]})
        normalizer = MinMaxNormalizer(data)
        self.assertEqual(normalizer.target, (0, 1))

    def test_init_custom_range(self):
        """Test initialization with custom target range"""
        data = pd.DataFrame({'A': [1, 2, 3]})
        normalizer = MinMaxNormalizer(data, target_range=(-1, 1))
        self.assertEqual(normalizer.target, (-1, 1))

    def test_set_target_range(self):
        """Test set_target_range method"""
        data = pd.DataFrame({'A': [1, 2, 3]})
        normalizer = MinMaxNormalizer(data)
        normalizer.set_target_range(-2, 2)
        self.assertEqual(normalizer.target, (-2, 2))

    def test_normalize_default_data_default_range(self):
        """Test normalization with default data and default range"""
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8]})
        normalizer = MinMaxNormalizer(data)
        normalized = normalizer.normalize()

        expected = pd.DataFrame({
            'A': [0.0, 0.5, 1.0],
            'B': [0.0, 0.5, 1.0]
        })
        pd.testing.assert_frame_equal(normalized, expected, check_dtype=False)

    def test_normalize_default_data_custom_range(self):
        """Test normalization with default data and custom range"""
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8]})
        normalizer = MinMaxNormalizer(data, target_range=(-1, 1))
        normalized = normalizer.normalize()

        expected = pd.DataFrame({
            'A': [-1.0, 0.0, 1.0],
            'B': [-1.0, 0.0, 1.0]
        })
        pd.testing.assert_frame_equal(normalized, expected, check_dtype=False)

    def test_round_trip(self):
        """Test normalization + denormalization returns original data"""
        data = pd.DataFrame({
            'A': [1, 2, 3, 4, 5],
            'B': [10, 20, 30, 40, 50],
            'C': [0.1, 0.2, 0.3, 0.4, 0.5]
        })

        # Test different target ranges
        for target_range in [(0, 1), (-1, 1), (0, 100), (-5, 5)]:
            with self.subTest(target_range=target_range):
                normalizer = MinMaxNormalizer(data, target_range=target_range)
                normalized = normalizer.normalize()
                denormalized = normalizer.denormalize(normalized)

                # Use pandas testing with tolerance and dtype check disabled
                pd.testing.assert_frame_equal(
                    denormalized,
                    data,
                    check_exact=False,
                    atol=1e-10,
                    rtol=1e-10,
                    check_dtype=False
                )

    def test_normalize_new_data(self):
        """Test normalization with new data"""
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8]})
        normalizer = MinMaxNormalizer(data)
        new_data = pd.DataFrame({'A': [0, 4], 'B': [2, 10]})
        normalized = normalizer.normalize(new_data)

        expected = pd.DataFrame({
            'A': [-0.5, 1.5],
            'B': [-0.5, 1.5]
        })
        pd.testing.assert_frame_equal(normalized, expected, check_dtype=False)

    def test_denormalize_default_range(self):
        """Test denormalization with default range"""
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8]})
        normalizer = MinMaxNormalizer(data)

        # Create normalized data directly
        normalized_data = pd.DataFrame({
            'A': [0.0, 0.5, 1.0],
            'B': [0.0, 0.5, 1.0]
        })

        denormalized = normalizer.denormalize(normalized_data)

        pd.testing.assert_frame_equal(
            denormalized,
            data,
            check_exact=False,
            atol=1e-10,
            rtol=1e-10,
            check_dtype=False
        )

    def test_denormalize_custom_range(self):
        """Test denormalization with custom range"""
        data = pd.DataFrame({'A': [1, 2, 3], 'B': [4, 6, 8]})
        normalizer = MinMaxNormalizer(data, target_range=(-1, 1))

        # Create normalized data directly
        normalized_data = pd.DataFrame({
            'A': [-1.0, 0.0, 1.0],
            'B': [-1.0, 0.0, 1.0]
        })

        denormalized = normalizer.denormalize(normalized_data)

        pd.testing.assert_frame_equal(
            denormalized,
            data,
            check_exact=False,
            atol=1e-10,
            rtol=1e-10,
            check_dtype=False
        )


if __name__ == '__main__':
    unittest.main()
