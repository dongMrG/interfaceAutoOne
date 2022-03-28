# -*- coding: utf-8 -*-
# @Time : 2022-03-29 14:30
# @Author : DXS
# @Email : 756444819@qq.com
# @File : baseAPI.py

#基类封装,这个基类后续可能因为业务模块的增加可以维护
'''
基类封装思路：
    1- 为所有的业务模块提供基本的接口操作：增删改查 + 发送
    2- 日志 截图都可以在基类里封装
    3- 断言方法
接口风格：
    1- 常规风格：
        1、一个模块增删改查的四个接口的路径的不一样--自动性比较强
        2、请求和响应数据类型不定
    2-restful风格
        1、一个模块，增删改查的四个接口的路径一样的
        2、请求和响应数据类型一样的--json格式
一个项目的版本定下来之后：
    例如一个接口有10个用例：
        1- 变的是： 接口的描述、接口的用例请求参数、预期的响应
        2- 不变的是：url 请求方法 （参数化）
'''
from demoTwo.utils.handle_yml import get_yaml_data
import requests
import inspect
from demoTwo.config.config import HOST
class BsaeAPI:
    # 1- 发送的公共方法
    #简单的
    def __init__(self):
        print('当前类的类名是',self.__class__.__name__)
        self.data = get_yaml_data('../config/apiConfig.yml')[self.__class__.__name__]

    def request_send(self,data):
        '''
        inspect：
            1、可以获取类或函数的参数的信息
            2、获取当前函数的函数名
            3、获取调用函数的函数名
        '''
        methodName = inspect.stack()[1][3]#固定写法，谁调用了我，就打印他的函数名
        path,method = self.data[methodName].values()#登录模块所有的数据--需要剥离对应某一个接口的数据对应的值 values()
        resp = requests.request(method=method,url=f'{HOST}{path}',data=data)
        print(methodName,'-----',self.data[methodName])
        # print(reqs.json())
        return resp
