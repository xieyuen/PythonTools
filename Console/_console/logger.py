'''

控制台的日志工具

有5种，import后就可以用了
e.g.
```py
import logger

logger.debug('hello world')
logger.info('hello world')
logger.warning('hello world')
logger.error('hello world')
logger.critical('hello world')

```

'''

from ..console import global_vars

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

# class LogOutput:
#     '''日志集成'''
#     def __init__(self):
#         self.debug = Logger('debug')
#         self.info = Logger('info')
#         self.warning = Logger('warning')
#         self.error = Logger('error')
#         self.critical = Logger('critical')
#     def debug(self, msg): self.debug(msg)
#     def info(self, msg): self.info(msg)
#     def warning(self, msg): self.warning(msg)
#     def warn(self, msg): self.warning(msg)
#     def error(self, msg): self.error(msg)
#     def critical(self, msg): self.critical(msg)

# 生成实例
# log = LogOutput()
debug = Logger('debug')
info = Logger('info')
warn = warning = Logger('warning')
error = Logger('error')
critical = Logger('critical')
