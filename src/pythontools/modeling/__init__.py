from typing import Iterable

import numpy as np
from pandas import DataFrame, Series
from scipy.stats import t

from pythontools.modeling.normalization import *
from pythontools.types.modeling import Model, LinearModel


def remove(data: DataFrame, condition: Series | Iterable):
    """
    删除符合条件的行，会直接修改数据

    Args:
        data (DataFrame): 要修改的数据
        condition (SeriesLike): 条件

    Example:
        >>> remove(data, data["x"]==1)
    """
    data.drop(
        data[condition].index,
        inplace=True
    )


def remove_na(data: DataFrame):
    """
    删除所有有数据缺失的行，会直接修改数据
    """
    for subset in data:
        data.dropna(
            subset=subset,
            inplace=True
        )


def r_squared(model: Model, X, y):
    return model.score(X, y)


def adjusted_r_squared(r2, X):
    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p(model: LinearModel, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)

    residuals = y - y_pred
    dof = len(X) - len(coefficients) - 1  # 自由度
    mse = np.sum(residuals ** 2) / dof

    X_with_const = np.column_stack([np.ones(len(X)), X])  # 添加截距项
    cov_matrix = np.linalg.inv(X_with_const.T @ X_with_const) * mse
    std_errors = np.sqrt(np.diag(cov_matrix))[1:]  # 忽略截距的标准误差

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - t.cdf(np.abs(t_stats), df=dof))

    return p_value


def related_r(x, y):
    """样本相关系数"""
    length = len(x)

    x_mean = x.mean()
    y_mean = y.mean()

    return (
            (np.sum(
                [xi * yi for xi, yi in zip(x, y)]
            ) - length * x_mean * y_mean)
            /
            (np.sqrt(
                np.sum([xi ** 2 for xi in x]) - length * x_mean ** 2
            ) * np.sqrt(
                np.sum([yi ** 2 for yi in y]) - length * y_mean ** 2
            ))
    )


def print_result_for_lm(model: LinearModel, x, y):
    print("变量:", *x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {adjusted_r_squared(model.score(x, y), x)}")
    print("P值:", *p(model, x, y))


__all__ = [
    # data handle
    "remove", "remove_na",
    # calc
    "related_r", "r_squared", "adjusted_r_squared", "p",
    # Normalizer
    "Normalizer",
    "ZScoreNormalizer", "ZScoreScaler", "StandardScaler",
    "MinMaxNormalizer", "MinMaxScaler",
    # other
    "print_result_for_lm",
]
