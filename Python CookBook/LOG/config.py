# -*- coding: utf-8 -*-
# @Time : 2021/07/08 10:01
# @Author : yunshan
# @File : config.py
import logging
import logging.config
import yaml
logger = logging.getLogger(__name__)

if __name__ == '__main__':
    with open('./config.yaml','r') as f:
        config = yaml.safe_load(f.read())
    logging.config.dictConfig(config)