#!/usr/bin/env python
# -*- coding:utf-8 -*-
'''
-----------------------------------------------------------
    @FileName  :read_config_data.py
    @Time      :2023/6/10 14:19
    @Author    :LittleSeven
    @Address   ：https://gitee.com/linguchong/Django_Project_Demo.git
-----------------------------------------------------------
'''
import os
from typing import Text
from config.models import Config
from get_yaml_data.yaml_data import GetYamlData

def root_path():
    """ 获取 根路径 """
    path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    return path

def ensure_path_sep(path: Text) -> Text:
    """兼容 windows 和 linux 不同环境的操作系统路径 """
    if "/" in path:
        path = os.sep.join(path.split("/"))

    if "\\" in path:
        path = os.sep.join(path.split("\\"))

    return root_path() + path

def read_config():
    res = GetYamlData(r"/Users/z.m/pythonProject/Interface_Auto_Test/common/config.yaml").get_yaml_data()
    config = Config(**res)
    return config

if __name__ == '__main__':
    print(read_config())
