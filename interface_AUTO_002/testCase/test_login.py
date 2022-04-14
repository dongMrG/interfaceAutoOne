# -*- coding: utf-8 -*-
# @Time : 2022-04-12 13:53
# @Author : DXS
# @Email : 756444819@qq.com
# @File : test_login.py
import pytest
from libs.login import Login
from utils.handle_excelV3 import get_excel_data
from utils.handle_path import report_path
import allure
import os
@allure.epic('外卖系统') #项目级别
@allure.feature('登录模块')#业务级别
# 1 登录类
class TestLogin:
    #2 登录方法
    @allure.story('登录接口')#接口级别

    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('登录模块','Login'))
    @allure.title('{title}') #用例标题
    def test_login(self,title,inBody,expData):
        #3 调用登录接口
        #这里碰到的错误：    login后面传入的参数，带了单引号，导致传入的值为字符串，不是inBody参数
        res = Login().login(inBody)
        #4 断言结果是否符合预期
        assert res['msg'] == expData['msg']

if __name__ == '__main__':

    '''
    - allure 跨平台性
    - 运行原理：
        1- 报告需要数据源  pytest执行后生成的json文件
        2- 使用allure serve 运行这些json文件
    '''
    pytest.main([__file__,'-s','--alluredir',report_path,'--clean-alluredir'])

    #,'--clean-alluredir']  '--alluredir‘后面接json文件存放的目录
    # os.system(f'allure serve {report_path}')