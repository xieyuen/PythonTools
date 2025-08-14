from typing import Protocol
from numbers import Real

import numpy as np
from pandas import DataFrame


class Model(Protocol):
    """数学模型"""

    def fit(self, data, *args, **kwargs) -> None:
        """训练模型

        Args:
            data: 应该是训练的数据
            *args: 其他参数
            **kwargs: 其他参数
        """
        raise NotImplementedError

    def predict(self, X, *args, **kwargs) -> np.ndarray[Real]:
        """预测

        Args:
            X: 需要预测的自变量数据
            *args: 其他参数
            **kwargs: 其他参数
        """
        raise NotImplementedError

    def score(self, X, y) -> Real:
        """评估模型

        Args:
            X: 自变量数据
            y: 因变量数据
        """
        raise NotImplementedError


class LinearModel(Model, Protocol):
    """线性回归模型

    Attributes:
        coef_: 回归系数
        intercept_: 截距
    """
    coef_: np.ndarray[Real]
    intercept_: Real

    def score(self, X, y) -> Real:
        """线性模型的评估，一般返回决定系数 :math:`R^2`

        Args:
            X: 自变量数据
            y: 因变量数据
        """
        raise NotImplementedError
