from typing import Protocol
from numbers import Real

import numpy as np


class Model(Protocol):
    def fit(self, *args, **kwargs) -> None: ...

    def predict(self, X) -> np.ndarray[Real]: ...

    def score(self, X, y) -> Real: ...


class LinearModel(Model, Protocol):
    coef_: np.ndarray[Real]
    intercept_: Real
