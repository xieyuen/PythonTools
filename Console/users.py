import hashlib

__all__ = ['User']


def sha256(data):
    return hashlib.sha256(data.encode()).hexdigest()


class Password:
    def __init__(self, pw_sha256, *, no_hash=False):
        self.__password_sha256 = pw_sha256 if not no_hash else sha256(pw_sha256)

    def get_password_sha256(self):
        return self.__password_sha256


class User:
    __username: str
    __password: str

    def __init__(self, username, pw_sha256):
        self.__username = username
        self.__password = pw_sha256

    def get_username(self):
        return self.__username

    def get_password_sha256(self):
        return self.__password

    def __eq__(self, other):
        return self.__username == other.get_username()

    def rename(self, pw: str, name: str) -> bool:
        if sha256(pw) != self.__password:
            return False
        self.__username = name
        return True

    def re_password(self, pw: str, new_pw: str) -> bool:
        if sha256(pw) != self.__password or new_pw.isdigit():
            return False
        self.__password = sha256(new_pw)
        return True

    def __hash__(self):
        return sha256(self.__username)
