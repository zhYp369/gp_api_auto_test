#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: edit_dependent
@time: 2020/8/26 17:13
@desc: 
"""
import os

from page.project_req_func.QZ_FUSE.jiemi_response import response_jiemi_dict
from util.sysEdit.filepathEdit import get_project_path
from util.data_type_data.edit_json import dict_to_json_write_file, json_file_to_dict, jiexi_json, json_to_dict, \
    inster_new_json, dict_to_json

dependent_dir = os.path.join(get_project_path(), "dependent", "fpt")


def get_request_dependent(request_dict, Be_dependent_request_fields_lise):
    req_dict = {}
    if Be_dependent_request_fields_lise:
        for i in range(len(Be_dependent_request_fields_lise)):
            value = jiexi_json(request_dict, Be_dependent_request_fields_lise[i])
            req_dict[Be_dependent_request_fields_lise[i]] = value
    return req_dict


def get_response_dependent(res_jiemi_dict, Be_dependent_response_fields_lise):
    res_dict = {}
    if Be_dependent_response_fields_lise:
        for i in range(len(Be_dependent_response_fields_lise)):
            value = jiexi_json(res_jiemi_dict, Be_dependent_response_fields_lise[i])
            res_dict[Be_dependent_response_fields_lise[i]] = value
    return res_dict


def save_dependent(api_all, response):
    file_name = api_all.get("case_id") + ".json"
    file_path = os.path.join(dependent_dir, file_name)
    res_jiemi_dict = response_jiemi_dict(response)
    request_dict = json_to_dict(api_all.get("data"))
    Be_dependent_fields_dict = json_to_dict(api_all.get("Be_dependent_fields"))
    Be_dependent_request_fields_lise = Be_dependent_fields_dict.get("request")
    Be_dependent_response_fields_lise = Be_dependent_fields_dict.get("response")
    Be_dependent_request_dict = get_request_dependent(request_dict, Be_dependent_request_fields_lise)
    Be_dependent_response_dict = get_response_dependent(res_jiemi_dict, Be_dependent_response_fields_lise)
    save_data_dict = {}
    save_data_dict.update(Be_dependent_request_dict)
    save_data_dict.update(Be_dependent_response_dict)
    dict_to_json_write_file(file_path, save_data_dict)


def request_data_add_dependent(api_all):
    file_name = api_all.get("d_case_id") + ".json"
    file_path = os.path.join(dependent_dir, file_name)
    dependent_key_dict = json_to_dict(api_all.get("dependent_fields"))
    dependent_value_dict = json_file_to_dict(file_path)
    request_data = json_to_dict(api_all.get("data"))
    for k, v in dependent_key_dict.items():
        request_data = inster_new_json(request_data, k, dependent_value_dict.get(v))
    api_all["data"] = dict_to_json(request_data)
    return api_all
