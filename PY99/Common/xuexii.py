# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/15 17:54
@Auth ： 荣
@File ：xuexii.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import unittest


class test_unittest(unittest.TestCase):

    @classmethod
    def setUpClass(cls):
        print("测试环境初始化，开始执行setup")

    @classmethod
    def tearDownClass(cls):
        print("测试执行完成，运行teardown")

        print("------------------------------")

    def test_a(self):
        print("开始执行test_a用例")

    def test_A(self):
        print("开始执行test_A用例")

    def test_1(self):
        print("开始执行test_1用例")


if __name__ == "__main__":
    unittest.main()
