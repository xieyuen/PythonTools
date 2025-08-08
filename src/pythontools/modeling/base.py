from typing import Literal

import numpy as np


def std(data, ddof: Literal[0, 1] = 0):
    if hasattr(data, "std"):
        return data.std(ddof=ddof)
    n = len(data)
    if n == 1:
        return 0
    return np.sqrt(
        (np.sum(x ** 2 for x in data))
        / (n - ddof) - mean(data) ** 2
    )


def mean(data):
    if hasattr(data, "mean"):
        return data.mean()
    return np.sum(data) / len(data)
