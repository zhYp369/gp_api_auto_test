#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: assert_result
@time: 2020/6/9 8:39
@desc: 
"""
import json


def assert_result_in(respon, new_case_data):
    """
    校验订单上传结果
    :param respon:
    :param api_all_dict:
    :return:
    """
    expecteds = new_case_data.get("expected")
    respon = respon.replace(" ", "").replace("\n", "")
    for expected in expecteds:
        expected = expected.replace(" ", "").replace("\n", "")
        try:
            assert expected in respon
        except:
            error = {
                "Expected_results": expected,
                "respon.text": respon,
            }
            error_json = json.dumps(error, ensure_ascii=False)
            raise Exception(error_json)
