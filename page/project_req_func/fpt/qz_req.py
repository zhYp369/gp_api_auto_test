#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: zwcm_req_funcs
@time: 2020/6/5 13:07
@desc:
"""

from page.api_globle_func.api_req import req_http
from page.project_req_func.fpt.qz_req_tool import get_req_data



def qz_req(api_all):
    """
    融合前置接口请求公共方法
    :param api_all:
    :return:
    """
    url = api_all.get("url")
    method = api_all.get("method")
    kwargs = {}
    kwargs["headers"] = api_all.get("header")
    # if api_all.get("d_case_id"):
    #     api_all = request_data_add_dependent(api_all, projectN, gcN)
    kwargs["data"] = get_req_data(api_all)
    kwargs["verify"] = False
    respon = req_http(url=url, method=method, kwargs=kwargs)
    return respon



