# -*- coding: utf-8 -*-
# @Time : 2022-03-29 14:56
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_data1.py

'''
RSA加密代码创建

'''
#MD5加密
import hashlib
def md5_test(pwd:str,salt=''):
    '''
    :param pwd: 需要加密的字符串
    :param salt: 盐值
    :return:
    '''
    h1 = hashlib.md5() #实例化MD5加密方法
    h1.update(f'{pwd}{salt}'.encode('utf-8'))
    return h1.hexdigest()

#RSA加密
from Crypto.PublicKey import RSA
from Crypto.Cipher import PKCS1_v1_5 as PKCS_rsa
import base64
class RSAencrpyt:
    '''
    提取到公钥，存放在一个.pem文件中
            username  账号
            password: RSA加密的结果
                1- xintian通过md5加密成密文--a
                2- 使用RSA的公钥加密(a)
            sign 签名
                md5(username+password密文)
    '''
    #初始化
    def __init__(self,file_path='./'):
        self.file_path = file_path
    #RSA加密
    def rsa_encrpyt(self,crpyt_data):
        #获取公钥
        with open(self.file_path+'public.pem') as fo:
            key = fo.read()#返回公钥的值
            import_key = RSA.importKey(key)#将字符串转换为公钥
            rsa_cipher = PKCS_rsa.new(import_key) #生成对象
            #RSA加密公钥
            rsa_test = base64.b64encode(rsa_cipher.encrypt(bytes(crpyt_data.encode('utf-8'))))
            '''
              bytes(crypt_data.encode('utf-8')) :加密数据转换为字节格式
              cipher.encrypt : 加密函数进行加密   加密对象.加密方法
              base64.b64encode : base64进行编码
            '''
            # print(rsa_test)
            return rsa_test.decode('utf-8')#对rsa加密的字符串进行解码处理

if __name__ == '__main__':
    RSAencrpyt().rsa_encrpyt('123132')