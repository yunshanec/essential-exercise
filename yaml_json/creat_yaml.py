# -*- coding: utf-8 -*-
# @Time : 2021/07/09 13:08
# @Author : yunshan
# @File : creat_yaml.py
import os
from ruamel.yaml import YAML
import yaml

# create yaml object
yaml1 =YAML()
py_dict = {
    'name':'xiao ming',
    'age':[18,19]
}

with open('./new_yaml_file.yaml','w',encoding='utf-8') as file:
    yaml1.dump(py_dict,file)

# load yaml file
with open('./new_yaml_file.yaml','r',encoding='utf-8') as yaml_data:
    data = yaml_data.read()

result = yaml.load(data)
print(result)
# print(result)
# for data in result:
#     print(data)