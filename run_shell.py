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
import time


#  获取相关数据
# project_name = sys.argv[1]
# gc_name = sys.argv[2]
project_name = "fpt"
gc_name = "fpt-rhqz"


data_path = "/opt/var/app/auto/api_test/gp_api_test_data/"
src_path = "/opt/var/app/auto/api_test/gp_api_test/"
result_paths = "/opt/var/app/auto/api_test/result/"
report_paths = "/opt/var/app/auto/api_test/report/"
python_env = "/home/zhangyp/pyenv/gp_api_test/bin/activate"


# 更新测试数据
updata_testdata = "cd %s && git pull" % data_path


# 更新测试脚本
updata_testscr = "cd %s && git pull" % src_path


# # 进入虚拟环境
workon = ". %s" % python_env


# 更新依赖
pip_updata = "pip install -i http://pypi.douban.com/simple/ --trusted-host pypi.douban.com -r pip.txt"


# 执行测试
now_time = time.strftime("%Y%m%d%H%M%S", time.localtime())
result_path = os.path.join(result_paths, project_name, gc_name, now_time)
test_shell = "pytest ./testcase/%s/%s/ --alluredir=%s" % (project_name, gc_name, result_path)
print(test_shell)


# 生成测试报告
report_path = os.path.join(report_paths, project_name, gc_name, now_time)
report_shell = "allure generate %s -o %s --clean" % (result_path, report_path)
print(report_shell)


shell = "%s && %s && %s && %s && %s && %s" %(updata_testdata, updata_testscr, workon, pip_updata, test_shell, report_shell)
print(shell)
os.system(shell)



