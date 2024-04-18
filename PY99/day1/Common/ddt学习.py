# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/15 18:38
@Auth ： 荣
@File ：ddt学习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest
from day1.Common.handle_excel import HandleExcel
from day1.Common.handle_path import datas_dir
from day1.Common.myddt import ddt,data
from day1.Common.handle_requests import send_requests


# he = HandleExcel(datas_dir + "\\api_cases.xlsx","login")
#
#
# cases = he.read_all_datas()
# he.close_file()
# print(cases)


cases = [{'id': 1, 'title': '正常登录', 'method': 'POST', 'url': '/token/get', 'request_data': '{\n    "loginName":"admin",\n    "pssWord":"7c4a8d09ca3762af61e59520943dc26494f8941b"\n}', 'expected': '{\n    "status": 1,\n    "msg": "登录成功",\n    "data": {\n        "token": "eyJhbGciOiJIUzI1NiJ9.eyJqdGkiOiIxIiwic3ViIjoiYWRtaW4iLCJpc3MiOiJEUlpLIiwiaWF0IjoxNzEyMDI4OTA3LCJleHAiOjE3MTIwOTM3MDd9.LBQLzIE9jovM4md8psL46eV4J7M9NhHEIx5pyekqcuc",\n        "loginStatus": "2"\n    }\n}'},
         {'id': 2, 'title': 'name为空', 'method': 'POST', 'url': '/token/get', 'request_data': '{\n    "loginName":"",\n    "pssWord":"7c4a8d09ca3762af61e59520943dc26494f8942b"\n}', 'expected': '{\n    "status": 0,\n    "msg": "用户名不能为空"\n}'},
         {'id': 3, 'title': 'word为空', 'method': 'POST', 'url': '/token/get', 'request_data': '{\n    "loginName":"admin",\n    "pssWord":""\n}', 'expected': '{\n    "status": 0,\n    "msg": "密码不能为空"\n}'},
         {'id': 4, 'title': 'name错误', 'method': 'POST', 'url': '/token/get', 'request_data': '{\n    "loginName":"admin1",\n    "pssWord":"7c4a8d09ca3762af61e59520943dc26494f8941b"\n}', 'expected': '{\n    "status": 0,\n    "msg": "用户名或密码错误"\n}'},
         {'id': 5, 'title': 'word错误', 'method': 'POST', 'url': '/token/get', 'request_data': '{\n    "loginName":"admin",\n    "pssWord":"7c4a8d09ca3762af61e59520943dc26494f8941b1"\n}', 'expected': '{\n    "status": 1,\n    "msg": "用户名或密码错误"\n}'}]

@ddt
class TestLogin_1(unittest.TestCase):
    @data(*cases)
    def test_login_ok(self,case):
        res = send_requests(case["method"],case["url"],case["request_data"])
        print(res.json())

