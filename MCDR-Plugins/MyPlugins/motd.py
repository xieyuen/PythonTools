from mcdreforged.api.all import *


PLUGIN_METADATA = {
    'id': 'motd',
    'version': '1.0.0',
    'name': 'MOTD',
    'description': {
        'en_us': "A plugin of joined players' MOTD",
        'zh_cn': '玩家加入 MOTD 插件(单文件)'
    },
    'author': 'xieyuen',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    },
}


class Server:
    def server(server: PluginServerInterface):
        server.tell()

    def help(server: PluginServerInterface):
        ...


def on_load(server: PluginServerInterface, prev_module):
    server.logger.info('MOTD插件已加载')
    server.register_command(
        Literal('@server')
        .requires(lambda src: src.has_permission(1))
        .runs(Server.server)
        .then(
            Literal('help')
            .runs(Server.help)
        )
    )


def on_player_joined(server: PluginServerInterface, player: str, info: Info):
    server.say(f'欢迎 {player} 加入本服务器')
    server.tell(player, '欢迎进入星云生电服务器！')
    server.execute_command(f'gamemode survival {player}')
    server.execute_command(f'sudo {player} chat !!help')
    server.execute_command(f'sudo {player} chat !!days')
    server.tell(player, '若有更多疑问，请输入 @server help 获取帮助')
    server.logger.info(f'玩家 {player} 加入服务器')
