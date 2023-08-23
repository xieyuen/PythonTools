import os
import yaml
from mymodule.api.logger import logger

_variables = {
    'beMapped': [
        '遍历',
        '循环',
        '定义函数',
        '定义类',
        '从',
        '导入',
        '在',
        '是',
        '【',
        '】',
        '（',
        '）',
        '“',
        '”',
        "‘",
        "’",
        '小于等于',
        '大于等于',
        '大于',
        '小于',
        '不等于',
        '等于',
        '赋值为',
        '加',
        '减',
        '乘',
        '除以',
        '模',
        '整除',
        '的',
        '获取输入',
    ],
    'mapped': [
        'for',
        'while',
        'def',
        'class',
        'from',
        'import',
        'in',
        'is',
        '[',
        ']',
        '(',
        ')',
        '"',
        '"',
        "'",
        "'",
        '>=',
        '<=',
        '>',
        '<',
        '!=',
        '==',
        '=',
        '+',
        '-',
        '*',
        '/',
        '%',
        '//',
        '**',
        'input',
    ],
    'default': {
        i: j
        for i, j in zip(_variables['beMapped'], _variables['mapped'])
    },
}


def main():
    # open map and safe config
    with open('./map.yaml', encoding='utf-8') as f:
        _map = yaml.safe_load(f)

    # 检测默认 map
    if _map['default'] != _variables['default']:
        logger.critical('默认 map 不正确')
        _map['default'] = _variables['default']
        with open('./map.yaml', 'w', encoding='utf-8') as f:
            yaml.safe_dump(_map, f, encoding='utf-8')

        logger.debug('map 文件已重置')
        return -1

    # 打开 main.py, 加载文件内容，进行重写
    with open('./main.py', encoding='utf-8') as f:
        _main = f.read()

    for bem, m in _map['map'].items():
        _main.replace(bem, m)

    # 生成临时文件
    with open('./temp.py', 'w', encoding='utf-8') as f:
        f.write(_main)

    # 运行
    os.chdir(os.path.split(os.path.realpath(__file__))[0])
    os.system('python temp.py')

    # 移除文件
    os.remove('./temp.py')

    return 0


if __name__ == '__main__':
    main()
