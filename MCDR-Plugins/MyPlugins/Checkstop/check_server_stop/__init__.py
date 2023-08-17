#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import time
from mcdreforged.api.all import PluginServerInterface as mcdrserver


def stop_server():
    mcdrserver.stop()
    time.sleep(10)
    if mcdrserver.is_server_running()==True: 
        time.sleep(60)
        if mcdrserver.is_server_running() == True:
            mcdrserver.logger.warning("服务器似乎并没有关闭...")
            mcdrserver.logger.info("10s后服务端进程将被杀死.")
            time.sleep(10)
            mcdrserver.set_exit_after_stop_flag(False)
            if mcdrserver.is_server_running() == False: 
                mcdrserver.logger.info("服务端已关闭")
            else:
                mcdrserver.set_exit_after_stop_flag(False)
                mcdrserver.kill()
    mcdrserver.logger.info("服务端已关闭.")


def stop_exit_server():
    stop_server()
    mcdrserver.exit()


def restart_server():
    stop_server()
    mcdrserver.start()


def on_load():
    mcdrserver.logger.info("插件已加载")
    mcdrserver.logger.info("Powered by xieyuen")
    mcdrserver.register_command(
        Literal('!!server_').
            requires(lambda src: src.has_permission(4)).
            runs(
            lambda src: src.reply(server.rtr('start_stop_helper_r.help'))
        ).
            then(
            Literal('start').
                requires(lambda src: src.has_permission(4)).
                runs(lambda src: mcdrserver.start())
        ).
            then(
            Literal('stop').
                requires(lambda src: src.has_permission(4)).
                runs(lambda src: stop_server())
        ).
            then(
            Literal('stop_exit').
                requires(
                lambda src: src.has_permission(4)).
                runs(lambda src: stop_exit_server())
        ).
            then(
            Literal('restart').
                requires(
                lambda src: src.has_permission(4)).
                runs(lambda src: mcdrserver.restart())
        ).
            then(
            Literal('exit').
                requires(lambda src: src.has_permission(4)).
                runs(lambda src: mcdrserver.exit())
        )
    )



'''
mcdrserver.register_command("!!check_stop stop")
mcdrserver.register_command("!!check_stop no")

@new_thread('CheckStop')
def check(server: PluginServerInterface):
    while True:
        _check_running = mcdrserver.is_server_running()
        _check_rcon = mcdrserver.is_rcon_running()
        
        if (_check_running == True) and (_check_rcon == False):
            time.sleep(60)
            _check_running = mcdrserver.is_server_running()
            _check_rcon = mcdrserver.is_rcon_running()
            if (_check_running == True) and (_check_rcon == False):
                mcdrserver.logger.warning("服务端似乎在关闭时卡死了？")
                mcdrserver.logger.warning("服务端进程将会在确认后的10s内被杀死")
                mcdrserver.logger.warning("届时 MCDR 将不会退出")
                mcdrserver.logger.warning("请输入 !!check_stop stop 确认，或输入 !!check_stop no 取消")
            else: continue
        else: continue
'''
