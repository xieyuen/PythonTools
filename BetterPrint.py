"""
Better Print 更好的打印
"""


__all__ = [
    'bPrint', 'BetterPrint'
]


def _formatPrint(
    *values: object,
    end = '\n',
    tabstr: str = '    ',
) -> None:
    # tabstr = '    ' # 这是 4 个空格
    # tabstr = '\t' # 这是 Tab 制表符
    tab = 0

    for val in values:

        match type(val):
            case str:
                for index in range(len(string)):
                    char = string[index]

                    if char in '([{':
                        print(char, end='')
                        tab += 1
                        print('\n', end=tabstr * tab)
                    elif char in '}])':
                        print()
                        tab -= 1
                        print(tabstr * tab, end=char)
                    elif char == ',':
                        print(char)
                        print(tabstr * tab, end='')
                    elif char == ' ':
                        # 当前面是空格 ( ) 或者半角逗号 (,) 时跳过
                        match string[index - 1]:
                            case ' '|',': continue
                        print(char, end='')
                    else: print(char, end='')
                print(' ', end='')

            case dict:
                for index in range(len(str(val))):
                    char = str(val)[index]

                    match char:
                        case '{':
                            if tab != 0:

                                tab += 1
                                print(char)
                                print(tabstr * tab, end='')
                        case '}': ...
                        case '[': ...
                        case ']': ...
                        case ',': ...
                        case ' ':
                            if str(val)[index - 1] in ' ,': continue
                            print(char, end='')
                        case _: print(char, end='')

    print('', end=end)
    return None


class BetterPrint:
    """
    更好的 print, 支持代码格式化
    可以关闭格式化

    需要启用格式化看下面：
    >>> bPrint = BetterPrint()
    >>> eg = [{'a':1, 'b':2}, {'a':3, 'b':4}]
    >>> bPrint(eg, format=True)
    [
        {
            'a': 1,
            'b': 2
        },
        {
            'a': 3,
            'b': 4
        }
    ]
    """

    def __init__(self): ...

    def __call__(
        self,
        *values: object,
        format: bool = True,
        end: str = '\n',
        tab: str = '    ',
        **okwargs
    ) -> None:

        if format: _formatPrint(*values, end=end)
        else:
            print(
                *values,
                end=end,
                **okwargs,
            )

    def __str__(self) -> str: return 'BetterPrint' + self.__doc__

bPrint = BetterPrint()