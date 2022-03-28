# -*- coding: utf-8 -*-
# @Time : 2022-03-30 16:15
# @Author : DXS
# @Email : 756444819@qq.com
# @File : test_login.py
import pytest
'''
用例文件执行条件：
    1- 改业务层代码封装
    2- 需要自动化测试用例---数据驱动---使用指定文件类型做
        功能用例：
            1- excel
            2- word
            3- xmind
            4- yaml
            5- 数据库
        自动化用例选型：靠代码或者工具
            1- excel
            2- yaml
    
'''
from interface_AUTO_001.libs.login import Login
class TestLogin:
    def test_login(self):
        pass