class BasePermissionError(Exception):
    pass


class PermissionReregisterError(BasePermissionError):
    pass


class UnknownPermission(BasePermissionError, ValueError):
    pass
