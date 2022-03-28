# -*- coding: utf-8 -*-
# @Time : 2022-03-31 15:52
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_excelV2.py

'''
            handle_excelV2
需求点：
返回
    - 请求体数据
    - 预期响应数据
'''

import xlrd
def get_excel_data(file_path, sheet_name,case_name,*args):
    '''
    :param file_path: 路径
    :param sheet_name: 表名
    :return: [(),()]
    '''
    res_list = [] #存放结果
    #1、 打开文件
        # formatting_info=True保持excel原样式
    work_book = xlrd.open_workbook(file_path,formatting_info=True)
    #2、 指定对应表
    work_sheet = work_book.sheet_by_name(sheet_name)

    #3、 根据列名，转换为下标来获取指定数据
    #args == ['标题','请求参数','响应预期结果']
    col_index = []
    #列名是第0列数据
    for col_name in args:
        col_index.append(work_sheet.row_values(0).index(col_name))
    print('需要获取的列名---',col_index)

    row_idx = 0
    for one in work_sheet.col_values(0):
        if case_name in one:
            # req_body = work_sheet.cell(row_idx,col_index[1]).value #cell(行编号，列编号)
            # req_data = work_sheet.cell(row_idx,col_index[2]).value #cell(行编号，列编号)
            col_datas = []
            for num in col_index: #[4,9,11]
                tmp = work_sheet.cell(row_idx,num).value
                col_datas.append(tmp)
            res_list.append(col_datas)
        row_idx += 1
    return res_list

if __name__ == '__main__':
    res = get_excel_data('../data/Delivery_System_V1.5.xls','登录模块','Login',*['请求参数'])
    print(res)