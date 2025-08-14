from numbers import Real

from pandas import DataFrame, Series
from scipy.stats import t

from pythontools.modeling import base
from pythontools.modeling.base import *
from pythontools.modeling.normalization import *
from pythontools.types.modeling import Model, LinearModel


def remove(data: DataFrame, condition: Series[bool]) -> None:
    """
    删除符合条件的行，会直接修改数据

    Args:
        data (DataFrame): 要修改的数据
        condition (Series): 布尔条件，例如 data["x"] == 1

    Example:
        >>> data = DataFrame({"x": [1, 2, 3]})
        >>> remove(data, data["x"]==1)
    """
    data.drop(
        data[condition].index,
        inplace=True
    )


def remove_na(data: DataFrame) -> None:
    """
    删除所有有数据缺失的行，会直接修改数据

    Example:
        >>> remove_na(data)
    """
    data.dropna(inplace=True)


def r_squared(model: Model, X, y) -> Real:
    """决定系数 R 方"""
    return model.score(X, y)


def adjusted_r_squared(r2: Real, X: DataFrame) -> Real:
    """
    调整 R 方

    Args:
        r2 (Real): 决定系数 R 方
        X (DataFrame): 模型拟合时用的数据
    """
    # 计算调整R²
    n, p = X.shape  # 样本数和特征数
    adjusted_r2 = 1 - (1 - r2) * (n - 1) / (n - p - 1)

    return adjusted_r2


def p_values(model: LinearModel, X, y):
    """p值"""
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


def corr(x: Series, y: Series) -> Real:
    r"""
    样本相关系数

    计算公式:

    .. math::
        corr = \frac{ \sum_{i=1}^{n} (x_i - \bar{x})(y_i - \bar{y}) }{ \sqrt{ \frac{1}{n}\sum_{i=1}^{n} (x_i - \bar{x})^2 } \sqrt{ \frac{1}{n}\sum_{i=1}^{n} (y_i - \bar{y})^2}}

    Args:
        x (Series): 变量 1
        y (Series): 变量 2

    Returns:
        Real: 一个 [0, 1] 之间的数

    Raises:
        ValueError: 数据长度必须大于 1
        ValueError: 数据长度必须相同
        ValueError: 数据有空
    """
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


def related_r(x: Series, y: Series) -> Real:
    """``corr`` 的别名"""
    return corr(x, y)


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
    "mean", "std",
    "related_r", "corr", "r_squared", "adjusted_r_squared", "p_values",
    # Normalizer
    "Normalizer",
    "ZScoreNormalizer", "ZScoreScaler", "StandardScaler",
    "MinMaxNormalizer", "MinMaxScaler",
    # other
    "print_result_for_lm",
    # types
    "Model", "LinearModel",
]
