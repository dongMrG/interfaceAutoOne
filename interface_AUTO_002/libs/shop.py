# -*- coding: utf-8 -*-
# @Time : 2022-03-30 10:17
# @Author : DXS
# @Email : 756444819@qq.com
# @File : shop.py
#定义店铺类
from common.baseAPI import BaseAPI
from libs.login import Login
from pprint import pprint
class Shop(BaseAPI):
    #重写
    '''
    1- 当修改店铺时，店铺id需要动态获取，可重写父类方法
    2- 需要动态获取图片信息
    '''
    def update(self,data,shop_id,image_info):
        if data['id'] == 'id':#如果正向用例需要动态获取id
            data['id'] = shop_id#更新id
        #更新图片信息
        data['image_path'] = ''
        data['image'] = f'/file/getImgStream?fileName={image_info}'
        #调用父类的update发送
        return super(Shop, self).update(data)  #super固定写法

if __name__ == '__main__':
    #登录
    TESTDATA ={"username":"zo0606","password":"83808"}
    token = Login().login(TESTDATA,getToken=True)
    #创建店铺实例
    shop = Shop(token)
    #列出店铺
    test_data = {'page':1,'limit':20}
    res = Shop(token).query(test_data)
    pprint(res)
    #获取店铺id
    shop_id = res['data']['records'][0]['id']
    print('店铺id----->',shop_id)
    #文件上传接口
    image_info = shop.file_upload('../data/y001.png')

    print(image_info)
    image_infos = image_info['data']['realFileName']
    #店铺更新
    update_data = {
            "name": "星巴克新建店",
            "address": "上海市静安区秣陵路303号",
            "id": "id",
            "Phone": "13176876632",
            "rating": "5.0",
            "recent_order_num":110,
            "category": "快餐便当/简餐",
            "description": "满30减5，满60减8",
            "image_path": "b8be9abc-a85f-4b5b-ab13-52f48538f96c.png",
            "image": "http://121.41.14.39:8082/file/getImgStream?fileName=b8be9abc-a85f-4b5b-ab13-52f48538f96c.png"
    }
    shop.update(update_data,shop_id,image_infos)