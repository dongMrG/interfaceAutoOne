# -*- coding: utf-8 -*-
# @Time : 2022-03-31 16:38
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login_pltest.py

from common.baseAPI import BaseAPI

from utils.handle_data1 import md5_test_data
from utils.handle_excelv1 import get_excel_data
class Login(BaseAPI):

    def login(self,inData):
        num = 0
        for i in inData:
            i = inData[num]
            i['password'] = md5_test(self.data['password'])#加密,将加密的数据传入inData中
            reqs = self.requests_send(inData)#发送请求
            num += 1
            return reqs


if __name__ == '__main__':
    res = Login().login(handle_list())
    print(res)