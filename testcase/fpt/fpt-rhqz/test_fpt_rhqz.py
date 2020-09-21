#!/usr/bin/env python
# coding=utf-8

'''
@author: zhangyp
@file: test_postman_api.py
@time: 2019/7/8 20:54
@desc: 测试fpsyy-interface工程接口用例 API
'''

import allure
import pytest
from page.project_req_func.fpt.edit_qz_response import get_response_text
from page.project_req_func.fpt.qz_req import qz_req
from page.project_req_func.fpt.qz_fuse_assert import assert_result_in
from page.api_globle_func.edit_test_data import updata_req_data, get_req_data, save_dependent, output
from page.api_globle_func.assemble_case_information import get_testData_title
# 获取相关数据文件的数据，项目配置文件数据，接口基本信息数据，测试用例数据
projectN = "fpt"
gcN = "fpt-rhqz"
testData_title = get_testData_title(projectN, gcN)


@allure.feature("发票通项目")
@allure.story("融合前置接口测试")
@allure.title("{title}")
@pytest.mark.parametrize('case_data, title', testData_title)
@pytest.mark.A
def test_timestamp(case_data, title):
# 获取接口相关数据
    case_data = get_req_data(case_data)
# 2、测试数据更新获取
    new_case_data = updata_req_data(case_data, projectN, gcN)
# 3、请求接口(分项目)
    response = qz_req(new_case_data)
# # 4、响应结果处理
    response_text = get_response_text(response)
# # 5、校验测试结果
    assert_result_in(response_text, new_case_data)
# # 6、save
    save_dependent(case_data, response_text, projectN, gcN)
# # 7、输出关键数据
    output(allure, new_case_data, response_text)




