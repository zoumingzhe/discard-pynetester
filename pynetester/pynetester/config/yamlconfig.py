#!/usr/bin/env python3
# coding=utf-8
# ----------------------------------------------------------------------------------------------------
import yaml
import os
# ----------------------------------------------------------------------------------------------------
# 类 yamlconfig
# ----------------------------------------------------------------------------------------------------
# 变更履历：
# 2021-05-19 | Zou Mingzhe   | Ver0.1  | 初始版本
# ----------------------------------------------------------------------------------------------------
# MAP：
# 未测试 | load_default(...)            | 导入默认配置
# 未测试 | load(...)                    | 导入配置
# 未测试 | merge(...)                   | 合并配置
# ----------------------------------------------------------------------------------------------------
class yamlconfig:
    """
    yamlconfig类。
    """
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def load_default(config_name = 'default.yaml'):
        cata = os.path.dirname(__file__)
        path = os.path.join(cata, config_name)
        return yamlconfig.load(path)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def load(config_path):
        with open(config_path, 'r') as f:
            return yaml.load(f, yaml.FullLoader)
# ----------------------------------------------------------------------------------------------------
    @staticmethod
    def merge(config1, config2):
        config = {}
        for key in config1:
            config[key] = config1[key]
        for key in config2:
            conf = config2[key]
            if key not in config:
                config[key] = conf
            # elif type(config[key]) == type(conf):
            #     config[key] = merge(config[key], conf)
            # else:
            #     print("error")
        return config
# ----------------------------------------------------------------------------------------------------
