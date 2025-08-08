from typing import Iterable
from numbers import Real

import numpy as np
from pandas import DataFrame, Series
from scipy.stats import t

from pythontools.modeling.normalization import *
from pythontools.modeling import base
from pythontools.types.modeling import Model, LinearModel


def remove(data: DataFrame, condition: Series | Iterable) -> None:
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


def remove_na(data: DataFrame) -> None:
    """
    删除所有有数据缺失的行，会直接修改数据
    """
    for subset in data:
        data.dropna(
            subset=subset,
            inplace=True
        )


def r_squared(model: Model, X, y) -> Real:
    return model.score(X, y)


def adjusted_r_squared(r2, X) -> Real:
    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p_values(model: LinearModel, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)

    residuals = y - y_pred
    dof = len(X) - len(coefficients) - 1  # 自由度
    mse = np.sum(residuals ** 2) / dof

    X_with_const = np.column_stack([np.ones(len(X)), X])  # 添加截距项
    cov_matrix = np.linalg.pinv(X_with_const.T @ X_with_const) * mse
    std_errors = np.sqrt(np.diag(cov_matrix))[1:]  # 忽略截距的标准误差

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - t.cdf(np.abs(t_stats), df=dof))

    return p_value


"""
def p_values(model: LinearModel, X, y):
    coefficients = model.coef_
    y_pred = model.predict(X)

    residuals = y - y_pred
    dof = len(X) - len(coefficients)  # 自由度修正
    if dof <= 0:
        raise ValueError("自由度必须为正数，请检查输入数据")
    
    mse = np.sum(residuals ** 2) / dof

    X_with_const = np.column_stack([np.ones(len(X)), X])  # 添加截距项
    
    # 使用更数值稳定的方法计算协方差矩阵
    try:
        # 使用solve方法避免直接求逆
        XtX_inv = np.linalg.pinv(X_with_const.T @ X_with_const)
        cov_matrix = XtX_inv * mse
    except np.linalg.LinAlgError:
        raise ValueError("无法计算协方差矩阵，可能是由于矩阵奇异")
    
    std_errors = np.sqrt(np.diag(cov_matrix))[1:]  # 忽略截距的标准误差
    
    # 避免除零错误
    if np.any(std_errors == 0):
        raise ValueError("标准误差不能为零")

    # 计算t统计量和P值
    t_stats = coefficients / std_errors
    p_value = 2 * (1 - t.cdf(np.abs(t_stats), df=dof))

    return p_value

"""



def related_r(x: Series, y: Series) -> Real:

    """样本相关系数"""
    length = len(x)

    if length <= 1:
        raise ValueError("数据长度必须大于1")
    if length != len(y):
        raise ValueError("数据长度必须相同")
    if x.isnull().any() or y.isnull().any():
        raise ValueError("数据有空")
    if np.isclose(x.std(), 0) or np.isclose(y.std(), 0):
        return 0  # 常数据不存在相关性

    return np.sum((x - base.mean(x)) * (y - base.mean(y))) / (length * base.std(x) * base.std(y))

    # 算法 2

    # x_mean = x.mean()
    # y_mean = y.mean()
    # xy = np.sum(x * y)
    # x_squares = np.sum(x ** 2)
    # y_squares = np.sum(y ** 2)

    # return (
    #         (xy - length * x_mean * y_mean)
    #         / (
    #                 np.sqrt(x_squares - length * x_mean ** 2)
    #                 * np.sqrt(y_squares - length * y_mean ** 2)
    #         )
    # )


corr = related_r


def print_result_for_lm(model: LinearModel, x, y) -> None:
    print("变量:", *x.columns.values)
    print("回归系数:", *model.coef_)
    print(f"截距: {model.intercept_}")
    print(f"决定R方: {model.score(x, y)}")
    print(f"调整R方: {adjusted_r_squared(model.score(x, y), x)}")
    print("P值:", *p_values(model, x, y))


__all__: list[str] = [
    # data handle
    "remove", "remove_na",
    # calc
    "related_r", "corr", "r_squared", "adjusted_r_squared", "p_values",
    # Normalizer
    "Normalizer",
    "ZScoreNormalizer", "ZScoreScaler", "StandardScaler",
    "MinMaxNormalizer", "MinMaxScaler",
    # other
    "print_result_for_lm",
]
