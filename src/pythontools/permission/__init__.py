from typing import Dict, Any

from pythontools.exceptions import PermissionReregisterError, UnknownPermission


class Permission:
    __all_permissions: Dict[Any, int] = {}
    __length: int = 0

    @classmethod
    def exists(cls, perm: Any) -> bool:
        return perm in cls.__all_permissions

    @classmethod
    def register(cls, *perms: Any) -> None:
        for perm in perms:
            if cls.exists(perm):
                raise PermissionReregisterError(perm)
            cls.__all_permissions[perm] = 2 ** cls.__length
            cls.__length += 1
    
    @classmethod
    def get(cls, perm) -> Any:
        return cls.__all_permissions[perm]
    
    # ----------------------------------------------------

    def __init__(self, *perms: Any) -> None:
        self.__permissions: int = 0
        if perms:
            self.set(*perms)

    def set(self, *perms: Any) -> None:
        for perm in perms:
            if not Permission.exists(perm):
                Permission.register(perm)
            self.__permissions |= Permission.get(perm)

    def has(self, *perms: Any) -> bool:
        for perm in perms:
            if not Permission.exists(perm):
                return False
            if not (self.__permissions & Permission.get(perm)):
                return False
        return True

    def remove(self, *perms: Any) -> None:
        for perm in perms:
            if not Permission.exists(perm):
                raise UnknownPermission(perm)
            self.__permissions &= ~Permission.get(perm)
            
