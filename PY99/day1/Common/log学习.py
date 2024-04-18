# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/12 11:43
@Auth ： 荣
@File ：log学习.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import logging
from logging import Handler


logger = logging.getLogger("jiekou")

#设置日志输出级别
logger.setLevel(logging.INFO)


#设置日志输出在哪些渠道
# logging.StreamHandler
handle1 = logging.StreamHandler()

#设置渠道自己的输出级别
handle1.setLevel(logging.ERROR)

#设置渠道输出的内容格式
# logging.Formatter

fmt = "%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d行：%(message)s"
formatter = logging.FileHandler(fmt)

#将日志格式绑定到渠道当中
handle1.setFormatter(formatter)


#将设置好 的渠道，添加到日志收集器上
logger.addHandler(handle1)


#添加filehandler
handle2 = logging.FileHandler("my_py30.log",encoding="utf-8")


handle2.setFormatter(formatter)
logger.addHandler(handle2)



logger.info("hello,py30,我的第一个收集器成功了吗？？？")
logger.error("ERROR!!!")