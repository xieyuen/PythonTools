class PermissionError(Exception):
    pass

class PermissionReregisterError(PermissionError):
    pass

class UnknownPermission(PermissionError, ValueError):
    pass
