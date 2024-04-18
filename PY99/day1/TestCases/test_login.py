# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/11 20:09
@Auth ： 荣
@File ：test_login.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest
import os
# from ddt import ddt,data,unpack
from day1.Common.myddt import ddt,data
from day1.Common.handle_requests import send_requests
from day1.Common.handle_excel import HandleExcel
from day1.Common.handle_path import datas_dir
from day1.Common.my_logger import logger
from day1.Common.handle_confing import conf



# he = HandleExcel(os.path.join(os.path.dirname(os.path.abspath(__file__)),"api_cases.xlsx"),"login")
he = HandleExcel(datas_dir + "\\api_cases.xlsx","login")


cases = he.read_all_datas()
he.close_file()
# for case in cases:
#     print(case)
#     print(case["title"])


# @ddt
# class TestLogin(unittest.TestCase):
#     @data(*cases)
#     def test_login_ok(self,case):
#         res = send_requests(case["method"],case["url"],case["request_data"])
#         print(res.json())
#
#




# @ddt
# class TestLogin(unittest.TestCase):
#
#     @classmethod
#     def setUpClass(cls) -> None:
#         logger.info("======= 登录模块用例  开始执行========")
#
#     @classmethod
#     def tearDownClass(cls) -> None:
#         logger.info("======= 登录模块用例  执行结束========")
#
#
#     @data(*cases)
#     def test_login_ok(self,case):
#         logger.info("执行用例{}：{}".format(case["id"],case["title"]))
#
#         #步骤   测试数据 - 发起请求
#         response = send_requests(case["method"],conf.get("server","base_url") + case["url"],case["request_data"])
#         print(response.json())
#         expected = eval(case["expected"])
#
#         #断言
#         logger.info("用例的期望结果为：{}".format(case["expected"]))
#         try:
#             self.assertEqual(response.json()["status"],expected["status"])
#             self.assertEqual(response.json()["msg"],expected["msg"])
#         except AssertionError:
#             logger.exception("断言失败！")
#             raise
#






@ddt
class TestRegister(unittest.TestCase):

    @classmethod
    def setUpClass(cls) -> None:
        logger.info("======  登录模块用例 开始执行  ========")

    @classmethod
    def tearDownClass(cls) -> None:
        logger.info("======  登录模块用例 执行结束  ========")


    @data(*cases)
    def test_register_ok(self,case):
        # print("本条测试数据：",case)
        logger.info("*********   执行用例{}：{}   *********".format(case["id"],case["title"]))

        # 替换 - 动态 -
        # 请求数据 #phone# 替换 new_phone
        # check_sql里的  #phone# 替换 new_phone
        # if case["request_data"].find("#phone#") != -1:
        #     new_phone = get_new_phone()
        #     case = replace_mark_with_data(case,"#phone#",new_phone)

        #将测试请求数据转换为字典格式
        case["request_data"] = eval(case["request_data"])
        # 步骤 测试数据 - 发起请求
        response = send_requests(case["method"],conf.get("server","base_url") + case["url"],case["request_data"])
        # print(response.json())
        logger.info("登陆结果为：{}".format(response.json()))
        # 期望结果，从字符串转换成字典对象。
        # expected = eval(case["expected"])
        #
        # # 断言 - code == 0 msg == ok
        # logger.info("用例的期望结果为：{}".format(case["expected"]))
        # try:
        #     self.assertEqual(response.json()["status"],expected["status"])
        #     self.assertEqual(response.json()["msg"], expected["msg"])
        #     # 如果check_sql有值，说明要做数据库校验。
        #     # if case["check_sql"]:
        #     #     # logger.info()
        #     #     result = db.select_one_data(case["check_sql"])
        #     #     self.assertIsNotNone(result)
        # except AssertionError:
        #     logger.exception("断言失败！")
        #     raise
