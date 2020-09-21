#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: edit_qz_response
@time: 2020/9/21 14:48
@desc: 
"""
from page.project_req_func.fpt.jiemi_response import response_jiemi_dict
from util.data_type_data.edit_json import dict_to_json


def get_response_text(response):
    response.encoding = "utf-8"
    respon_text = response.text.replace("\n", "").replace("\t", "")
    res_jiemi_dict = response_jiemi_dict(respon_text)
    text = dict_to_json(res_jiemi_dict)
    return text


