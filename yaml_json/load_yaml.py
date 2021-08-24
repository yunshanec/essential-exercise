# -*- coding: utf-8 -*-
# @Time : 2021/07/09 11:47
# @Author : yunshan
# @File : load_yaml.py

import yaml
import os

yaml_file = os.path.join('./yaml_practice1.yaml')
with open(yaml_file,'r',encoding='utf-8') as f:
    data = f.read()

yaml_data = yaml.load_all(data)

# 读取多个ymal文档
for data in yaml_data:
    print(data)