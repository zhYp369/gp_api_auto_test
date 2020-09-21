#!/usr/bin/env python
# coding=utf-8

"""
@author: zhangyp
@project: apiAutoTest
@file: get_path
@time: 2020/8/26 16:56
@desc: 
"""
import os


def get_super_dir(now_dir, num):
    for i in range(num):
        now_dir = os.path.dirname(now_dir)
    return now_dir


def get_project_dir():
    now_dir = os.path.dirname(__file__)
    project = get_super_dir(now_dir, 2)
    return project


def check_and_creat_dir(file_url):
    '''
    判断文件是否存在，文件路径不存在则创建文件夹
    :param file_url: 文件路径，包含文件名
    :return:
    '''
    file_gang_list = file_url.split('/')
    if len(file_gang_list) > 1:
        [fname, fename] = os.path.split(file_url)
        print(fname, fename)
        if not os.path.exists(fname):
            os.makedirs(fname)
        else:
            return None
        # 还可以直接创建空文件

    else:
        return None


