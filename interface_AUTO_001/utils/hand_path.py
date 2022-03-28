# -*- coding: utf-8 -*-
# @Time : 2022-03-30 17:20
# @Author : DXS
# @Email : 756444819@qq.com
# @File : hand_path.py
import os
'''
需求： 代码在任意路径都可以获取到项目工程的绝对路径

'''
# print(__file__) #获取当前文件的路径
# print(os.path.dirname(__file__))#上一层目录的文件路径
#工程路径
project_path = os.path.dirname(os.path.dirname(__file__))
# print(project_path)

#配置路径
config_path = os.path.join(project_path,'configs')
# print(config_path)

#测试数据文件路径
testData_path = os.path.join(project_path,'data')
print(testData_path)

#测试报告路径
report_path = os.path.join(project_path,r'outFiles\report')
# print(testData_path)

#测试报告路径
log_path = os.path.join(project_path,'outFiles\log')
# print(testData_path)


