from typing import Protocol

import numpy as np


class Model(Protocol):
    def fit(self, *args, **kwargs) -> None: ...

    def predict(self, X) -> np.ndarray[np.number]: ...

    def score(self, X, y) -> np.number: ...


class LinearModel(Model, Protocol):
    coef_: np.ndarray[np.number]
    intercept_: np.number
