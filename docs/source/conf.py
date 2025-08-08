# Configuration file for the Sphinx documentation builder.
#
# For the full list of built-in configuration values, see the documentation:
# https://www.sphinx-doc.org/en/master/usage/configuration.html

# -- Project information -----------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#project-information

project = 'PythonTools'
copyright = '2025, xieyuen'
author = 'xieyuen'
release = '0.2.1'

# -- General configuration ---------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#general-configuration

extensions = [
    'myst_parser',
    'sphinx.ext.autodoc',
    'sphinx.ext.viewcode',
    'sphinx.ext.napoleon'
]
source_suffix = {
    '.rst': 'restructuredtext',
    '.md': 'markdown',
}
templates_path = ['_templates']
exclude_patterns = []

language = 'zh_CN'

# -- Options for HTML output -------------------------------------------------
# https://www.sphinx-doc.org/en/master/usage/configuration.html#options-for-html-output

# html_theme = 'alabaster'
html_theme = 'sphinx_rtd_theme'  # 更现代化的主题:cite[3]:cite[10]
html_static_path = ['_static']


# 调整目录
import os
import sys

sys.path.insert(0, os.path.abspath('../../src'))  # 调整路径指向你的代码目录

# autodoc
autodoc_mock_imports = ['numpy', 'pandas', 'scipy']
autodoc_default_options = {
    'members': True,           # 显示所有成员（包括 properties）
    'undoc-members': True,    # 显示未文档化的成员
    'member-order': 'bysource',  # 按源码顺序排列
    # 'special-members': '__init__',  # 可选：显示 `__init__`
    # 'exclude-members': '__weakref__',  # 可选：排除某些成员
    'separate-members': True,  # 关键配置：每个成员（包括 property）独立一行
    'autofunction': 'show-inheritance',
    'show-signature': True
}
