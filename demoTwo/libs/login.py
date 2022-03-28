# -*- coding: utf-8 -*-
# @Time : 2022-03-30 10:12
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login.py

from demoTwo.common.baseAPI import BsaeAPI
from demoTwo.config.config import TESTDATA
from demoTwo.utils.handle_data1 import md5_test

class Login(BsaeAPI):
    def login(self,inData):
        indata = md5_test(inData['password'])#加密
        inData['password'] = indata #将加密的数据传入inData中
        resp = self.request_send(data=inData)#发送请求
        resData = resp.json()['data']['token']
        print('token: ',resData)
        print(resp.text)

if __name__ == '__main__':
    print(Login().login(TESTDATA))
