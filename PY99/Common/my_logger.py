# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/11 20:39
@Auth ： 荣
@File ：my_logger.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import logging
import os
from Common.handle_confing import conf
from Common.handle_path import logs_dir








class MyLogger(logging.Logger):
    def __init__(self,file=None):
        #设置输出级别、输出渠道、输出日志格式
        # super().__init__(name,level)
        super().__init__(conf.get("log","name"),conf.get("log","level"))


        #日志格式
        fmt = '%(asctime)s %(name)s %(levelname)s %(filename)s %(lineno)d行：%(message)s'
        formatter = logging.Formatter(fmt)

        #控制台渠道
        handle1 = logging.StreamHandler()
        handle1.setFormatter(formatter)
        self.addHandler(handle1)


        if file:
            #文件渠道
            handle2 = logging.FileHandler(file,encoding="utf-8")
            handle2.setFormatter(formatter)
            self.addHandler(handle2)


#是否需要写入文件
if conf.getboolean("log","file_ok"):
    file_name = os.path.join(logs_dir,conf.get("log","file_name"))
else:
    file_name = None
print(file_name)
# mlogger = MyLogger(conf.get("log","name"),conf.get("log","level"),file_name)
logger = MyLogger(file_name)
# dir = logs_dir + "\\my_logger.log"
# print(dir)

# logger.info("测试，我自己封装的日志类！")
# if __name__ == '__main__':
#     logger = MyLogger(conf.get("log","name"),file=r"C:\Users\26360\PycharmProjects\PY99\day1\Outputs\logs\my_logger.log")
#     logger.info("测试，我自己封装的日志类！")






