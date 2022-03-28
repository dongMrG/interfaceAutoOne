# -*- coding: utf-8 -*-
# @Time : 2022-03-31 11:14
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_yaml.py

import yaml

#读取文件
def get_yaml_data(fileDir):
    with open(fileDir,encoding='utf-8') as f:
        return yaml.safe_load(f.read())

if __name__ == '__main__':
    res = get_yaml_data('../configs/apiConfig.yml')
    print(res)