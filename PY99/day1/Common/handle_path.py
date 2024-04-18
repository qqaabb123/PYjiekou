# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/11 20:56
@Auth ： 荣
@File ：handle_path.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
# print(base_dir)
#测试用例的路径
cases_dir = os.path.join(base_dir,"TestCases")
#测试数据的路径
datas_dir = os.path.join(base_dir,"TestDatas")
# 测试报告
reports_dir = os.path.join(base_dir,"Outputs\\reports")
# 日志的路径
logs_dir = os.path.join(base_dir,"Outputs\\logs")
# 配置文件的路径
cof_dir = os.path.join(base_dir,"Conf")


print(logs_dir)