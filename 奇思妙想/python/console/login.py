from mymodule import logger

import data
from utils import sha256


accounts = data.load_user_data().copy()
login_status: bool = False
login_account: str = str()


def login(username: str, *, password: str | None = None) -> bool:
    """
    登录账号
    :param username: 用户名
    :param password: 密码
    :return: 是否登录成功
    """
    for account in accounts:
        if account['username'] == username:
            password = input('Enter your password: ') \
                if password is None else password

            if sha256(password) == account['password']:
                logger.info('登录成功！')

                global login_status, login_account
                login_status = True
                login_account = username

                return True

            logger.warning('密码错误！')
            return False
    logger.warning('账号不存在！')
    return False


def logout():
    """
    登出账号
    :return:
    """
    global login_status, login_account
    login_status = False
    login_account = ''
    logger.info('登出成功！')


def register_account(username, password):
    """
    注册账号
    :param username: 用户名
    :param password: 密码
    :return:
    """
    global login_status, login_account
    accounts.append(
        {
            'username': username,
            'password': sha256(password),
            'enable': True
        }
    )
    data.save_user_data(accounts)
    logger.info('注册成功！已为您自动登录')
    login_status = True
    login_account = username


def change_password(username, old_password: str, new_password: str) -> bool:
    """
    修改密码
    :param username: 用户名
    :param old_password: 旧密码
    :param new_password: 新密码
    :return: 是否修改成功
    """
    for a in accounts:
        if a['username'] == username:
            if sha256(old_password) == sha256(a['password']):
                a['password'] = sha256(new_password)
                data.save_user_data(accounts)
                logger.info('修改密码成功！')
                return True
            logger.warning('密码错误！')
            return False
    logger.warning('账号不存在！')
    return False


def change_username(username, password, new_username) -> bool:
    """
    修改用户名
    :param username: 用户名
    :param password: 密码
    :param new_username: 新用户名
    :return: 是否修改成功
    """
    for a in accounts:
        if a['username'] == username:
            if sha256(password) == sha256(a['password']):
                a['username'] = new_username
                data.save_user_data(accounts)
                logger.info('修改用户名成功！')
                return True
            logger.warning('密码错误！')
            return False
    logger.warning('账号不存在！')
    return False


def main():
    logger.info('请登录你的账号')
    user_name = input('Enter your account name: ')
    login(user_name)
    while not login_status:
        logger.info('您需要注册账号吗？')
        logger.info('需要请输入y，重新登录请输入r，切换账号请输入s')
        need_register = input('y/r/s: ')
        if need_register.lower() == 'y':
            user_name = input('Enter your account name: ')
            password = input('Enter your password: ')
            register_account(user_name, password)
        elif need_register.lower() == 'r':
            login(user_name)
        elif need_register.lower() == 's':
            user_name = input('Enter your account name: ')
            login(user_name)

    return login_status
