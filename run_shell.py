#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: gp_api_auto_test
@file: run_shell
@time: 2020/9/9 14:35
@desc: 
"""

import os
import sys
from util.num.edit_time import get_time
from util.fileEdit.get_data import getYamlData

#  获取相关数据
# project_name = sys.argv[1]
# gc_name = sys.argv[2]
project_name = "fpt"
gc_name = "fpt-rhqz"
config_file = os.path.join(os.path.dirname(__file__), "config", "global.yml")
config_data = getYamlData(config_file)[0]


# 更新测试数据
data_path = config_data.get("data_path")
os.system('cd %s' % data_path)
os.system('git pull')


# 更新测试脚本
src_path = config_data.get("src_path")
os.system('cd %s' % src_path)
os.system('git pull')


# 进入虚拟环境
workon = config_data.get("python_env")
os.system('workon %s' % workon)


# 执行测试
now_time = get_time()
result_path = os.path.join(config_data.get("result_path"), project_name, gc_name, now_time)
test_shell = "pytest ./testcase/%s/%s/ --alluredir=%s" % (project_name, gc_name, result_path)
os.system(test_shell)


# 生成测试报告
report_path = os.path.join(config_data.get("report_path"), project_name, gc_name, now_time)
report_shell = "allure generate %s -o %s --clean" % (result_path, report_path)




