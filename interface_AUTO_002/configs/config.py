# -*- coding: utf-8 -*-
# @Time : 2022-03-30 14:10
# @Author : DXS
# @Email : 756444819@qq.com
# @File : config.py
import json

from interface_AUTO_002.utils.handle_excelV2 import get_excel_data
HOST = 'http://121.41.14.39:8082'

TESTDATA = json.loads(get_excel_data('../data/Delivery_System_V1.5.xls','登录模块','Login',*['请求参数']))
d = {}
num = 0
for i in TESTDATA:
    d[f'userdata{num}'] = i
    num += 1
print(d)
print(TESTDATA)
