#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: get_req_data_tool
@time: 2020/9/18 16:28
@desc: 
"""
# test_case_data["gc_globle"] = gc_ymal_data
# test_case_data["api_config"] = get_case_api_config(test_case, api_config_data)
# test_case_data["case_data"] = test_case
# test_case_data["testdatafile"] = all_test_data.get("testdatafile")
import os

from util.data_type_data.edit_json import json_to_dict


def get_case_id(testdata):
    case_id = testdata.get("case_data").get("case_id")
    return case_id


def get_test_discribe(testdata):
    test_discribe = testdata.get("case_data").get("test_discribe")
    return test_discribe


def get_api_id(testdata):
    api_id = testdata.get("case_data").get("api_id")
    return api_id


def get_url(testdata):
    hp = testdata.get("gc_globle_data").get("hp")
    api_path_url = testdata.get("api_config").get("api_url")
    url = hp + api_path_url
    return url


def get_method(testdata):
    if testdata.get("case_data").get("method"):
        method =testdata.get("case_data").get("method")
    else:
        method =testdata.get("api_config").get("method")
    return method


def get_header(testdata):
    if testdata.get("case_data").get("header"):
        header =testdata.get("case_data").get("header")
    else:
        header =testdata.get("api_config").get("header")
    header = json_to_dict(header)
    return header


def get_global_data(testdata):
    globle_file = testdata.get("api_config").get("global_file")
    if globle_file:
        testdatafile = testdata.get("testdatafile")
        relative_path = testdata.get("gc_globle_data").get("save_path").get("req_globle")
        globle_file_path = os.path.join(testdatafile, relative_path, globle_file)
        with open(globle_file_path, "r", encoding="utf8") as f:
            global_data = f.read()
    else:
        global_data = ""
    return global_data


def get_yw_params(testdata):
    params_file = testdata.get("case_data").get("params_file")
    if params_file:
        testdatafile = testdata.get("testdatafile")
        relative_path = testdata.get("gc_globle_data").get("save_path").get("req_params")
        params_file_path = os.path.join(testdatafile, relative_path, params_file)
        with open(params_file_path, "r", encoding="utf8") as f:
            params_data = f.read()
    else:
        params_data = ""
    return params_data


def get_yw_data(testdata):
    data_file = testdata.get("case_data").get("data_file")
    if data_file:
        testdatafile = testdata.get("testdatafile")
        relative_path = testdata.get("gc_globle_data").get("save_path").get("req_data")
        data_file_path = os.path.join(testdatafile, relative_path, data_file)
        with open(data_file_path, "r", encoding="utf8") as f:
            req_data = f.read()
    else:
        req_data = ""
    return req_data


def get_cookie(testdata):
    cookie = testdata.get("api_config").get("cookie")
    return cookie


def get_tonken(testdata):
    tonken = testdata.get("api_config").get("tonken")
    return tonken


def get_d_case_id(testdata):
    d_case_id = testdata.get("case_data").get("dp_case_id")
    return d_case_id


def get_d_field_filename(testdata):
    dependent_field = testdata.get("case_data").get("dp_data_file")
    return dependent_field


def get_is_bei_dp(testdata):
    is_bei_dp = testdata.get("case_data").get("is_bei_dp")
    return is_bei_dp


def get_expected(testdata):
    expected_isfile = testdata.get("case_data").get("expected_isfile")
    if expected_isfile=="yes":
        testdatafile = testdata.get("testdatafile")
        relative_path = testdata.get("gc_globle_data").get("save_path").get("expected")
        expected_file = testdata.get("case_data").get("case_id") + ".txt"
        expected_file_path = os.path.join(testdatafile, relative_path, expected_file)
        with open(expected_file_path, "r", encoding="utf8") as f:
            expected_data_list = f.readlines()
    else:
        expected_data_list = testdata.get("case_data").get("expected_data").replace("\n", "").split(";")
    return expected_data_list


def get_output(testdata):
    outputFileName = testdata.get("case_data").get("output")
    return outputFileName