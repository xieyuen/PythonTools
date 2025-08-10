from abc import ABC, abstractmethod

from numbers import Real
from typing import Self, Optional

import pandas as pd


class Normalizer(ABC):
    """
    Normalizer 抽象基类，拥有基本的数据

    Attributes:
        data (DataFrame): 标准数据
        ddof (Real): 自由度增量，一般是 0 或 1，默认 0
    """

    def __init__(
            self,
            data: pd.DataFrame,
            ddof: Real = 0,
    ) -> None:
        """
        Args:
            data: 标准化的标准数据
            ddof: 自由度增量，默认 0
        """
        self.data = data
        self.ddof = ddof

    @property
    def max(self) -> pd.Series:
        """最大值"""
        return self.data.max()

    @property
    def min(self) -> pd.Series:
        """最小值"""
        return self.data.min()

    @property
    def std(self) -> pd.Series:
        """标准差"""
        return self.data.std(ddof=self.ddof)

    @property
    def mean(self) -> pd.Series:
        """算术平均数"""
        return self.data.mean()

    @property
    def range(self) -> pd.Series:
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
            data (DaraFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame

        Raises:
            NotImplementedError: 没实现
        """
        raise NotImplementedError


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

        公式:

        .. math::
            result = \frac{data - mean}{std}

        Returns:
            Z Score 结果 DataFrame
        """
        if data is None:
            data = self.data
        return (data - self.mean) / self.std

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            data (DaraFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame
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
            a (Real): 区间的最小值/下确界
            b (Real): 区间的最大值/上确界

        Returns:
            Self: 返回实例本身，便于链式调用

        Examples:
            >>> MinMaxNormalizer(data).set_target_range(-1,1).normalize()
        """
        self.target = a, b
        self.__check_target_range_valid()
        return self

    def normalize(self, data: Optional[pd.DataFrame] = None) -> pd.DataFrame:
        r"""
        归一化

        公式: (放缩到 [a, b])

        .. math::
            result = (b-a) \cdot \frac{data - min}{range} + a

        Returns:
            归一化结果 DataFrame
        """
        if data is None:
            data = self.data
        a, b = self.target
        return (b - a) * (data - self.min) / self.range + a

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        """
        Args:
            data (DaraFrame): 标准化后的数据

        Returns:
            反标准化后的 DataFrame
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
