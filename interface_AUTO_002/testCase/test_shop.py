# -*- coding: utf-8 -*-
# @Time : 2022-04-14 11:17
# @Author : DXS
# @Email : 756444819@qq.com
# @File : test_shop.py
import allure
import pytest
import os
from libs.login import Login
from libs.shop import Shop
from testCase.conftest import shop_init
from utils.handle_path import report_path
from utils.handle_excelV3 import get_excel_data
# 店铺模块，接口自动化测试测试类
'''
店铺的模块测试：初始化操作（前置条件）
    1- 首先完成有效的登录操作---拿到token
    2- 完成店铺实例的创建
    
fixtrue环境初始化与数据清除 
    新建conftest文件----固定写法
'''

@allure.epic('外卖系统')
@allure.feature('店铺模块')
class TestShop():

    @allure.story('列出商铺')
    @pytest.mark.parametrize('title,inBody,expData',get_excel_data('我的商铺','listshopping'))
    @allure.title('{title}')#用例标题
    def test_shop_query(self,shop_init,title,inBody,expData):#列出商铺
        #查询
        shop = shop_init.query(inBody)
        assert shop['code'] == expData['code']

    # 方案1   店铺编辑接口
    # @allure.story('更新店铺')
    # @pytest.mark.parametrize('title,update_inBody,update_expData',get_excel_data('我的商铺','updateshopping'))
    # @allure.title('{title}')
    # def test_shop_update(self,shop_init,title,update_inBody,update_expData):
    #     with allure.step('1、用户登录'):
    #         shop_object = shop_init
    #     with allure.step('2、选中编码店铺'):
    #         shop_id = shop_init.query({'page':1,'limit':20})['data']['records'][0]['id']
    #     with allure.step('3、替换店铺图片'):
    #         image_info = shop_init.file_upload('../data/y001.png')['data']['realFileName']
    #     with allure.step('4、提交店铺信息'):
    #         res = shop_init.update(update_inBody,update_expData,image_info)
    #     with allure.step('5、判断是否操作成功'):
    #         assert res['code'] == update_expData['code']

    # 方案2  fixture
    @allure.story('更新店铺')
    @pytest.mark.parametrize('title,update_inBody,update_expData',get_excel_data('我的商铺','updateshopping'))
    @allure.title('{title}')
    def test_shop_update(self,shop_update_init,title,update_inBody,update_expData):
        with allure.step('1、提交店铺信息'):
            res = shop_update_init['shop_object'].update(update_inBody,
                                                         shop_update_init['shop_id'],
                                                         shop_update_init['image_info'])
        with allure.step('2、判断是否操作成功'):
            assert res['code'] == update_expData['code']


if __name__ == '__main__':

    pytest.main([__file__,'-s','--alluredir',report_path,'--clean-alluredir'])
    os.system(f'allure serve {report_path}')