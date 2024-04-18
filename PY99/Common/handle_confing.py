# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/12 16:48
@Auth ： 荣
@File ：handle_confing.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""
import os
from configparser import ConfigParser
from Common.handle_path import cof_dir

class HandleConfing(ConfigParser):
    def __init__(self,file_path):
        super().__init__()
        self.read(file_path,encoding="utf-8")

file_path = os.path.join(cof_dir,"nmn.ini")

# print(dir)
conf = HandleConfing(file_path)



if __name__ == '__main__':
    conf = HandleConfing("../Conf/nmn.ini")
    conf.get("log","name")
    aaa = conf.get("server", "base_url")
    print(aaa)