import os

import logger

from ..console import global_vars

# 自定义函数
def cmd(command: str): os.system(command)
class ConsoleExit(Exception):
    def __init__(self, message: str = 'Console has exited.'):
        self.message = message
    def __str__(self):
        return self.message


def help(__other_cmd: str):
    logger.info('帮助')
    if __other_cmd.isspace() or __other_cmd == '':
        logger.info('Help Massage:')
        print(global_vars['help']['console'])
    else:
        if __other_cmd in global_vars['help']:
            logger.info(global_vars['help'][__other_cmd])
        else: logger.warning(f'未找到 {__other_cmd } 的帮助！')
    return     

def cd(__other_cmd: str):
    global global_vars
    if __other_cmd.isspace() or __other_cmd == '':
        logger.info(global_vars['path'])
    else:
        __path = global_vars['path'] + '/' + __other_cmd
        global_vars['path'] = __path
        if not os.path.exists(__path):
            logger.error('目录不存在')
            os.mkdir(__path)
            logger.debug('目录已创建')
        os.chdir(__path)
        logger.info('工作目录已更改为 ' + global_vars['path'] + '.')

def mkdir(__other_cmd: str):
    if __other_cmd.isspace() or __other_cmd == '':
        logger.error('mkdir 必须要指定目录名称')
    else:
        os.mkdir(__other_cmd)
        logger.info('目录已创建')

def cls(__none):
    cmd('cls')

def dir(__none):
    print(cmd('dir'))

def rmdir(__other_cmd: str):
    if __other_cmd.isspace() or __other_cmd == '':
        logger.error('rmdir 必须要指定目录名称')
    else:
        os.rmdir(__other_cmd)
        logger.info('目录已删除')

def pause(__none):
    logger.info('请按 Enter 键继续...')
    input()

def version(__none):
    logger.info(global_vars['version'])

def license(__none):
    logger.info(global_vars['license'])

def echo(__other_cmd: str):
    print(__other_cmd)

def exit(__none):
    logger.info('Bye!')
    raise ConsoleExit

def plg(__other_cmd: str):
    logger.info('plugin')
    print(__other_cmd)
    logger.info(global_vars['plugin'])
