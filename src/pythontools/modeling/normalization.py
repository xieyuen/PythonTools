from abc import ABC, abstractmethod
from functools import cached_property
from numbers import Real
from typing import Self, Literal, Optional

import pandas as pd


class Normalizer(ABC):
    """
    Normalizer 抽象基类，拥有基本的数据
    """

    def __init__(
            self,
            data: pd.DataFrame,
            ddof: Literal[0, 1] = 0,
    ) -> None:
        """
        Args:
            data: 标准化的标准数据
            ddof: 自由度增量，默认 0
        """
        if not isinstance(data, pd.DataFrame):
            raise NotImplementedError("暂不支持 data 不是 pandas DataFrame 的情形")

        self.__data = data
        self.__ddof = ddof

    @property
    def ddof(self) -> Literal[0, 1]:
        """自由度增量"""
        return self.__ddof

    def set_ddof(self, ddof: Literal[0, 1]):
        """设置自由度增量

        一般是 0 或 1

        Args:
            ddof (Literal[0, 1]): 自由度增量
        """
        self.__ddof = ddof

    @cached_property
    def max(self) -> pd.Series[Real]:
        """最大值"""
        return self.__data.max()

    @cached_property
    def min(self) -> pd.Series[Real]:
        """最小值"""
        return self.__data.min()

    @cached_property
    def std(self) -> pd.Series[Real]:
        """标准差"""
        return self.__data.std(ddof=self.ddof)

    @cached_property
    def mean(self) -> pd.Series[Real]:
        """算术平均数"""
        return self.__data.mean()

    @cached_property
    def range(self) -> pd.Series[Real]:
        """极差"""
        return self.max - self.min

    @abstractmethod
    def normalize(self, data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        """
        标准化

        Args:
            data (Optional[DataFrame]): 需要标准化的数据
        Returns:
            返回数据标准化后的 DataFrame
        """
        raise NotImplementedError

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        反标准化

        可以不实现

        Args:
            data (DataFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame

        Raises:
            NotImplementedError: 没实现
        """
        raise NotImplementedError

    def transform(self, data: pd.DataFrame) -> pd.DataFrame:
        """``normalize`` 的别名"""
        return self.normalize(data)

    @classmethod
    def fit_transform(cls, data: pd.DataFrame, *args, **kwargs) -> pd.DataFrame:
        """使用 data 训练并返回标准化后的数据

        Args:
            data (DataFrame): 训练数据
            *args: 其他参数
            **kwargs: 其他参数

        Returns:
            标准化后的数据
        """
        return cls(data, *args, **kwargs).normalize()


class ZScoreNormalizer(Normalizer):
    """
    Z-Score 标准化

    Example:
        >>> data = pd.DataFrame({
        ...     "A": [1, 2, 3],
        ...     "B": [4, 5, 6],
        ...     "C": [2, 4, 6],
        ... })
        >>> normalizer = ZScoreNormalizer(data)
        >>> normalizer.normalize()
            A   B   C
        1  -1  -1  -1
        2   0   0   0
        3   1   1   1
    """

    def normalize(self, data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        r"""Z Score 标准化

        特殊情况:
        1. 常数列(标准差为 0)：标准化为 0
        2. 空数据：返回空数据

        公式:

        .. math::
            result = \frac{data - mean}{std}

        Returns:
            Z Score 结果 DataFrame
        """
        if data is None:
            data = self.__data

        if not isinstance(data, pd.DataFrame):
            raise NotImplementedError("暂不支持 data 不是 pandas DataFrame 的情形")
        if data.empty:
            return data

        # 处理标准差为0的情况，避免除零错误
        std = self.std
        mean = self.mean
        result = data.copy()

        # 对于标准差为0的列，标准化结果设为0
        zero_std_columns = std == 0
        if zero_std_columns.any():
            result.loc[:, zero_std_columns] = 0
            # 对于标准差非0的列，正常进行Z-Score标准化
            nonzero_std_columns = ~zero_std_columns
            if nonzero_std_columns.any():
                result.loc[:, nonzero_std_columns] = (
                        (data.loc[:, nonzero_std_columns] - mean[nonzero_std_columns])
                        / std[nonzero_std_columns]
                )
        else:
            # 所有列都正常进行Z-Score标准化
            result = (data - mean) / std

        return result

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            data (DataFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame，常数列不能得到原数据
        """
        return data * self.std + self.mean


ZScoreScaler = StandardScaler = ZScoreNormalizer


class MinMaxNormalizer(Normalizer):
    """把数据归一化到 [a,b]

    Attributes:
        target (tuple[Real, Real]): 放缩区间

    Example:
        >>> data = pd.DataFrame({
        ...     "A": [1, 2, 3],
        ...     "B": [4, 5, 6],
        ...     "C": [2, 4, 6],
        ... })
        >>> normalizer = MinMaxNormalizer(data, target_range=(0, 1))
        >>> # 或者 normalizer = MinMaxNormalizer(data).set_target_range(0, 1)
        >>> normalizer.normalize()
            A   B   C
        1   0   0   0
        2  0.5 0.5 0.5
        3   1   1   1
    """

    def __init__(
            self,
            data: pd.DataFrame,
            target_range: tuple[Real, Real] = (0, 1),
            *args, **kwargs
    ):
        """
        Args:
            data: 数据
            target_range (tuple[Real, Real]): 目标闭区间
            *args: 传给 Normalizer 的参数
            **kwargs: 传给 Normalizer 的参数
        """
        super().__init__(data, *args, **kwargs)
        self.target: tuple[Real, Real] = target_range
        self.__check_target_range_valid()

    def __check_target_range_valid(self) -> None:
        """
        检查放缩范围的有效性

         Raises:
             TypeError: 输入不是实数
             ValueError: 无效的范围: [a, b]
        """
        if any(not isinstance(x, Real) for x in self.target):
            raise TypeError("输入不是实数")
        if self.target[0] >= self.target[1]:
            raise ValueError(f"无效的范围: {list(self.target)}")

    def set_target_range(self, a: Real, b: Real) -> Self:
        """
        设置放缩的闭区间

        Args:
            a (Real): 区间的最小值
            b (Real): 区间的最大值

        Returns:
            Self: 返回实例本身，便于链式调用

        Examples:
            >>> MinMaxNormalizer(pd.DataFrame()).set_target_range(-1,1).normalize()
        """
        self.target = a, b
        self.__check_target_range_valid()
        return self

    def normalize(self, data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        r"""归一化

        特殊情况:
            常数列(极差为 0)：归一化为区间中点

        公式: (放缩到 [a, b])

        .. math::
            result = (b-a) \cdot \frac{data - min}{range} + a

        Returns:
            归一化结果 DataFrame
        """
        if data is None:
            data = self.__data
        a, b = self.target

        # 处理极差为0的情况，避免除零错误
        range_val = self.range
        min_val = self.min
        result = data.copy()

        # 对于极差为0的列，归一化结果设为目标区间的中点
        zero_range_columns = range_val == 0
        if zero_range_columns.any():
            midpoint = (a + b) / 2
            result.loc[:, zero_range_columns] = midpoint
            # 对于极差非0的列，正常进行MinMax标准化
            nonzero_range_columns = ~zero_range_columns
            if nonzero_range_columns.any():
                result.loc[:, nonzero_range_columns] = (
                        (b - a) * (data.loc[:, nonzero_range_columns] - min_val[nonzero_range_columns])
                        / range_val[nonzero_range_columns] + a
                )
        else:
            # 所有列都正常进行MinMax标准化
            result = (b - a) * (data - min_val) / range_val + a

        return result

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            data (DataFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame，常数列不能得到原数据
        """
        a, b = self.target
        return (data - a) * self.range / (b - a) + self.min


MinMaxScaler = MinMaxNormalizer

__all__ = [
    # Base class
    "Normalizer",

    # Z-Score normalizers (all are the same)
    "ZScoreNormalizer", "ZScoreScaler", "StandardScaler",

    # Min-Max normalizers (all are the same)
    "MinMaxNormalizer", "MinMaxScaler",
]
