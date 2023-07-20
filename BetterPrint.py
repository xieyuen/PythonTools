'''
Better Print 更好的打印
'''


# def print(
#     *values: object,
#     sep: Optional[str] = ...,
#     end: Optional[str] = ...,
#     file: Optional[SupportsWrite[str]] = ...,
#     flush: bool = ...,
# ) -> None: ...

class BetterPrint:
    '''
    更好的 print, 支持代码格式化
    可以关闭格式化

    需要启用格式化看下面：
    >>> bPrint = BetterPrint()
    >>> eg = [{'a':1, 'b':2}, {'a':3, 'b':4}]
    >>> bPrint(eg, format_=True)
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
    '''

    def __init__(self): ...

    def __call__(
        self,
        *values: object,
        _sep: Optional[str] = ...,
        _end: Optional[str] = ...,
        _file: Optional[SupportsWrite[str]] = ...,
        _flush: bool = ...,
        format_: bool = False,
    ) -> None:
        if format_: self.formatPrint(*values, end=_end)
        else:
            print(
                object_,
                sep=_sep,
                end=_end,
                file=_file,
                flush=_flush
            )

    def formatPrint(
        self,
        *values: object,
        end: Optional[str] = ...
    ) -> None:
        # tabstr = '    ' # 这是 4 个空格
        tabstr = '	' # 这是 Tab 制表符 '\t'
        tab = 0

        for string in values:
            if type(string) != str: string = str(string)

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
                    match string[index -1]:
                        case ' '|',': continue
                    print(char, end='')
                else: print(char, end='')
            
            print(' ', end='')
        print('',end=end)
        return None

    def __str__(self) -> str: return 'BetterPrint', self.__doc__

bPrint = BetterPrint()