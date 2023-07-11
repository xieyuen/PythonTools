# 自己做一个控制台
import os
import sys

# 定义全局变量
__vars = {
    'path': os.getcwd(),
    'echo': 'on',
    'version': '0.0.1',
    'license': 'MIT License',
    'help': {
        'console': {},
        'plugin': {}
    },
    'cmd': {
        'space': {
            'count': 0,
            'index': []
        }
    }
}
__vars['welcome'] = 'Welcome to use this console!'
# 命令帮助
__vars['help']['console']['baseCmd'] = '::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : 列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n'
__vars['help']['console']['logger'] = '简单的日志工具\n\n直接使用这些命令：\n1. log_debug    调试\n2. log_info     信息\n3. log_warning  警告\n4. log_error    错误\n5. log_critical 严重'


# 自定义函数
def cmd(command: str): os.system(command)
class ConsoleExit(Exception):
    def __init__(self, message: str = 'Console has exited.'):
        self.message = message
    def __str__(self):
        return self.message
    def __repr__(self):
        return self.message


class Logger:
    '''简单的日志工具'''
    # log 类型
    __log_map = {
        'info': '[Info]',
        'error': '[ERROR]',
        'warning': '[WARNING]',
        'debug': '[debug]',
        'critical': '[CRITICAL]'
    }
    def __init__(self, __level: str):
        self.level = __level
    def __call__(self, message: str):
        __level = self.__log_map[self.level]
        print(__level + ' ' + message)


# 这些都是已经实例化好的日志工具
log_debug = Logger('debug')
log_info = Logger('info')
log_warning = Logger('warning')
log_error = Logger('error')
log_critical = Logger('critical')


# 定义命令
def __cmd_help(__other_cmd: str):
    log_info('帮助')
    if __other_cmd.isspace() or __other_cmd == '':
        print(__vars['help']['console'])
    else: ...

def __cmd_cd(__other_cmd: str):
    global __vars
    if __other_cmd.isspace() or __other_cmd == '':
        log_info(__vars['path'])
    else:
        __path = __vars['path'] + '/' + __other_cmd
        __vars['path'] = __path
        if not os.path.exists(__path):
            log_error('目录不存在')
            os.mkdir(__path)
            log_debug('目录已创建')
        os.chdir(__path)
        log_info('工作目录已更改为 ' + __vars['path'] + '.')

def __cmd_mkdir(__other_cmd: str):
    if __other_cmd.isspace() or __other_cmd == '':
        log_error('mkdir 必须要指定目录名称')
    else:
        os.mkdir(__other_cmd)
        log_info('目录已创建')

def __cmd_cls(__none):
    cmd('cls')

def __cmd_dir(__none):
    cmd('dir')

def __cmd_rmdir(__other_cmd: str):
    if __other_cmd.isspace() or __other_cmd == '':
        log_error('rmdir 必须要指定目录名称')
    else:
        os.rmdir(__other_cmd)
        log_info('目录已删除')

def __cmd_pause(__none):
    print('请按 Enter 键继续...')
    input()

def __cmd_python(__other_cmd: str):
    cmd('python ' + __other_cmd)

def __cmd_version(__none):
    log_info(__vars['version'])

def __cmd_license(__none):
    log_info(__vars['license'])

def __cmd_echo(__other_cmd: str):
    print(__other_cmd)

def __cmd_exit(__none):
    log_info('Bye!')
    raise ConsoleExit

def __eg_plg(__none):
    print('ExamplePlugin')

__command_map = {
    'help': __cmd_help, 
    'cd': __cmd_cd,
    'md': __cmd_mkdir,
    'mkdir': __cmd_mkdir,
    'rd': __cmd_rmdir,
    'rmdir': __cmd_rmdir,
    'pause': __cmd_pause,
    'python': __cmd_python,
    'version': __cmd_version,
    'license': __cmd_license,
    'echo': __cmd_echo,
    'clear': __cmd_cls,
    'cls': __cmd_cls,
    'dir': __cmd_dir,
    'ls': __cmd_dir,
    'exit': __cmd_exit,
    'quit': __cmd_exit,
    'ExamplePlugin': __eg_plg,
}


def analysis_space(string: str):
    
    global __vars
    
    for __index in range(len(string)):
        __char = string[__index]
        match __char:
            case ' ':
                __vars['cmd']['space']['count'] += 1
                __vars['cmd']['space']['index'].append(__index)
    if __vars['cmd']['space']['count'] == 0:
        __vars['cmd']['space']['index'].append(len(string))


def analysis_cmd(command: str):

    global __vars
    global __command_map

    analysis_space(command)
    # 第一个空格
    __action = __command_map.get(command[0:__vars['cmd']['space']['index'][0]], None)
    if __action:
        __action(command[__vars['cmd']['space']['index'][0] + 1:])
    else:
        log_warning('command not found')


def main():
    print(__vars['welcome'])
    while True:
        input_str = input('>>> ')
        analysis_cmd(input_str)


if __name__ == '__main__':
    main()
