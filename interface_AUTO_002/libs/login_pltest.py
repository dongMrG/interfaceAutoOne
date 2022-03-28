# -*- coding: utf-8 -*-
# @Time : 2022-03-31 16:38
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login_pltest.py

from interface_AUTO_002.common.baseAPI import BaseAPI
from interface_AUTO_002.configs.config import TESTDATA
from interface_AUTO_002.utils.handle_data1 import md5_test
from interface_AUTO_002.utils.handle_excelv1 import get_excel_data,handle_list
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