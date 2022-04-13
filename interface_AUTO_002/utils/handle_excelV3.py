# -*- coding: utf-8 -*-
# @Time : 2022-04-12 14:19
# @Author : DXS
# @Email : 756444819@qq.com
# @File : handle_excelV3.py
import xlrd
import os
from utils.handle_yaml import get_yaml_data
from utils.handle_path import config_path,data_path

def get_excel_data( sheet_name, case_name, run_case=['all']):
    '''
    :param file_path: 文件路径
    :param sheet_name: 表名
    :param case_name: 用例名
    :param args: 列名
    :param run_case: 用例编号
    :return:
    '''
    config_data = get_yaml_data(os.path.join(config_path,'excelConfig.yml'))
    file_path = os.path.join(data_path,config_data['file_name'])
    args = config_data['col_name']
    res_list = []  # 存放结果
    # 1、 打开文件
    # formatting_info=True保持excel原样式
    work_book = xlrd.open_workbook(file_path, formatting_info=True)
    # 2、 指定对应表
    work_sheet = work_book.sheet_by_name(sheet_name)

    # 3、 根据列名，转换为下标来获取指定数据
    col_indexs = []
    # 列名是第0列数据
    for col_name in args:
        col_indexs.append(work_sheet.row_values(0).index(col_name))
    print('需要获取的列名---', col_indexs)

    # --------------------用例筛选---------------------
    # ['all','003','005-007','009']
    run_case_data = []
    if 'all' in run_case:  # 所有的用例全部运行
        run_case_data = work_sheet.col_values(0)
    else:  # 不是全部运行 ['003','005-007','009']
        for one in run_case:
            if '-' in one:  # 连续的用例
                start,end = one.split('-')  # 获取对应的数值
                for num in range(int(start), int(end) + 1):
                    run_case_data.append(case_name + f'{num:0>3}')
            else:  # 不连续的用例
                run_case_data.append(case_name + f'{one:0>3}')
    print('运行的用例是', run_case_data)
    # -----------------------------------------------
    # 获取指定数据
    row_idx = 0
    for one in work_sheet.col_values(0):
        if case_name in one and one in run_case_data:
            # req_body = work_sheet.cell(row_idx,col_index[1]).value #cell(行编号，列编号)
            # req_data = work_sheet.cell(row_idx,col_index[2]).value #cell(行编号，列编号)
            col_datas = []#每一行所获取的列数据
            for num in col_indexs:  # [4,9,11] 遍历需要获取的列
                tmp = is_josn(work_sheet.cell(row_idx, num).value)#cell(行编号，列编号)
                # tmp = work_sheet.cell(row_idx, num).value#cell(行编号，列编号)
                print(type(tmp))
                col_datas.append(tmp)
            res_list.append(tuple(col_datas))
            # res_list.append(col_datas)
        row_idx += 1
    return res_list

#根据需求写函数
import json
def is_josn(inStr):#  返回值 ： 是  ,不是
    try:
        return json.loads(inStr)#没有报错---可以转化为字典 --就json格式
    except:
        return inStr#返回需要判断的字符串--不是json字符串

if __name__ == '__main__':
    res = get_excel_data( '登录模块', 'Login',run_case=['001','003-005'])
    print(res)
    for i in res:
        print(i)
