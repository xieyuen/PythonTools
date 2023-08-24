from mymodule import logger

import data
from utils import sha256


accounts = data.load_user_data().copy()
login_status: bool = False
login_account: str = str()
login_password: str = str()


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

            if not sha256(password) == account['password']:
                logger.warning('密码错误！')
                return False

            if not account['enable']:
                logger.warning('账号已被禁用！')
                return False
            logger.info('登录成功！')

            global login_status, login_account,  login_password
            login_status = True
            login_account = username
            login_password = sha256(password)

            return True

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


def register_account(username):
    """
    注册账号
    :param username: 用户名
    :return:
    """
    global login_status, login_account
    for acc in accounts:
        if acc['username'] == username:
            logger.error('该用户名已被注册！')
            return False

    password = input('Enter your password: ')
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


def enable_account(username) -> bool:
    """
    启用账号
    :param username: 用户名
    :return: 是否启用成功
    """
    for a in accounts:
        if a['username'] == username:
            if a['enable']:
                logger.warning('该账号已启用！')
                return False

            logger.info('启用账号需要授权！')
            if sha256(input('请输入密码: ')) != login_password:
                logger.warning('密码错误！')
                return False

            a['enable'] = True
            data.save_user_data(accounts)
            logger.info('启用账号成功！')
            return True
    logger.warning('未查询到账号！')
    return False


def disable_account(username) -> bool:
    """
    禁用账号
    :param username: 用户名
    :return: 是否禁用成功
    """
    for a in accounts:
        if a['username'] == username:
            if not a['enable']:
                logger.warning('该账号已禁用！')
                return False

            logger.info('禁用账号需要授权！')
            if sha256(input('请输入密码: ')) != login_password:
                logger.warning('密码错误！')
                return False

            a['enable'] = False
            data.save_user_data(accounts)
            logger.info('禁用账号成功！')
            return True

    logger.warning('未查询到账号！')
    return False


def main() -> login_status:
    if len(accounts) == 1 and accounts[0]['username'] == 'root':
        logger.info('当前没有账号，请注册您的账号')
        username = input('Enter your account name: ')
        register_account(username)

    logger.info('请登录你的账号')
    username = input('Enter your account name: ')
    login(username)
    while not login_status:
        logger.info('您需要注册账号吗？')
        logger.info('需要请输入y，重新登录请输入r，切换账号请输入s')
        need_register = input('y/r/s: ')
        if need_register.lower() == 'y':
            username = input('Enter your account name: ')
            register_account(username)
        elif need_register.lower() == 'r':
            login(username)
        elif need_register.lower() == 's':
            username = input('Enter your account name: ')
            login(username)

    return login_status
