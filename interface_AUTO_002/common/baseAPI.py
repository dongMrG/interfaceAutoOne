# -*- coding: utf-8 -*-
# @Time : 2022-03-31 10:13
# @Author : DXS
# @Email : 756444819@qq.com
# @File : baseAPI.py
import requests
import inspect
from utils.handle_yaml import get_yaml_data
from configs.config import HOST
from utils.handle_excelV2 import get_excel_data
class BaseAPI:

    def __init__(self):
        self.data = get_yaml_data('../configs/apiConfig.yml')[self.__class__.__name__]#根据类名去获取yaml文件内对应的数据
        # print(self.data)
    def requests_send(self,data):#发送请求
        data_test = self.data[inspect.stack()[1][3]]#根据对应的方法名，提取对应的数据
        # print(data_test['method'])
        reqs = requests.request(
            method=data_test['method'],
            url=f"{HOST}{data_test['path']}",
            data=data
        )
        return reqs.json()

