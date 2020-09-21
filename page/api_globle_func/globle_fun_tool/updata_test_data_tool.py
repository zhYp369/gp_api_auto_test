#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: edit_test_data_tool
@time: 2020/9/18 14:35
@desc: 
"""
import os

from page.api_globle_func.globle_fun_tool.updata_dependent_tool import get_updata_dependent
from util.GlobeTestDataFunction.dataFunction import getfunc_value
from util.zhengzebiaodashi.getdata_fromzhengze import get_data_func_list


def updata_func_data(req_data):
    """
    将请求报文里的数据进行进行更新（将自定义数据方法替换为对应的数据），并返回
    """
    # 获取请求数据包含的方法，返回list
    req_data_func_list = get_data_func_list(req_data)

    # 根据方法列表，返回方法和方法对应的值
    req_data_FuncAndValue_dict = {}
    for i in range(len(req_data_func_list)):
        req_data_FuncAndValue_dict[req_data_func_list[i]] = getfunc_value(req_data_func_list[i])

    # 将请求数据的方法换成对应的值
    for k, v in req_data_FuncAndValue_dict.items():
        req_data = str(req_data).replace(k, v)
    return req_data





def updata_dependent(casedata, projectN, gcN):
    casedata = get_updata_dependent(casedata, projectN, gcN)
    return casedata









