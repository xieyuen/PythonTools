# 自己做一个控制台

from _console import logger, analysis

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
global_vars['help']['console']['logger'] = '简单的日志工具\n\n直接使用这些命令：\n1. logger.debug    调试\n2. logger.info     信息\n3. logger.warning  警告\n4. logger.error    错误\n5. log_critical 严重'


# 自定义函数
def cmd(command: str): os.system(command)
class ConsoleExit(Exception):
    def __init__(self, message: str = 'Console has exited.'):
        self.message = message
    def __str__(self):
        return self.message

def main():
    logger.info(global_vars['welcome'])
    while True:
        input_str = input('>>> ')
        analysis_cmd(input_str)


if __name__ == '__main__':
    main()
