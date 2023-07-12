# 自己做一个控制台
import os
import sys

# 全局变量
global_vars = {
    'path': os.getcwd(),
    'console': {
        'echo': 'on',
        'version': '0.0.1',
        'license': 'MIT License',
    },
    'help': {
        'console': {},
        'plugin': {}
    },
    'temp': {
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
    'debug':    '\033[34m',
    'info':     '\033[92m',
    'error':    '\033[91m',
    'warning':  '\033[93m',
    'critical': '\033[31;1m'
}
# 命令帮助
global_vars['help']['console']['baseCmd'] = '::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : 列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n'
global_vars['help']['console']['logger'] = '简单的日志工具\n\n直接使用这些命令：\n1. log.debug    调试\n2. log.info     信息\n3. log.warning  警告\n4. log.error    错误\n5. log_critical 严重'


# 自定义函数
def cmd(command: str): os.system(command)
class ConsoleExit(Exception):
    def __init__(self, message: str = 'Console has exited.'):
        self.message = message
    def __str__(self):
        return self.message

# ---------------------------------------------------------------------------------------------

class Logger:
    '''简单的日志工具'''
    global global_vars
    # log 类型
    __log_color = global_vars['console']['logger']
    if __log_color == 'default': #默认值
        __log_color = global_vars['console']['logger'] = { # 日志颜色
            'debug':    '\033[34m',
            'info':     '\033[92m',
            'error':    '\033[91m',
            'warning':  '\033[93m',
            'critical': '\033[31;1m'
        }
    __log_map = {
        'debug':    __log_color['debug']    + '[debug]',
        'info':     __log_color['info']     + '[Info]',
        'error':    __log_color['error']    + '[ERROR]',
        'warning':  __log_color['warning']  + '[WARNING]',
        'critical': __log_color['critical'] + '[CRITICAL]'
    }
    def __init__(self, __level: str):
        self.level = __level
    def __call__(self, message: str):
        __level = self.__log_map[self.level]
        print(__level + ' ' + message + '\033[0m')

class LogOutput:
    '''日志集成'''
    def __init__(self):
        self.debug = Logger('debug')
        self.info = Logger('info')
        self.warning = Logger('warning')
        self.error = Logger('error')
        self.critical = Logger('critical')
    def debug(self, msg): self.debug(msg)
    def info(self, msg): self.info(msg)
    def warning(self, msg): self.warning(msg)
    def warn(self, msg): self.warning(msg)
    def error(self, msg): self.error(msg)
    def critical(self, msg): self.critical(msg)
# 生成实例
log = LogOutput()

# ---------------------------------------------------------------------------------------------

# 定义命令
class ConsoleCmd:
    '''控制台命令'''
    def help(__other_cmd: str):
        log.info('帮助')
        if __other_cmd.isspace() or __other_cmd == '':
            log.info('Help Massage:')
            print(global_vars['help']['console'])
        else:
            if __other_cmd in global_vars['help']:
                log.info(global_vars['help'][__other_cmd])
            else: log.warning(f'未找到 {__other_cmd } 的帮助！')
        return     

    def cd(__other_cmd: str):
        global global_vars
        if __other_cmd.isspace() or __other_cmd == '':
            log.info(global_vars['path'])
        else:
            __path = global_vars['path'] + '/' + __other_cmd
            global_vars['path'] = __path
            if not os.path.exists(__path):
                log.error('目录不存在')
                os.mkdir(__path)
                log.debug('目录已创建')
            os.chdir(__path)
            log.info('工作目录已更改为 ' + global_vars['path'] + '.')

    def mkdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            log.error('mkdir 必须要指定目录名称')
        else:
            os.mkdir(__other_cmd)
            log.info('目录已创建')

    def cls(__none):
        cmd('cls')

    def dir(__none):
        print(cmd('dir'))

    def rmdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            log.error('rmdir 必须要指定目录名称')
        else:
            os.rmdir(__other_cmd)
            log.info('目录已删除')

    def pause(__none):
        log.info('请按 Enter 键继续...')
        input()

    def version(__none):
        log.info(global_vars['version'])

    def license(__none):
        log.info(global_vars['license'])

    def echo(__other_cmd: str):
        print(__other_cmd)

    def exit(__none):
        log.info('Bye!')
        raise ConsoleExit

    def plg(__other_cmd: str):
        log.info('plugin')
        print(__other_cmd)
        log.info(global_vars['plugin'])

command_map = {
    'exit':    ConsoleCmd.exit,
    'quit':    ConsoleCmd.exit,
    'help':    ConsoleCmd.help,
    'cd':      ConsoleCmd.cd,
    'md':      ConsoleCmd.mkdir,
    'mkdir':   ConsoleCmd.mkdir,
    'rd':      ConsoleCmd.rmdir,
    'rmdir':   ConsoleCmd.rmdir,
    'pause':   ConsoleCmd.pause,
    'version': ConsoleCmd.version,
    'license': ConsoleCmd.license,
    'echo':    ConsoleCmd.echo,
    'clear':   ConsoleCmd.cls,

    'plugin': ConsoleCmd.plg
}

def command_choice(header: str, other):
    __action = command_map.get(header, None)
    if __action: __action(other)
    else:
        log.warning(f'Command {header} not found')

# ---------------------------------------------------------------------------------------------

def analysis_space(string: str):

    global global_vars
    __space = global_vars['temp']['cmd']['space']

    for __index in range(len(string)):
        __char = string[__index]
        if __char == ' ':
            __space['count'] += 1
            __space['index'].append(__index)
    if __space['count'] == 0:
        __space['index'].append(len(string))

    global_vars['temp']['cmd']['space'] = __space
    return __space


def analysis_cmd(command: str):

    global global_vars
    global command_map
    __1st_space = analysis_space(command)['index'][0]

    # __action = __command_map.get(command[0:__1st_space], None)
    # if __action:
    #     __action(command[__1st_space + 1:])
    # else:
    #     log.warning('command not found')

    del __action

# ---------------------------------------------------------------------------------------------

def main():
    log.info(global_vars['welcome'])
    while True:
        input_str = input('>>> ')
        analysis_cmd(input_str)


if __name__ == '__main__':
    main()
