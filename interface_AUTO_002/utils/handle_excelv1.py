# -*- coding: utf-8 -*-
# @Time : 2022-03-31 15:02
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_excelv1.py
'''
需求点：
返回
    - 请求体数据
    - 预期响应数据
'''
import re
import xlrd
def get_excel_data(file_path,sheet_name):
    '''
    :param file_path: 路径
    :param sheet_name: 表名
    :return: [(),()]
    '''
    #1、 打开文件
        # formatting_info=True保持excel原样式
    try:
        work_book = xlrd.open_workbook(file_path,formatting_info=True)
        #2、 指定对应表
        work_sheet = work_book.sheet_by_name(sheet_name)
        # print(work_book.sheet_names())#查看所有的表名
        # print(work_sheet.row_values(0))#查看表内的第一行数据

        #获取指定数据
        row_idx = 0
        data_list = []

        sum = {}
        for one in work_sheet.col_values(1):
            req_body = dict(work_sheet.cell(row_idx,9).value) #cell(行编号，列编号)
            req_data = work_sheet.cell(row_idx,11).value #cell(行编号，列编号)
            data_list.append(req_body)
            row_idx += 1
        return data_list

    except IndexError:
        print('这里有一个空行')
#将提取出来的参数，转换为字符串
def handle_list():
    re_list = []
    dict1 = {}
    listf = get_excel_data('../data/Delivery_System_V1.5.xls','登录模块')
    print(type(listf))
    for i in listf:
        dict1 = dict(zip(i))
        if i == '请求参数':
            continue
        elif i == None:
            continue
        else:
            re_list.append(i)
    da = 0
    for one in re_list:
        json = str(one)
        print(json)
    return re_list
#将转换为字符串的列表数据分离出来
def login_data():
    print(handle_list()[0])

if __name__ == '__main__':
    # login_data()
    handle_list()


