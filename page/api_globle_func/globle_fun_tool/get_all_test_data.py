#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: get_test_file_path
@time: 2020/8/25 10:56
@desc: 根据globalyml配置文件获取api_auto_case的路径，根据项目名称、工程名称获取测试项目project.yml配置文件路径
"""


import os
from util.sysEdit.filepathEdit import get_project_path
from util.fileEdit.get_data import getExcelData, getYamlData


# 获取config/global.yml配置的数据，返回dict
def get_global_config_data():
    globle_config_path = os.path.join(get_project_path(), "config", "global.yml")
    globle_data = getYamlData(globle_config_path)[0]
    return globle_data


# 根据测试数据主目录，项目名，工程名，获取工程配置数据
def get_project_config(projectN, gcN):
    globle_data = get_global_config_data()
    globle_yml_path = os.path.join(globle_data.get("data_path"),  projectN, gcN, "project.yml")
    project_config = getYamlData(globle_yml_path)[0]
    return project_config


# 获取工程配置、接口配置、测试用例、用例请求数据目录，用dict返回
def get_project_test_data(projectN, gcN):
    # 获取global配置测试数据的根目录
    deat_save_path = get_global_config_data().get("data_path")
    # 获取工程的配置
    project_config = get_project_config(projectN, gcN)
    # 根据工程配置文件获取测试用例文件路径
    project_excel = os.path.join(deat_save_path, projectN, gcN, project_config.get("save_path").get("test_case_path"))
    # 获取接口文档数据excel-apiFile
    api_config = getExcelData(project_excel, 0)
    # 获取接口测试数据excel-apiCase
    test_cases = getExcelData(project_excel, 1)
    # 获取接口测试数据data_file路径
    testdatafile_path = os.path.join(deat_save_path, projectN, gcN)
    test_data_dict = {
        "project_config": project_config,       # 项目公共配置
        "api_config": api_config,               # 工程接口要素数据
        "test_case": test_cases,                # 工程接口测试用例数据
        "testdatafile": testdatafile_path    # 测试用例数据对应的数据文件目录
    }
    return test_data_dict

