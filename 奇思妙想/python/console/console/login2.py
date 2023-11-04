from loguru import logger

from utils import sha256


class Account:
    def __init__(self, username: str, password: str = None, *, password_sha256: str = None):
        self.authorized = None
        self.username = username
        if (password_sha256 is None) ^ (password is None):
            raise ValueError('Either password_sha256 or password must be provided.')
        if password_sha256 is None:
            self.password = sha256(password)
        else:
            self.password = password_sha256

    def __eq__(self, other):
        return self.username == other.username

    def __repr__(self):
        return f"Account(username='{self.username}', password='**********')"

    def dict(self) -> dict:
        return {
            'username': self.username,
            'password': self.password,
            'enable': True
        }

    def auth(self, password):
        """
        Authenticate the user.
        :param password: The password to be authenticated.
        """
        if sha256(password) != self.password:
            logger.error('密码错误')
            logger.error('授权失败')
            self.authorized = False
        else:
            logger.info('授权成功')
            self.authorized = True

    def rename(self, new_username: str):
        logger.info('需要授权')
        pw = input('请输入密码：')
        self.auth(pw)
        if self.authorized:
            self.username = new_username
            logger.info('改名成功')
            self.authorized = False

    def change_password(self, new_password: str):
        logger.info('需要授权')
        pw = input('请输入密码：')
        self.auth(pw)
        if self.authorized:
            self.username = new_password
            logger.info('密码已更改')
            self.authorized = False

    @classmethod
    def load(cls, data: dict):
        return cls(data['username'], password_sha256=data['password'])
