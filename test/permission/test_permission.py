import unittest
from enum import Enum, auto
from pythontools import Permission
from pythontools.exceptions import PermissionReregisterError


class Perms(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    UPDATE = auto()


Permission.register(Perms.WRITE, Perms.DELETE, Perms.READ)
p = Permission(Perms.READ, Perms.WRITE)


class TestPermission(unittest.TestCase):

    def test_permission_operations(self):
        # 测试权限存在性
        self.assertTrue(p.has(Perms.READ))
        self.assertTrue(p.has(Perms.WRITE))
        self.assertFalse(p.has(Perms.DELETE))

        # 测试移除权限
        p.remove(Perms.WRITE)
        self.assertFalse(p.has(Perms.WRITE))

    def test_lock(self):
        Permission.lock()
        self.assertRaises(RuntimeError, Permission.register, Perms.UPDATE)
        Permission.lock()

    def test_reregister(self):
        self.assertRaises(PermissionReregisterError, Permission.register, Perms.READ)


if __name__ == "__main__":
    unittest.main()
