import os
import yaml

from my_logger import logger

# from mcdreforged.api.types import PluginServerInterface
from objprint import op


class Config:

    default_config = {
        'commands': {
            'enable': {
                'all': True,
                'server': {
                    'all':   True,  'exit': True,
                    'kill':  False, 'restart': True,
                    'start': True,  'stop': True,
                },
            },
            'permissions': {
                'server': {
                    'exit': 4, 'start': 4,
                    'kill': 4, 'stop': 3,
                    'restart': 3,
                    
                    
                },
            },
        },
        'wait_for_server': 20,
    }
    config = {}


    def __init__(self): ...


    def __check(self, config: dict, default_config: dict):
        def recursive_check(config: dict, default_config: dict):
            for key, value in default_config.items():
                if key not in config:
                    config[key] = value
                elif type(value) == type(config[key]) == dict:
                    recursive_check(config[key], value)
                elif not isinstance(config[key], type(value)):
                    logger.catch_exc('捕捉异常：TypeError')
                    logger.catch_exc(f'配置文件中键 {key} 的值不是 {type(value)} 类型数据')
                    logger.warning('配置错误，使用默认值代替')
                    config[key] = value

        recursive_check(config, default_config)
        self.save()


    def create_default_config(self):
        if not os.path.exists('./config/'): os.mkdir('./config')
        with open('./config/tools.yml', 'w', encoding='utf-8') as f:
            yaml.dump(self.default_config, f, allow_unicode=True)


    def load(self) -> dict:
        # check whether exist config file
        if not os.path.exists('./config/tools.yml'):
            logger.warning('未找到配置文件！')
            logger.warning('即将创建默认配置文件')
            self.create_default_config()

        # read config
        with open('./config/tools.yml', encoding='utf-8') as f:
            for cfgs in yaml.safe_load_all(f):
                self.config.update(cfgs)

        if self.config is {}:
            logger.crit('配置文件读取失败！')
            logger.crit('请在Github上提交一个PR反映此问题')
            raise SystemExit(1)
        self.__check(self.config, self.default_config)
        return self.config


    def save(self):
        with open('./config/tools.yml', 'w', encoding='utf-8') as f:
            yaml.dump(self.config, f, allow_unicode=True)


    def update_config_value(self, key, value):
        def recursive_update(cfg, key_list, value):
            if len(key_list) == 1:
                cfg[key_list[0]] = value
            else:
                recursive_update(
                    cfg[key_list[0]], key_list[1:], value
                )

        key_list = key.split('.')
        recursive_update(self.config, key_list, value)


if __name__ == '__main__':
    cfg = Config()
    cfg.create_default_config()
    op(cfg.config)
    cfg.load()
    op(cfg.config)
    cfg.update_config_value('commands.enable.server.kill', True)
    cfg.update_config_value('test', True)
    op(cfg.config)
    cfg.save()
