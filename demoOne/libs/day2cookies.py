# -*- coding: utf-8 -*-
# @Time : 2022-03-28 8:57
# @Author : DXS
# @Email : 756444819@qq.com
# @File : day2cookies.py

'''
cookies验证登录教管系统

data,json   一般用于POST请求
params,files    一般用于get请求，files在文件上传接口中使用

'''

import requests
import hashlib
from demoOne.config.HOST import JGHOST,KC
from demoOne.data import handle


def login(data):
    url = f'{JGHOST}/api/mgr/loginReq'
    palyload = data
    res =requests.post(url,data=palyload)
    return res.cookies

#MD5加密登录
class List_less:

    def __init__(self,payload):
        self.payloads = payload
    #列出课程
    def list_less(self,data):
        url = f'{JGHOST}/api/mgr/sq_mgr/'
        palyload = data
        req = requests.get(url, params=palyload, cookies=self.payloads)
        req.encoding = 'utf-8'  # 设置响应数据编码
        print(req.json())
        return req.json()
if __name__ == '__main__':
    '''登录'''
    # cookie = login(TESTDATA)
    cookies = login({'username':'auto','password':'sdfsdfsdf'})
    #列出课程
    List_less(cookies).list_less(KC)
