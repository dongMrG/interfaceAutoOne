# -*- coding: utf-8 -*-
# @Time : 2022-03-31 10:13
# @Author : DXS
# @Email : 756444819@qq.com
# @File : baseAPI.py
import requests
import inspect
from utils.handle_yaml import get_yaml_data
from configs.config import HOST
from utils.handle_path import api_path
import os
class BaseAPI:

    def __init__(self,token=None):
        if token:#需要token的业务
            self.header = {'Authorization':token}
        else:#登录业务
            self.header = None
        #获取对应模块的接口信息
        self.data = get_yaml_data(os.path.join(api_path,'apiConfig.yml')
                                  )[self.__class__.__name__]#根据类名去获取yaml文件内对应的数据
    # 发送请求
    def requests_send(self,data=None,params=None,id='',files=None):
        try:
            data_test = self.data[inspect.stack()[1][3]]#根据对应的方法名，提取对应的数据
            reqs = requests.request(
                    method=data_test['method'],
                    url=f"{HOST}{data_test['path']}{id}",
                    data=data,
                    params=params,
                    headers=self.header,
                    files=files
                )
            return reqs.json()
        except:
            pass
    #---------------------接口增删改查-------------------------
    #查询数据接口
    def query(self,data):
        return self.requests_send(params=data)
    #增加数据接口
    def add(self,data):
        return self.requests_send(data=data)

    # 更新数据接口
    def update(self,data):
        return self.requests_send(data=data)
    # 删除数据接口
    def delete(self,id):
        return self.requests_send(params=id)

    #--------------------文件上传---------------------
    '''
    文件上传格式： 文件路径、文件名、文件类型
    路径： 
    {'file':(文件名，文件对象本身，文件类型)}----转化
    {'file'：('123.png',open('xx/123.png','rb'),'png')}
    '''
    def file_upload(self,file_path:str):
        #1- 获取文件名
        file_name = file_path.split('/')[-1]
        #2- 文件类型
        file_type = file_path.split('.')[-1]
        file = {'file':(file_name,open(file_path,'rb'),file_type)}
        #3- 发送请求
        return self.requests_send(files=file)