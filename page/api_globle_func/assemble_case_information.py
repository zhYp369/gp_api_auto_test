#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: assemble_req_data
@time: 2020/8/26 9:12
@desc:
"""
from page.api_globle_func.globle_fun_tool.get_all_test_data import get_project_test_data
from page.api_globle_func.globle_fun_tool.assemble_tool import get_case_api_config


def get_test_data(all_test_data):
    """
    获取接口信息和数据，更新测试数据，删选执行用例
    """
    # 定义一个字典，用来组装每个用例的测试数据
    all_run_case = []
    # 根据参数（用例的所有数据，测试用例，测试报文，接口配置）
    gc_ymal_data = all_test_data.get("project_config")
    api_config_data = all_test_data.get("api_config")
    test_cases = all_test_data.get("test_case")

    # 循环每一个用例，进行组装测试数据
    for i in range(len(test_cases)):
        # 定义一个字典，用来组装每个用例的测试数据
        test_case_data = {}
        test_case = test_cases[i]
        if test_case["is_run"] == "yes":
            test_case_data["gc_globle_data"] = gc_ymal_data
            test_case_data["api_config"] = get_case_api_config(test_case, api_config_data)
            test_case_data["case_data"] = test_case
            test_case_data["testdatafile"] = all_test_data.get("testdatafile")
            title = test_case.get("case_id") + test_case.get("test_discribe")
            test_case_data_title = (test_case_data, title)
            all_run_case.append(test_case_data_title)
        else:
            continue
    return all_run_case


def get_testData_title(projectN, gcN):
    all_test_data = get_project_test_data(projectN, gcN)
    # 获取所有用例测试数据
    all_run_case = get_test_data(all_test_data)
    # 组装testcase, title, expected
    return all_run_case