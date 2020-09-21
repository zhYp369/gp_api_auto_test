#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: updata_dependent_tool
@time: 2020/9/20 11:18
@desc: 
"""
import os

from util.data_type_data.edit_json import json_file_to_dict, jiexi_json, inster_new_json, json_to_dict, \
    dict_to_json_write_file, dict_to_json
from util.sysEdit.filepathEdit import get_project_path

dependent_dir = os.path.join(get_project_path(), "dependent")



def get_dependent_field(casedata):
    d_field_dict = {}
    gc_path = casedata.get("testdatafile")
    relative_path = casedata.get("gc_globle_data").get("save_path").get("dp")
    dp_file = casedata.get("case_data").get("case_id") + ".txt"
    dp_file_path = os.path.join(gc_path, relative_path, dp_file)
    with open(dp_file_path, "r") as f:
        d_field_list = f.readlines()
    for i in range(len(d_field_list)):
        d_field = d_field_list[i].replace(" ", "").replace("\n", "")
        if d_field:
            req_field = d_field.split(":")[0]
            de_field = d_field.split(":")[1]
            d_field_dict[req_field] = de_field
    return d_field_dict


def get_de_field_value(d_field, projectN, gcN):
    filename = d_field.split(">")[0] + ".json"
    file_path = os.path.join(dependent_dir, projectN, gcN, filename)  # 组装整个依赖文件的路径
    file_path_data_dict = json_file_to_dict(file_path)
    d_field_value = jiexi_json(file_path_data_dict, d_field.split(">")[1])
    return d_field_value


def get_updata_dependent(casedata, projectN, gcN):
    d_field_dict = get_dependent_field(casedata)
    for k, v in d_field_dict.items():
        d_field_value = get_de_field_value(v, projectN, gcN)
        req_de_list = k.split(">")
        if req_de_list[0] == "bodydata":
            casedata["bodydata"] = dict_to_json(inster_new_json(json_to_dict(casedata.get("bodydata")), req_de_list[1], d_field_value))
        if req_de_list[0] == "urldata":
            casedata["urldata"] = dict_to_json(inster_new_json(json_to_dict(casedata.get("urldata")), req_de_list[1], d_field_value))
        if req_de_list[0] == "globaldata":
            casedata["globaldata"] = dict_to_json(inster_new_json(json_to_dict(casedata.get("globaldata")), req_de_list[1], d_field_value))
    return casedata


def save_dependent_data(case_data, response_text, projectN, gcN):
    file_name = case_data.get("case_id") + ".json"  # 用测试用例id定义依赖数据文件名字的json文件
    file_path = os.path.join(dependent_dir, projectN, gcN, file_name)  # 组装整个依赖文件的路径
    save_data_dict = {}
    if case_data.get("bodydata"):
        save_data_dict["bodydata"] = json_to_dict(case_data.get("bodydata"))
    if case_data.get("urldata"):
        save_data_dict["urldata"] = json_to_dict(case_data.get("urldata"))
    save_data_dict["response"] = json_to_dict(response_text)
    dict_to_json_write_file(file_path, save_data_dict)

