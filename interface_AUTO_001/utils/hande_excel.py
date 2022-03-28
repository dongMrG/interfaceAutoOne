# -*- coding: utf-8 -*-
# @Time : 2022-03-30 16:31
# @Author : DXS
# @Email : 756444819@qq.com
# @File : hande_excel.py
'''
-----------------版本V1.0-----------------
需求：有可能客户或者上下游同事，描述不是很专业

分析需求：
     1- 获取自动化测试用例 excel里面的对应的数据----大功能
        2- 获取具体哪些数据
            1- 用例编号
            2- 用例标题
            3- 请求body
            4- 预期相应结果
        3- 需要返回什么类型
            1- 客户需要吧读取的数据给test_login()   使用的是pytest 数据驱动的方法
解决方案：
    1- 操作excel库是什么
        1- xlrd xlwt 操作xx.xls
            xlrd 读操作
            xlwt 写操作--新建一个文件
            xlutils 写操作--在已有的excel文件里修改（写）
        2- openpyxl
        3- panda

测试反馈：
版本迭代建议：

'''
import xlrd
from interface_AUTO_001.utils.hand_path import testData_path
import os
def get_excel_data(excelDir,sheetName) -> list:
    #1-打开一个文件
        #formatting_info=True 保持原样式，规范，一般都要加
    workBook = xlrd.open_workbook(excelDir,formatting_info=True)#excel文件
    #2- 获取对应的子表
    sheets = workBook.sheet_names()
    print(sheets)

if __name__ == '__main__':
    fileDir = os.path.join(testData_path,'')
    get_excel_data()