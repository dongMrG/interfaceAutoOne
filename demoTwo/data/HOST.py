# -*- coding: utf-8 -*-
# @Time : 2022-03-28 10:53
# @Author : DXS
# @Email : 756444819@qq.com
# @File : HOST.py

WMHOST = 'http://121.41.14.39:8082'
JGHOST = 'http://175.24.199.78:8086'
RSAHOST = 'http://121.41.14.39:8082/account/loginRsa'
#登录
TESTDATA = {
    'username': 'zo0606',
    'password': '83808'
}
#列出商铺
PL = {
    "page": '1',
    "limit": '3'
}
#列出课程
KC = {
    "action":"list_course",
    "pagenum":1,
    "pagesize":20
}