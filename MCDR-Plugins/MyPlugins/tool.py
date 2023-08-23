import os
import time
from platform import system

from mcdreforged.api.all import *

PLUGIN_METADATA = {
    'id': 'tool_plugin',
    'version': '1.0.0',
    'name': 'Tool Plugin',
    'description': {
        'en_us': 'A tool plugin',
        'zh_cn': '服务器工具(单文件)'
    },
    'author': 'xieyuen',
    'dependencies': {
        'mcdreforged': '>=2.0.0',
    },
}


class Commands:
    def __init__(self):
        self.server = self.ServerControl()

    class ServerControl:
        def __init__(self):
            ...

        def start(self, server: PluginServerInterface):
            server.start()
            server.logger.info('服务器已开启')

        def stop(self, server: PluginServerInterface):
            server.logger.info('服务器关闭')
            server.stop()

            # wait 20 secs
            time.sleep(20)

            if server.is_server_running:
                server.logger.info('服务器似乎卡死了')
                server.logger.info('3s 后将会杀死服务端')
                time.sleep(3)

                server_pid = server.get_server_pid()
                if system() == 'Windows':
                    # Windows
                    os.system(f'taskkill /f /pid {server_pid}')
                else:
                    server.kill()

            server.logger.info('服务端已停止')

        def exit(self, server: PluginServerInterface):
            if server.is_server_running():
                self.stop()
            server.exit()

        def restart(self, server: PluginServerInterface):
            self.stop()
            self.start()

    def run(self, command: str):
        exec(command)

    @new_thread('refresh_plugin')
    def refresh_all_plugins(self, server: PluginServerInterface, player: str | None = None):
        server.refresh_all_plugins()
        if (player is not None) and player != 'console':
            server.say('全部插件已重新加载')
        server.logger.info(f'{player} 刷新了全部插件')
        return True

    @new_thread('refresh_plugin')
    def refresh_changed_plugins(self, server: PluginServerInterface):
        server.refresh_changed_plugins()
        server.boardcast('已重新加载有变化的插件')
        return True

    def seed(self, server: PluginServerInterface):
        server.execute_command('seed')


cmds = Commands()


def on_load(server: PluginServerInterface, prev_module):
    server.logger.info('插件已加载')
    server.logger.warning('此插件为单文件插件！')
    server.logger.warning('此插件为单文件插件！')
    server.logger.warning('此插件为单文件插件！')
    server.logger.info('Powered by xieyuen')

    server.register_help_message(
        '!!tools',
        '一个小工具'
    )

    server.register_command(
        Literal('!!tools')
        .requires(lambda src: src.has_permission(1))
        .runs(
            lambda src: src.reply(server.rtr('tool_plugin.help'))
        ).then(
            Literal('server')
            .requires(lambda src: src.has_permission(3))
            .then(
                Literal('start')
                .runs(cmds.server.start)
                .requires(lambda src: src.has_permission(4))
            ).then(
                Literal('stop')
                .runs(cmds.server.stop)
                .requires(lambda src: src.has_permission(3))
            ).then(
                Literal('exit')
                .runs(cmds.server.exit)
                .requires(lambda src: src.has_permission(4))
            ).then(
                Literal('restart')
                .runs(cmds.server.restart)
                .requires(lambda src: src.has_permission(3))
            )
        ).then(
            Literal('plugin')
            .requires(lambda src: src.has_permission(2))
            .then(
                Literal('refresh')
                .requires(lambda src: src.has_permission(3))
                .then(
                    Literal('all')
                    .runs(cmds.refresh_all_plugins)
                ).then(
                    Literal('changed')
                    .runs(cmds.refresh_changed_plugins)
                )
            )
        ).then(
            Literal('seed')
            .requires(lambda src: src.has_permission(2))
            .runs(cmds.seed)
        )
    )
