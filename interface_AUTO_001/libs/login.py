# -*- coding: utf-8 -*-
# @Time : 2022-03-30 10:12
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login.py

from interface_AUTO_001.common.baseAPI import BsaeAPI
from interface_AUTO_001.configs.config import TESTDATA
from interface_AUTO_001.utils.handle_data1 import md5_test

class Login(BsaeAPI):
    def login(self,inData,getToken=False):
        indata = md5_test(inData['password'])#加密
        inData['password'] = indata #将加密的数据传入inData中
        resp = self.request_send(data=inData)#发送请求
        resData = resp.json()['data']['token']
        if getToken == True:
            return resData
        else:
            return resp

if __name__ == '__main__':
    print(Login().login(TESTDATA,True))
