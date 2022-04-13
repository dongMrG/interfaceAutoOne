# -*- coding: utf-8 -*-
# @Time : 2022-04-12 13:53
# @Author : DXS
# @Email : 756444819@qq.com
# @File : test_login.py
import pytest
from libs.login import Login
from utils.handle_excelV3 import get_excel_data
# 1 登录类
class TestLogin:
    #2 登录方法
    @pytest.mark.parametrize('inBody,expData',get_excel_data('登录模块','Login'))
    def test_login(self,inBody,expData):
        #3 调用登录接口
        print(inBody['password'])
        res = Login().login('inBody')
        print(res)
        #4 断言结果是否符合预期
        assert res['msg'] == expData['msg']

if __name__ == '__main__':

    pytest.main([__file__,'-s'])