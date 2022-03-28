# -*- coding: utf-8 -*-
# @Time : 2022-03-29 14:56
# @Author : DXS
# @Email : 756444819@qq.com
# @File : login1_RSA.py

'''

'''
HOST = 'http://121.41.14.39:8082'
import requests
from demoTwo.testBase.handle_data1 import md5_test,RSAencrpyt
'''
参数：
username  账号
password: RSA加密的结果
    1- xintian通过md5加密成密文--a
    2- 使用RSA的公钥加密(a)
sign 签名 
    md5(username+password密文)
'''
def login(data): #登录
    url = f'{HOST}/account/loginRsa'
    #1、通过md5加密密码
    pwd_md5_test = md5_test(data['password'])
    #2、使用RSA加密公钥
    rsa = RSAencrpyt()#实例化
    pwd_rsa_test = rsa.rsa_encrpyt(pwd_md5_test)
    #将rsa加密后的密码更新值data中
    data['password'] = pwd_rsa_test
    #增加签名
    data.update({'sign':md5_test(data['username']+pwd_rsa_test)})

    reqs = requests.post(url,data=data)
    print(reqs.text)

if __name__ == '__main__':

    data_test = {
            'username': 'zo0606',
            'password': '83808'
    }
    login(data_test)