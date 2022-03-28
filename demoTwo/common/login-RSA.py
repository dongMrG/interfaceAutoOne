# -*- coding: utf-8 -*-
# @Time : 2022-03-29 11:20
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login-RSA.py
import requests
from demoTwo.common.handle_data import md5_data,RSAenderypt

HOST = 'http://121.41.14.39:8082'
def login(data):
    url = f'{HOST}/account/loginRsa'
    #MD5加密
    pwd_md5_text = md5_data(data['password'])
    #rsa加密
    rsa = RSAenderypt()
    pwd_rsa_text = rsa.encrypt(pwd_md5_text)
    #更新到data
    data['password'] = pwd_rsa_text
    #增加sign签名
    data.update({'sign':md5_data(data['username']+pwd_rsa_text)})
    print(data)
    res = requests.post(url,data=data)
    print(res.text)

if __name__ == '__main__':
    test_data = {
            'username': 'zo0606',
            'password': '83808'
    }
    login(test_data)
