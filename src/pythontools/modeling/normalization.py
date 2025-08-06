from abc import ABC, abstractmethod
from typing import Self, Literal

import numpy as np
import pandas as pd


class Normalizer(ABC):
    def __init__(self, data: pd.DataFrame, ddof: Literal[0, 1] = 0, *args, **kwargs) -> None:
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

    @abstractmethod
    def denormalize(self, data: pd.DataFrame) -> pd.DataFrame:
        raise NotImplementedError


class ZScoreNormalizer(Normalizer):
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

    Example:
        >>> data = pd.DataFrame({
        ...     "A": [1, 2, 3],
        ...     "B": [4, 5, 6],
        ... })
        >>> normalizer = MinMaxNormalizer(data, (0, 1))
        >>> normalizer.normalize()
            A   B
        1   0   0
        2   0.5 0.5
        3   1   1
    """

    def __init__(self, data: pd.DataFrame, target_range: tuple[np.number, np.number] = (0, 1)):
        super().__init__(data)
        self.target: tuple[np.number, np.number] = target_range
        assert self.__is_target_range_valid(), "Target range is not valid"

    def __is_target_range_valid(self):
        return self.target[0] < self.target[1]

    def set_target_range(self, a: np.number, b: np.number) -> Self:
        self.target = a, b
        assert self.__is_target_range_valid(), "Target range is not valid"
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
