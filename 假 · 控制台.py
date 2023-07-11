# 假 · 控制台
import os

# 定义全局变量
__vars = {
    'path': os.getcwd(),
    'echo': 'on',
    'version': '0.0.1',
    'help': {}
}
__vars['welcome'] = 'Welcome to use console'
# 命令帮助
__vars['help']['console'] = '::: Help :::\nConsole help massage:\n\ncommands:\ncd <path> : 改变工作路径\ncls : 清空屏幕\ndir : 列出目录下的所有文件(夹)\nls : 列出目录下的所有文件(夹)\necho *args : 回显\nhelp : 显示此页面，后加命令名可获取该命令的详细帮助\npause : pause console\npython : 调用 python 命令/函数/方法\nversion : 版本信息\nexit : 退出控制台\n'
__vars['help']['plugin'] = {}

# log 类型 
def Console_info(): # info 
    print('[Console]',end='')
    print('[INFO] ',end='')
def Console_error(): # error
    print('[Console]',end='')
    print('[ERROR] ',end='')
def Console_warning(): # warning
    print('[Console]',end='')
    print('[WARNING] ',end='')
def Console_debug(): # debug
    print('[Console]',end='')
    print('[DEBUG] ',end='')


def main():
    print(__vars['welcome'])
    while True:
        input_str = input('>>> ')
        analysis(input_str)


def analysis(command: str):

    global __vars
    __space = {
        'count': 0,
        'index': []
    }

    for __index in range(len(command)):
        __char = command[__index]
        match __char:
            case ' ':
                __space['count'] += 1
                __space['index'].append(__index)


    # 第一个空格
    match command[:__space[0]]:
        case 'cd':
            os.chdir(command[__space[0]:])

        case 'cls':
            os.system('cls')

        case 'dir'|'ls':
            os.system('dir')

        case 'echo':
            if command[__space[0]:].find('on') == -1:
                if command[__space[0]:].find('off') == -1:
                    print(command[__space[0]:])
                else:
                    Console_info()
                    print('回显已关闭')
                    __vars['echo'] = 'off'
            else:
                if __echo: Console_warning()
                else:
                    Console_info()
                    __vars['echo'] = 'on'
                print('回显已开启')

        case 'help':
            __help()

        case 'pause':
            Console_info()
            print('请按任意键继续...')
            pass
        
        case 'python'|'py':
            os.system('py' + command[[__space][0]:])

        case 'read':
            print('read')

        case 'type':
            print('type')

        case 'ver':
            print('ver')

        case 'write':
            print('write')

        case 'exit'|'quit':
            print('Console will exit')
            exit()

        case _:
            print(f'[ERROR] Command "{ command }" is not found')


def __help():
    Console_info()
    print(__vars['help']['console'])
