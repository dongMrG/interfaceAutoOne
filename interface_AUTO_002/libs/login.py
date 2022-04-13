# -*- coding: utf-8 -*-
# @Time : 2022-03-30 10:12
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login.py

from common.baseAPI import BaseAPI
from utils.handle_data1 import md5_test_data
from utils.handle_excelV3 import get_excel_data
import json
class Login(BaseAPI):

    def login(self,inData):#,getToken=False
        inData['password'] = md5_test_data(inData['password'])#加密,将加密的数据传入inData中
        print(type(inData))
        reqs = self.requests_send(inData)#发送请求
        # if getToken:
        #     return reqs['data']['token']
        # else:
        return reqs

if __name__ == '__main__':
    TESTDATA ={
        "username":"zo0606",
        "password":"83808"
    }
    print(Login().login(TESTDATA))
