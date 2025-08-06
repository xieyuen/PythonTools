from typing import Literal

import numpy as np


def std(data, ddof: Literal[0, 1] = 0):
    if hasattr(data, "std"):
        return data.std(ddof=ddof)
    n = len(data)

    return (np.sum(data ** 2) - n * mean(data)) / (n - ddof)


def mean(data):
    if hasattr(data, "mean"):
        return data.mean()
    return np.sum(data) / len(data)
