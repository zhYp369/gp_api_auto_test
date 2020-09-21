#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: edit_test_data
@time: 2020/9/18 14:27
@desc: 
"""
from page.api_globle_func.globle_fun_tool.get_req_data_tool import *
from page.api_globle_func.globle_fun_tool.updata_test_data_tool import updata_func_data, updata_dependent
from page.api_globle_func.globle_fun_tool.updata_dependent_tool import save_dependent_data
from page.api_globle_func.globle_fun_tool.output_tool import get_output_list


def get_req_data(testdata):
    case_data = {}
    case_data["case_id"] = get_case_id(testdata)
    case_data["test_discribe"] = get_test_discribe(testdata)
    case_data["api_id"] = get_api_id(testdata)
    case_data["url"] = get_url(testdata)
    case_data["method"] = get_method(testdata)
    case_data["header"] = get_header(testdata)
    case_data["globaldata"] = get_global_data(testdata)
    case_data["urldata"] = get_yw_params(testdata)
    case_data["bodydata"] = get_yw_data(testdata)
    case_data["cookie"] = get_cookie(testdata)
    case_data["tonken"] = get_tonken(testdata)
    case_data["expected"] = get_expected(testdata)
    case_data["d_case_id"] = get_d_case_id(testdata)
    case_data["dependent_field"] = get_d_field_filename(testdata)
    case_data["is_bei_dp"] = get_is_bei_dp(testdata)
    case_data["output"] = get_output(testdata)
    case_data["gc_globle_data"] = testdata.get("gc_globle_data")
    case_data["api_config"] = testdata.get("api_config")
    case_data["case_data"] = testdata.get("case_data")
    case_data["testdatafile"] = testdata.get("testdatafile")
    return case_data


def updata_req_data(casedata, projectN, gcN):
    # 更新fun_data
    if casedata["globaldata"]:
        casedata["globaldata"] = updata_func_data(casedata["globaldata"])
    if casedata["urldata"]:
        casedata["urldata"] = updata_func_data(casedata["urldata"])
    if casedata["bodydata"]:
        casedata["bodydata"] = updata_func_data(casedata["bodydata"])
    dp_case_id = casedata.get("case_data").get("dp_case_id")
    if dp_case_id:
        casedata = updata_dependent(casedata, projectN, gcN)
    return casedata


def save_dependent(case_data, response_text, projectN, gcN):
    """
    获取被依赖的数据，并保存到文件中，供依赖用例使用
    :param api_all:  测试所有数据
    :param response: 请求响应数据
    :param projectN: 项目名称
    :param gcN: 工程名称
    :return: None
    """
    if case_data.get("is_bei_dp"):
        save_dependent_data(case_data, response_text, projectN, gcN)


def output(allure, case_data, response_text):
    output_list = get_output_list(case_data, response_text)
    for i in range(len(output_list)):
        for k, v in output_list[i].items():
            with allure.step(k + " : " + v):
                pass







