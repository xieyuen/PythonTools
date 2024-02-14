import traceback
from typing import Callable


def print_exc(call: Callable, _e=Exception):
    def wrapper(*args, **kwargs):
        try:
            return call(*args, **kwargs)
        except _e:
            traceback.print_exc()

    return wrapper
