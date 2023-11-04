import os
import json
import yaml

from loguru import logger

from utils import sha256


config: dict = {}
user_data: list = []
default_config: dict = {}
default_user_data: list[dict] = [
    {
        'username': 'root',
        'password': sha256('root'),
        'enable': False,
    }
]


def create_default_config():
    with open('./config.yml', 'w', encoding='utf-8') as cfg_file:
        yaml.safe_dump(default_config, cfg_file, default_flow_style=False, allow_unicode=True)


def load_config() -> dict:
    """
    Loads the config file
    """
    global config

    while True:
        logger.info('Loading config file')

        if os.path.exists('./config.yml'):
            with open('./config.yml', 'r', encoding='utf-8') as cfg_file:
                config = yaml.safe_load(cfg_file)
            break

        if os.path.exists('./config.json'):
            logger.warning('Config file is in JSON format, converting to YAML')
            with open('./config.json', 'r') as cfg_file:
                config = json.load(cfg_file)

            with open('./config.yml', 'w', encoding='utf-8') as cfg_file:
                yaml.safe_dump(config, cfg_file, default_flow_style=False, allow_unicode=True)
            os.remove('./config.json')
            break

        logger.error('Config file not found')
        logger.debug('Creating default config file')
        create_default_config()
    return config


def create_default_user_data():
    if not os.path.exists('./data/'):
        os.mkdir('./data/')
    with open("./data/user_data.json", "w", encoding='utf-8') as user_data_file:
        json.dump(default_user_data, user_data_file, indent=4)


def load_user_data() -> list:
    """
    Loads the user data file
    """
    global user_data
    if not os.path.exists('./data/user_data.json'):
        logger.warning('User data file not found, creating new one')
        create_default_user_data()
    with open("./data/user_data.json", "r", encoding='utf-8') as jsonfile:
        user_data = json.load(jsonfile)
    for acc in user_data:
        if not default_user_data[0].keys() == acc.keys():
            logger.error('Invalid user data file, removing it')
            create_default_user_data()
            user_data = default_user_data.copy()
            break
    return user_data


def save_user_data(new):
    with open("./data/user_data.json", "w", encoding='utf-8') as user_data_file:
        json.dump(new, user_data_file, indent=4)
