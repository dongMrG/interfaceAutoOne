# -*- coding: utf-8 -*-
# @Time : 2022-04-12 14:23
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_path.py

#自动获取文件路径
import os
#当前文件路径
# print(__file__)
#上层目录
# print(os.path.dirname(__file__))
#1、工程路径
project_path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
#2、配置路径
config_path = os.path.join(project_path,'configs')
# print(config_path)
#3、配置文件
data_path = os.path.join(project_path,'data')
#4、api配置文件
api_path = os.path.join(project_path,'configs')
# print(data_path)
#allure报告
report_path = os.path.join(project_path,r'outFiles\report\tmp')
#log日志
logs_path = os.path.join(project_path,r'outFiles\log')


