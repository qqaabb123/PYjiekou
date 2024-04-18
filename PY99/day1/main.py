# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/11 20:34
@Auth ： 荣
@File ：main.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""


import unittest
import os
from day1.Common.handle_path import cases_dir,reports_dir


from BeautifulReport import BeautifulReport
#收集用例
# caase_dir = os.path.dirname(os.path.abspath(__file__))

s = unittest.TestLoader().discover(cases_dir)

#生成报告
br = BeautifulReport(s)

br.report("自动化", "report.html",reports_dir )
