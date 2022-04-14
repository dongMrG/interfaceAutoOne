# -*- coding: utf-8 -*-
# @Time : 2022-04-13 15:13
# @Author : DXS
# @Email : 756444819@qq.com
# @File : food.py
from common.baseAPI import BaseAPI
from libs.login import Login
class Food(BaseAPI):
    pass

if __name__ == '__main__':
    #登录
    TESTDATA ={"username":"zo0606","password":"83808"}
    token = Login().login(TESTDATA,getToken=True)
    #列出食品
    # res = Food(token).requests_send(id=5624763)
    res = Food(token).query(10866)
    print(res)