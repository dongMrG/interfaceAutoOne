# -*- coding: utf-8 -*-
# @Time : 2022-03-30 9:54
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_yml.py

import yaml
def get_yaml_data(fileDir):
    '''
    :param fileDir: 文件路径
    :return:
    '''
    #1- 文件在磁盘---open函数----在内存去打印
    with open(fileDir,encoding='utf-8') as f:
        return yaml.safe_load(f.read())#使用yaml加载方法的到文件内容

if __name__ == '__main__':
    #TODO 项目中一般用工程的绝对路径
    res = get_yaml_data('../configs/apiConfig.yml')
    print(res)