#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: assemble_tool
@time: 2020/9/18 14:44
@desc: 
"""


def get_case_api_config(test_case, api_config_list):
    """
    根据传入的接口id，和接口文档数据，获取对应接口的配置数据
    :param api_id:
    :param api_config_list:
    :return: 返回接口信息api_config_dict
    """
    api_id = test_case.get("api_id")
    api_config_dict = {}
    for i in range(len(api_config_list)):
        if api_config_list[i].get("api_id") == api_id:
            api_config_dict = api_config_list[i]
            break
        else:
            continue
    return api_config_dict
