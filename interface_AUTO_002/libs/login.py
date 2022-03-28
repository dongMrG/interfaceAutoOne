# -*- coding: utf-8 -*-
# @Time : 2022-03-30 10:12
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login.py

from interface_AUTO_002.common.baseAPI import BaseAPI
from interface_AUTO_002.configs.config import TESTDATA
from interface_AUTO_002.utils.handle_data1 import md5_test

class Login(BaseAPI):
    def login(self,inData,getToken=False):
        inData['password'] = md5_test(inData['password'])#加密,将加密的数据传入inData中
        reqs = self.requests_send(inData)#发送请求
        # resData = reqs.json()['data']['token']
        # if getToken == True:
        #     return resData
        # else:
        #     return reqs

if __name__ == '__main__':
    print(Login().login(TESTDATA,True))
