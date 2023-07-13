# 自己做一个控制台
import os
import sys
import shutil

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
    'debug':    '\033[34m', # 蓝色
    'info':     '\033[92m', # 绿色
    'warning':  '\033[93m', # 橙色
    'error':    '\033[91m', # 红色
    'critical': '\033[31;1m' # 红色加粗
}
# 命令帮助
global_vars['help']['console']['baseCmd'] = '::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : 列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n'
global_vars['help']['console']['logger'] = '简单的日志工具\n\n直接使用这些命令：\n1. console.logger.debug    调试\n2. console.logger.info     信息\n3. console.logger.warning  警告\n4. console.logger.error    错误\n5. log_critical 严重'

# ---------------------------------------------------------------------------------------------

class Console:
    '''控制台工具'''
    
    class Logger:
        '''日志工具'''
        
        class LogPrint:
            '''日志打印'''

            global global_vars
            __log_color = global_vars['console']['logger']
            if __log_color == 'default': # 默认
                __log_color = global_vars['console']['logger'] = { # 日志颜色
                    'debug':    '\033[34m', # 蓝色
                    'info':     '\033[92m', # 绿色
                    'warning':  '\033[93m', # 橙色
                    'error':    '\033[91m', # 红色
                    'critical': '\033[31;1m' # 红色加粗
                }
            __log_map = {
                'debug':    __log_color['debug']    + '[debug]',
                'info':     __log_color['info']     + '[Info]',
                'error':    __log_color['error']    + '[ERROR]',
                'warning':  __log_color['warning']  + '[WARNING]',
                'critical': __log_color['critical'] + '[CRITICAL]'
            }
            def __init__(self, __level: str): self.level = __level

            def __call__(self, message: str):
                if self.level != 'catch_exc':
                    __level = self.__log_map[self.level]

                    if self.level == 'debug' or self.level == 'info':
                        print(__level + '\033[0m ' + message)
                    else: print(__level + ' ' + message + '\033[0m')

                else: print('\033[93m[CatchExc]' + __log_map['info'] + '\033[0m ' + message)

        def __init__(self): # 实例化
            self.__debug     = self.LogPrint('debug')
            self.__info      = self.LogPrint('info')
            self.__warning   = self.LogPrint('warning')
            self.__error     = self.LogPrint('error')
            self.__critical  = self.LogPrint('critical')
            self.__catch_exc = self.LogPrint('catch_exc')
        # 定义日志打印方法
        def debug(self, msg):    self.__debug(msg)    # debug    日志
        def info(self, msg):     self.__info(msg)     # info     日志
        def warning(self, msg):  self.__warning(msg)  # warning  日志
        def warn(self, msg):     self.__warning(msg)  # warning  日志
        def error(self, msg):    self.__error(msg)    # error    日志
        def critical(self, msg): self.__critical(msg) # critical 日志
        def crit(self, msg):     self.__critical(msg) # critical 日志
        # 异常日志
        def catch_exc(self, msg): self.__catch_exc(msg)
        def exception(self, msg, exc_msg):
            '''这会打印 critical 级别的日志再抛出 ConsoleException 异常'''
            self.critical(msg)
            raise ConsoleException(exc_msg)

    class CustomCmds:
        '''自定义命令'''
        def __init__(self): ...
        def cmd(self, command: str): os.system(command)

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

console = Console()
cmd = console.custom_cmds.cmd

# ---------------------------------------------------------------------------------------------

