# -*- coding: utf-8 -*-
from typing import Dict

from mcdreforged.api.types import PluginServerInterface
from mcdreforged.api.command import *
from mcdreforged.api.utils import Serializable

import time


class Config(Serializable):
    permissions: Dict[str, int] = {
        'help': 3,
        'start': 3,
        'stop': 3,
        'stop_exit': 4,
        'restart': 3,
        'exit': 4,
        'kill': 4,
    }


config: Config


def stop_server(server: PluginServerInterface):
    server.stop()
    time.sleep(20)
    if server.is_server_running:
        server.logger.warning("服务器似乎卡死了")
        server.logger.info("3s后将会杀死服务端")
        time.sleep(3)
        server.kill()

def exit_server(server: PluginServerInterface):
    try:
        stop_server()
    finally:
        server.exit()

def restart_server(server: PluginServerInterface):
    try:
        stop_server()
    except:...
    server.start()


def on_load(server: PluginServerInterface, prev_module):

    server.logger.info("插件已加载")
    server.logger.warning("你使用的并非原版！而是 xieyuen 修改版!")
    server.logger.warning("若需要原版，请在下面的网址下载（或者用MPM）")
    server.logger.warning("https://www.mcdreforged.org/plugins/start_stop_helper_r")
    server.logger.warning("或者用 MPM")

    global config
    config = server.load_config_simple('config.json', target_class=Config)
    permissions = config.permissions
    server.register_help_message(
        '!!server',
        {
            'en_us': 'Start and stop server helper',
            'zh_cn': '开关服助手'
        }
    )
    server.register_command(
        Literal('!!server').
            requires(lambda src: src.has_permission(permissions['help'])).
            runs(
            lambda src: src.reply(server.rtr('start_stop_helper_r_changed.help'))
        ).
            then(
            Literal('start').
                requires(lambda src: src.has_permission(permissions['start'])).
                runs(lambda src: server.start())
        ).
            then(
            Literal('stop').
                requires(lambda src: src.has_permission(permissions['stop'])).
                runs(lambda src: stop_server())
        ).
            then(
            Literal('stop_exit').
                requires(
                lambda src: src.has_permission(permissions['stop_exit'])).
                runs(lambda src: exit_server())
        ).
            then(
            Literal('restart').
                requires(
                lambda src: src.has_permission(permissions['restart'])).
                runs(lambda src: restart_server())
        ).
            then(
            Literal('exit').
                requires(lambda src: src.has_permission(permissions['exit'])).
                runs(lambda src: server.exit())
        ).
            then(
            Literal('kill').
                requires(lambda src: src.has_permission(permissions['kill'])).
                runs(lambda src: server.kill())
        ).
            then(
            Literal('exit2').
                requires(lambda src: src.has_permission(permissions['exit'])).
                runs(lambda src: exit_server())
        )
    )
