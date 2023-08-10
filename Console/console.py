# 自己做一个控制台
import os
import sys
import shutil

from mymodule import logger


# 全局变量
global_vars = {
    'path': os.getcwd(),
    'console': {
        'echo': 'on',
        'version': '0.0.1',
        'license': 'MIT License',
    },'help': {
        'console': {},
        'plugin': {}
    },'temp': {
        'cmd': {
            'space': {
                'count': 0,
                'index': []
            }
        }
    },
}
global_vars['welcome'] = 'Welcome to use this console!'
# 日志颜色，将 global_vars['console']['logger'] 设为 'default' 则为默认值
global_vars['console']['logger'] = {
    'debug':    '\033[34m', # 蓝色
    'info':     '\033[92m', # 绿色
    'warning':  '\033[93m', # 橙色
    'error':    '\033[91m', # 红色
    'critical': '\033[31;1m' # 红色加粗
}
# 命令帮助
global_vars['help']['console'][
    'baseCmd'] = '::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : 列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n'
global_vars['help']['console'][
    'logger'] = '简单的日志工具\n\n直接使用这些命令：\n1. logger.debug    调试\n2. logger.info     信息\n3. logger.warning  警告\n4. logger.error    错误\n5. log_critical 严重'
# 别名
temp = global_vars['temp']

# ---------------------------------------------------------------------------------------------


class Console:
    '''控制台工具'''

    class CustomCmds:
        '''自定义命令'''

        def __init__(self):
            ...

        def cmd(self, command: str):
            os.system(command)


    class ConsoleException(Exception):
        '''控制台异常，请在抛出异常前用 exc_msg() 方法设置异常信息'''

        def __init__(self, msg: str = 'Console has exited.'):
            self.message = msg
        def __str__(self):
            return self.message
        def exc_msg(self, msg: str):
            self.message = msg


    def __init__(self):
        self.logger = self.Logger()
        self.custom_cmds = self.CustomCmds()
        self.exception = self.ConsoleException()
        self.command_map = {
            'help': ConsoleCmd.help,
            'cd': ConsoleCmd.cd,
            'md': ConsoleCmd.mkdir,
            'mkdir': ConsoleCmd.mkdir,
            'rd': ConsoleCmd.rmdir,
            'rmdir': ConsoleCmd.rmdir,
            'pause': ConsoleCmd.pause,
            'version': ConsoleCmd.version,
            'license': ConsoleCmd.license_,
            'echo': ConsoleCmd.echo_,
            'del': ConsoleCmd.del_,
            'cls': ConsoleCmd.clear_,
            'plugin': ConsoleCmd.plg,
        }
    
    def register_command(self, key: str, func: callable) -> None:
        '''添加新的定位定位'''
        def recursive(key: list, func: callable):
            if len(key) == 1:
                self.command_map[key[0]] = func
            elif key[0] not in self.command_map:
                self.command_map[key[0]] = {}
                recursive(key[1:], func)
            elif isinstance(key[0], dict):
                recursive(key[1:], func)
            else:
                raise TypeError('key must be a dict')


console = Console()
cmd = console.custom_cmds.cmd


# ---------------------------------------------------------------------------------------------


# 定义命令
class ConsoleCmd:
    '''控制台命令'''

    def help(__other_cmd: str):
        logger.info('帮助')
        if __other_cmd.isspace() or __other_cmd == '':
            logger.info('Help Massage:')
            print(global_vars['help']['console'])
        else:
            if __other_cmd in global_vars['help']:
                logger.info(global_vars['help'][__other_cmd])
            else:
                logger.warning(f'未找到 {__other_cmd } 的帮助！')
        return None


    def cd(__other_cmd: str):
        global global_vars
        if __other_cmd.isspace() or __other_cmd == '':
            logger.info(global_vars['path'])
            return global_vars['path']

        __path = __other_cmd
        if not os.path.exists(__path):
            logger.error('目录不存在')
            os.mkdir(__path)
            logger.debug('目录已创建')
        os.chdir(__path)
        global_vars['path'] = os.getcwd()
        logger.info('工作目录已更改为 ' + global_vars['path'] + '.')
        return True


    def mkdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            logger.error('mkdir 必须要指定目录名称')
            return False
        os.mkdir(__other_cmd)
        logger.info('目录已创建')
        return True


    def rmdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            logger.error('rmdir 必须要指定目录名称')
            return False
        try:
            os.rmdir(__other_cmd)
            logger.info('目录已删除')
        except OSError:
            logger.error('目录非空')
            logger.error('是否强制删除目录？这会会删除目录下的所有文件(夹)')
            ans = input('输入 y 确认，其他任意键取消：')
            if ans == 'y':
                try:
                    shutil.rmtree(__other_cmd)
                    logger.info('目录已删除')
                    return True
                except:
                    logger.catch_exc('Python 抛出了一个异常')
                    logger.error('目录删除失败')
            logger.info('目录删除操作取消')
        except:
            logger.catch_exc('好像触发了什么奇奇怪怪的异常？')
        return False


    def del_(__other_cmd: str) -> bool:
        if __other_cmd.isspace() or __other_cmd == '':
            logger.error('del 必须要指定文件名称')
            return False
        if not os.path.exists(__other_cmd):
            logger.error('文件不存在')
            return False
        try:
            os.remove(__other_cmd)
        except:
            logger.catch_exc('好像触发了什么奇奇怪怪的异常？')
        else:
            logger.info('文件已删除')
            return True


    def pause(__none=None) -> None:
        logger.info('请按 Enter 键继续...')
        input()


    def version(__none=None) -> None:
        logger.info(f"版本号: {global_vars['console']['version']}")


    def license_(__none=None) -> None:
        logger.info(global_vars['console']['license'])


    def echo_(__other_cmd: str) -> None:
        print(rf'{__other_cmd}')


    def clear_(__none=None) -> None:
        os.system('cls')
        return True


    def exit_(__none=None) -> None:
        logger.info('Bye!')
        raise SystemExit


    def plg(__other_cmd: str) -> None:
        logger.info('plugin')
        print(__other_cmd)
        logger.info(global_vars['plugin'])


# ---------------------------------------------------------------------------------------------


def main():
    global global_vars
    logger.info(global_vars['welcome'])

    while True:
        __space['count'] = 0
        __space['index'] = []

        input_str = input('>>> ')
        if input_str == 'exit' or input_str == 'quit' or input_str == '':
            ConsoleCmd.exit_(None)

        for __index in range(len(input_str)):
            __char = input_str[__index]

            if __char == ' ':
                __space['count'] += 1
                __space['index'].append(__index)
        if __space['count'] == 0:
            __space['index'].append(len(input_str))

        global_vars['temp']['cmd']['space'] = __space
        __1st_space = __space['index'][0]
        __action = console.command_map.get(input_str[0:__1st_space], False)

        if __action:
            __action(input_str[__1st_space + 1:])
        else:
            logger.warning(f'Command "{input_str}" not found')

        # 重置变量
        del __action


if __name__ == '__main__':
    main()
