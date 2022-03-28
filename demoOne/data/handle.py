# -*- coding: utf-8 -*-
# @Time : 2022-03-28 16:53
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle.py

import hashlib

#md5加密
def md5_pwd(pwd:str,salt=''):
    '''
    :param pwd: 加密的字符串
    :param salt: 盐值
    :return: 返回加密后的结果
    '''
    #创建md5实例
    h1 = hashlib.md5()
    #调用md5函数
    h1.update(f'{pwd}{salt}'.encode('utf-8'))
    return h1.hexdigest()