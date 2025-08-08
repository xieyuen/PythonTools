from abc import ABC, abstractmethod

from numbers import Real
from typing import Self, Literal


import numpy as np
import pandas as pd


class Normalizer(ABC):
    """
    Normalizer 抽象基类，不能直接使用，在实现 normalize() 后可用

    denormalize() 默认不定义，不重写直接调用会报 NotImplementedError

    Args:
        data (DataFrame): 标准化的标准数据
        ddof (Literal[0, 1]): 是否为无偏估计(主要决定标准差的计算方式)，默认为 0
    """

    def __init__(
            self,
            data: pd.DataFrame,
            ddof: Literal[0, 1] = 0,
            *args, **kwargs
    ) -> None:
        self.data = data
        self.ddof = ddof

    @property
    def max(self) -> pd.Series:
        return self.data.max()

    @property
    def min(self) -> pd.Series:
        return self.data.min()

    @property
    def std(self) -> pd.Series:
        return self.data.std(ddof=self.ddof)

    @property
    def mean(self) -> pd.Series:
        return self.data.mean()

    @property
    def range(self) -> pd.Series:
        return self.max - self.min

    @abstractmethod
    def normalize(self, data: pd.DataFrame | None = None) -> pd.DataFrame:
        raise NotImplementedError

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError


class ZScoreNormalizer(Normalizer):
    """
    Z-Score 标准化
    Args:
        data (DataFrame): 标准化的标准数据
        ddof (Literal[0, 1]): 是否为无偏估计(主要决定标准差的计算方式)，默认为 0

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

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

    def normalize(self, data: pd.DataFrame | None = None) -> pd.DataFrame:
        if data is None:
            data = self.data
        return (data - self.mean) / self.std

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        return data * self.std + self.mean


ZScoreScaler = StandardScaler = ZScoreNormalizer


class MinMaxNormalizer(Normalizer):
    """
    把数据归一化到 [a,b]
    Args:
        data (DataFrame): 标准化的标准数据
        ddof (Literal[0, 1]): 是否为无偏估计(主要决定标准差的计算方式)，默认为 0
        target_range (tuple[Real, Real]): 放缩的目标闭区间，默认 [0, 1]

    Example:
        >>> data = pd.DataFrame({
        ...     "A": [1, 2, 3],
        ...     "B": [4, 5, 6],
        ...     "C": [2, 4, 6],
        ... })
        >>> normalizer = MinMaxNormalizer(data, target_range=(0, 1))
        >>> normalizer.normalize()
            A   B   C
        1   0   0   0
        2  0.5 0.5 0.5
        3   1   1   1
    """

    def __init__(
            self,
            data: pd.DataFrame,
            ddof: Literal[0, 1] = 0,
            target_range: tuple[Real, Real] = (0, 1),
            *args, **kwargs
    ):
        super().__init__(data, ddof, *args, **kwargs)
        self.target: tuple[Real, Real] = target_range
        self.__check_target_range_valid()

    def __check_target_range_valid(self):
        if any(not isinstance(x, Real) for x in self.target):
            raise TypeError("Target range must be a tuple of two real numbers")
        if self.target[0] >= self.target[1]:
            raise ValueError(f"Invalid target range: {list(self.target)}")

    def set_target_range(self, a: Real, b: Real) -> Self:
        self.target = a, b
        self.__check_target_range_valid()
        return self

    def normalize(self, data: pd.DataFrame | None = None) -> pd.DataFrame:
        if data is None:
            data = self.data
        a, b = self.target
        return (b - a) * (data - self.min) / self.range + a

    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
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
