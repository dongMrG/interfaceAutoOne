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


