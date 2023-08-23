from mymodule.register import Register


没用的函数 = Register()


@没用的函数
def mergeDicts(*dicts, **other):
    result = {}
    for d in dicts:
        result.update(d)
    return dict(**result, **other)
