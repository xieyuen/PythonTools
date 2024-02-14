from enum import auto
from typing import TYPE_CHECKING

from tools import print_exc


def keywordSetter(name):
    raise SyntaxError(f'cannot assign to {name}')


if TYPE_CHECKING:
    keywordSetter = print_exc(keywordSetter)


class GlobalVariables:
    @property
    def null(self):
        return auto()

    @property
    def undefined(self):
        return auto()

    @null.setter
    def null(self, item):
        keywordSetter('null')


GlobalVariables = GlobalVariables()

if __name__ == '__main__':
    GlobalVariables.null = 1
