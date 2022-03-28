# -*- coding: utf-8 -*-
# @Time : 2022-03-29 9:48
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_data.py

import hashlib
from Crypto.PublicKey import RSA
from Crypto.Cipher import  PKCS1_v1_5 as PKC_cipher
import base64
#md5加密
def md5_data(pwd:str,salt=''):

    h1 = hashlib.md5()
    pwd = pwd+salt#拼接盐值
    h1.update(pwd.encode('utf-8'))
    # h1.update(f'{pwd}{salt}'.encode('utf-8'))
    # print(h1.hexdigest())
    return h1.hexdigest() #加密后的结果 16进制

'''
外卖项目--RSA加密接口
        url = 'http://121.41.14.39:8082/account/loginRsa'
        参数：
            username  账号
            password: RSA加密的结果
                1- xintian通过md5加密成密文--a
                2- 使用RSA的公钥加密(a)
            sign 签名 
                md5(username+password密文)
        加密流程：
            1-首先需要一个公钥,
'''
#RSA加密
class RSAenderypt:
    def __init__(self,file_path='./'):
        self.file_path = file_path
    #创建密钥对
    #加密操作
    def encrypt(self,crypt_data):
        #打开读取公钥
        with open(self.file_path+'public.pem') as fo:
            key = fo.read() #读取字符串类型的内容
            print(key)
            public_key = RSA.importKey(key) #将读取的字符串转换为公钥
            cipher = PKC_cipher.new(public_key) #生成对象
            rsa_text = base64.b64encode(cipher.encrypt(bytes(crypt_data.encode('utf-8'))))#固定写法
            '''
            bytes(crypt_data.encode('utf-8')) :加密数据转换为字节格式
            cipher.encrypt : 加密函数进行加密   加密对象.加密方法
            base64.b64encode : base64进行编码
            '''
            #解码
            return rsa_text.decode('utf-8')


# if __name__ == '__main__':
#     res = md5_data('DXS')
#     RSAenderypt('./public.pem').encrypt()
