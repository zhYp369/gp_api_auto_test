#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_test
@file: output_tool
@time: 2020/9/21 17:34
@desc: 
"""
import os
from util.data_type_data.edit_json import jiexi_json, json_to_dict


def get_output_list(case_data, response_text):
    output_list = []
    gc_path = case_data.get("testdatafile")
    relative_path = case_data.get("gc_globle_data").get("save_path").get("output")
    filename = case_data.get("output")
    filename_path = os.path.join(gc_path, relative_path, filename)
    with open(filename_path, "r") as f:
        output_str = f.read().replace(" ", "").replace("\n", "")
    output_filte_list = output_str.split(";")
    for i in range(len(output_filte_list)):
        de_data_dict = {}
        filte_list = output_filte_list[i].split(">")
        if filte_list[0] == "response":
            de_data_dict = json_to_dict(response_text)
        if filte_list[0] == "bodydata":
            de_data_dict = json_to_dict(case_data.get("bodydata"))
        if filte_list[0] == "urldata":
            de_data_dict = json_to_dict(case_data.get("urldata"))
        filte_value = jiexi_json(de_data_dict, filte_list[1])
        filte_value_dict = {}
        filte_value_dict[filte_list[1].split(".")[-1]] = filte_value
        output_list.append(filte_value_dict)
    return output_list