import os
import sys

from loguru._logger import Core, Logger

from users import User


class GlobalVariables:
    WELCOME_MESSAGE = 'Welcome to use this console!'

    path = os.getcwd()

    @staticmethod
    def refresh_path():
        GlobalVariables.path = os.getcwd()

    TempVariables = {}

    @staticmethod
    def clear_TempVariables():
        GlobalVariables.TempVariables.clear()

    class Console:
        echo = 'on'
        version = '0.0.1'
        license = 'MIT License'
        logger_color = {
            'debug': '\033[34m',  # 蓝色
            'info': '\033[92m',  # 绿色
            'warning': '\033[93m',  # 橙色
            'error': '\033[91m',  # 红色
            'critical': '\033[31;1m'  # 红色加粗
        }

        @staticmethod
        def reload__logger_color():
            GlobalVariables.Console.logger_color = GlobalVariables.Console.getDefault__logger_color()

        @staticmethod
        def getDefault__logger_color():
            return {
                'debug': '\033[34m',  # 蓝色
                'info': '\033[92m',  # 绿色
                'warning': '\033[93m',  # 橙色
                'error': '\033[91m',  # 红色
                'critical': '\033[31;1m'  # 红色加粗
            }

    class UserLoginInfo:
        login_status = False
        username = ''
        password_sha256 = ''
        UserInstance = None
        @staticmethod
        def login(account: User):
            GlobalVariables.UserLoginInfo.UserInstance = User
            GlobalVariables.UserLoginInfo.login_status = True
            GlobalVariables.UserLoginInfo.username = account.get_username()
            GlobalVariables.UserLoginInfo.password_sha256 = account.get_password_sha256()

        @staticmethod
        def logout():
            GlobalVariables.UserLoginInfo.login_status = False
            GlobalVariables.UserLoginInfo.username = ''
            GlobalVariables.UserLoginInfo.password_sha256 = ''


class Help:
    class Console:
        baseCmd = ('::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : '
                   '列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : '
                   'pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n')
        logger = ('简单的日志工具\n\n直接使用这些命令：\n1. logger.debug    调试\n2. logger.info     信息\n3. logger.warning  警告\n4. '
                  'logger.error    错误\n5. log_critical 严重')

    class Plugins: pass


# 别名
TempVariables = GlobalVariables.TempVariables


class ConsoleLogger:
    def __init__(self):
        self.__logger = Logger(
            core=Core(),
            exception=None,
            depth=0,
            record=False,
            lazy=False,
            colors=False,
            raw=False,
            capture=True,
            patchers=[],
            extra={},
        )
        self.__logger.remove()
        self.__logger.add(
            sys.stdout,
            format='[{time:YYYY-MM-DD HH:mm:ss}] [{level}] [{module}] | {message}',
            level="TRACE",
        )
        self.__logger.add(
            "logs/latest.log",
            format='[{time:YYYY-MM-DD HH:mm:ss}] [{level}] [{module}] | {message}',
            level="DEBUG",
            rotation="1 MB",
            retention="1 day",
            encoding="utf-8",
            compression="zip"
        )
        self.trace = self.__logger.trace
        self.debug = self.__logger.debug
        self.info = self.__logger.info
        self.success = self.__logger.success
        self.warning = self.__logger.warning
        self.warn = self.__logger.warning
        self.error = self.__logger.error
        self.critical = self.__logger.critical
        self.crit = self.__logger.critical
        self.catch = self.__logger.catch
        self.exception = self.__logger.exception

    @staticmethod
    def log_lines(log, msg: str):
        for line in msg.splitlines():
            log(line)


class Console:
    def __init__(self):
        self.logger = ConsoleLogger()
