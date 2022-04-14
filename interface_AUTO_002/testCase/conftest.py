# -*- coding: utf-8 -*-
# @Time : 2022-04-14 14:51
# @Author : DXS
# @Email : 756444819@qq.com
# @File : conftest.py

#----验证功能----
import pytest
from configs.config import USERDATA
from libs.login import Login
from libs.shop import Shop
'''
scope='session'   整个自动化运行只做一次
    1- 环境检测（运行环境、项目环境）
    2- 登录
scope='function'  没一个函数或方法都会调用
scope='class'     每一个类调用一次，一个类中可以有多个方法
'''
@pytest.fixture(scope='function',autouse=True)
def start_running():
    print('----开始自动化测试运行----')


#--------------1、登陆操作--------------
@pytest.fixture(scope='session')
def login_init():
    print('------1、开始执行登录操作------')
    token = Login().login(USERDATA,getToken=True)
    #不推荐使用return,推荐使用yield之后的代码还可以运行
    yield token
    print('------登录完成了------')

#--------------2、店铺初始化操作--------------
#有返回值 fixture使用：如果一个fixtrue函数需要使用另一个fixtrue返回值，直接使用他的函数名
#没有返回值： @pytest.mark.userfixtures('函数名')
@pytest.fixture(scope='session')
def shop_init(login_init):
    print('------2、创建店铺实例操作------')
    shop_object = Shop(login_init)
    yield shop_object