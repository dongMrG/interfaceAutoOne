# -*- coding: utf-8 -*-
# @Time : 2022-03-28 10:48
# @Author : DXS
# @Email : 756444819@qq.com
# @File : tokenyanzheng.py
import requests
from demoOne.config.HOST import WMHOST,TESTDATA,PL
import hashlib
from demoOne.data.handle import md5_pwd
'''
接口自动化列出商铺列表
'''


def login(indata):
    url = f'{WMHOST}/account/sLogin'
    indata['password'] = md5_pwd(indata['password'])
    indata = TESTDATA
    res = requests.post(url, data=indata)
    token = res.json()["data"]["token"] #提取token
    # print('token为：',token)
    return token

#列出商铺
def list_less(data,indata):
    url = f'{WMHOST}/shopping/myShop'
    intoken = {
        "Authorization" : indata #传入登录的token值
    }
    palyload = data
    req = requests.get(url,params=palyload,headers=intoken)
    req.encoding = 'utf-8'#设置响应数据编码
    print(req.text)
    return req.json()

if __name__ == '__main__':

    list_less(PL,login(TESTDATA))