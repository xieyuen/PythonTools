from ..console import global_vars

def space(string: str):

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


def cmd(command: str):

    global global_vars
    global command_map
    __1st_space = analysis_space(command)['index'][0]

    del __action

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
        logger.warning(f'Command {header} not found')
