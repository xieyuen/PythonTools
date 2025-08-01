from enum import Enum, auto
from pythontools import Permission

class Perms(Enum):
    READ = auto()
    WRITE = auto()
    DELETE = auto()
    EDIT = auto()


Permission.register(*Perms)


def test():
    p = Permission(Perms.READ, Perms.WRITE)
    print(p.has(Perms.READ))  # True
    print(p.has(Perms.WRITE))  # True
    print(p.has(Perms.DELETE))  # False
    p.remove(Perms.WRITE)
    print(p.has(Perms.WRITE))  # False


if __name__ == "__main__":
    test()
