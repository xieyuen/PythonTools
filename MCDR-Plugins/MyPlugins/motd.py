from mcdreforged.api.all import *


PLUGIN_METADATA = {
    'id': 'motd',
    'version': '1.0.0',
    'name': 'MOTD',
    'description': {
        'en_us': "A plugin of joined players' MOTD",
        'zh_cn': '玩家加入MOTD插件(单文件)'
    },
    'author': 'xieyuen',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    },
}


def on_load(server: PluginServerInterface, prev_module):
    server.logger.info('MOTD插件已加载')


def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    server.say(f'欢迎 {player} 加入本服务器')
    server.logger.info(f'玩家 {player} 加入服务器')