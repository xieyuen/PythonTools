import unittest
from enum import Enum, auto
from pythontools import Permission


class Perms(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    EDIT = READ | WRITE | DELETE


Permission.register(*Perms)


class TestPermission(unittest.TestCase):

    def test_permission_operations(self):
        # 创建一个包含READ和WRITE权限的Permission对象
        p = Permission(Perms.READ, Perms.WRITE)

        # 测试权限存在性
        self.assertTrue(p.has(Perms.READ))
        self.assertTrue(p.has(Perms.WRITE))
        self.assertFalse(p.has(Perms.DELETE))
        self.assertFalse(p.has(Perms.EDIT))

        # 测试移除权限
        p.remove(Perms.WRITE)
        self.assertFalse(p.has(Perms.WRITE))


if __name__ == "__main__":
    unittest.main()