# 定义命令
class ConsoleCmd:
    '''控制台命令'''
    def help(__other_cmd: str):
        console.logger.info('帮助')
        if __other_cmd.isspace() or __other_cmd == '':
            console.logger.info('Help Massage:')
            print(global_vars['help']['console'])
        else:
            if __other_cmd in global_vars['help']:
                console.logger.info(global_vars['help'][__other_cmd])
            else: console.logger.warning(f'未找到 {__other_cmd } 的帮助！')
        return None

    def cd(__other_cmd: str):
        global global_vars
        if __other_cmd.isspace() or __other_cmd == '':
            console.logger.info(global_vars['path'])
            return global_vars['path']

        __path = __other_cmd
        if not os.path.exists(__path):
            console.logger.error('目录不存在')
            os.mkdir(__path)
            console.logger.debug('目录已创建')
        os.chdir(__path)
        global_vars['path'] = os.getcwd()
        console.logger.info('工作目录已更改为 ' + global_vars['path'] + '.')
        return True

    def mkdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            console.logger.error('mkdir 必须要指定目录名称')
            return False
        os.mkdir(__other_cmd)
        console.logger.info('目录已创建')
        return True

    def rmdir(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            console.logger.error('rmdir 必须要指定目录名称')
        else:
            try:
                os.rmdir(__other_cmd)
                console.logger.info('目录已删除')
            except OSError:
                console.logger.error('目录非空')
                console.logger.error('是否强制删除目录？这会会删除目录下的所有文件(夹)')
                ans = input('输入 y 确认，其他任意键取消：')
                if ans == 'y':
                    try:
                        shutil.rmtree(__other_cmd)
                        console.logger.info('目录已删除')
                        return True
                    except:
                        console.logger.catch_exc('Python 抛出了一个异常')
                        console.logger.error('目录删除失败')
                console.logger.info('目录删除操作取消')
            except: console.logger.catch_exc('好像触发了什么奇奇怪怪的异常？')
            return False

    def del_(__other_cmd: str):
        if __other_cmd.isspace() or __other_cmd == '':
            console.logger.error('del 必须要指定文件名称')
            return False
        if not os.path.exists(__other_cmd):
            console.logger.error('文件不存在')
            return False
        try: os.remove(__other_cmd)
        except: console.logger.catch_exc('好像触发了什么奇奇怪怪的异常？')
        else:
            console.logger.info('文件已删除')
            return True

    def pause(__none):
        console.logger.info('请按 Enter 键继续...')
        input()

    def version(__none):
        console.logger.info(global_vars['version'])

    def license_(__none):
        console.logger.info(global_vars['console']['license'])

    def echo_(__other_cmd: str):
        print(rf'{__other_cmd}')

    def exit_(__none):
        console.logger.info('Bye!')
        console.exception.exc_msg('Console has exited.')
        raise console.exception

    def plg(__other_cmd: str):
        console.logger.info('plugin')
        print(__other_cmd)
        console.logger.info(global_vars['plugin'])

command_map = {
    'help':    ConsoleCmd.help,
    'cd':      ConsoleCmd.cd,
    'md':      ConsoleCmd.mkdir,
    'mkdir':   ConsoleCmd.mkdir,
    'rd':      ConsoleCmd.rmdir,
    'rmdir':   ConsoleCmd.rmdir,
    'pause':   ConsoleCmd.pause,
    'version': ConsoleCmd.version,
    'license': ConsoleCmd.license_,
    'echo':    ConsoleCmd.echo_,
    'del':     ConsoleCmd.del_,

    'plugin': ConsoleCmd.plg
}

# ---------------------------------------------------------------------------------------------

def main():
    console.logger.info(global_vars['welcome'])
    while True:
        input_str = input('>>> ')
        if input_str == 'exit' or input_str == 'quit' or input_str == '':
            ConsoleCmd.exit_(None)
        
        global global_vars
        __space = global_vars['temp']['cmd']['space']

        for __index in range(len(input_str)):
            __char = input_str[__index]
            if __char == ' ':
                __space['count'] += 1
                __space['index'].append(__index)
        if __space['count'] == 0:
            __space['index'].append(len(input_str))

        global_vars['temp']['cmd']['space'] = __space

        __1st_space = __space['index'][0]
        __action = command_map.get(input_str[0:__1st_space], None)

        if __action:
            __action(input_str[__1st_space + 1:])
        else:
            console.logger.warning('input_str not found')

        del __action


if __name__ == '__main__':
    main()
