from .global_variables import GlobalVariables

class Void:
    def __repr__(self):
        return GlobalVariables.undefined

    __str__ = __repr__


class Object(object):
    def toString(self, __n=GlobalVariables.null):
        return str(self)


class Function(Object):
    def __init__(self, call):
        self.__call = call

    def __call__(self, *args, **kwargs):
        return self.__call(*args, **kwargs)
