# -*- coding: utf-8 -*-

import time

from mcdreforged.api.all import *


player_died = LiteralEvent('player_died')


def on_load(server: PluginServerInterface, prev_module):
    server.register_event_listener(on_player_died, player_died)
    
    server.logger.info("插件已加载")
    server.logger.info("Powered by xieyuen")


@new_thread('checkstop')
def on_server_stop(server: PluginServerInterface, server_return_code: int):
    ...