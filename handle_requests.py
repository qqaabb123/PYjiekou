# -*- coding: utf-8 -*-
"""
@Time ： 2024/4/11 18:53
@Auth ： 荣
@File ：handle_requests.py
@IDE ：PyCharm
@Motto：ABC(Always Be Coding)
"""

import requests
from day1.Common.my_logger import logger
from day1.Common.handle_confing import conf



# def send_requests(method,url,data=None,token=None):
#     """
#
#     :param method: 请求的方式
#     :param url: 请求的地址
#     :param data: 请求的参数
#     :param token: 所需要的token，有就需要上传
#     :return:
#     """
#     #得到请求头
#     headers = __handle_header(token)
#     logger.info("请求头为：{}".format(headers))
#     #根据请求类型，调用请求方法
#     method = method.upper()
#     if method == "GET":
#         resp = requests.get(url,data,headers=headers)
#     else:
#         resp = requests.post(url,json=data,headers=headers)
#     return resp

def send_requests(method,url,data=None,token=None):
    """

    :param method:
    :param url:
    :param data:字典形式的数据。
    :param token:
    :return:
    """
    logger.info("发起一次HTTP请求")
    # 得到请求头
    headers = __handle_header(token)
    # 得到完整的url - 拼接url
    # url = __pre_url(url)
    # 请求数据的处理 - 如果是字符串，则转换成字典对象。
    # data = __pre_data(data)
    # 将请求数据转换成字典对象。
    logger.info("请求头为：{}".format(headers))
    logger.info("请求方法为：{}".format(method))
    logger.info("请求url为：{}".format(url))
    logger.info("请求数据为：{}".format(data))
    # 根据请求类型，调用请求方法
    method = method.upper()  # 大写处理
    if method == "GET":
        resp = requests.get(url,data,headers=headers)
    else:
        resp = requests.post(url,json=data,headers=headers)
    # logger.info("响应状态码为：{}".format(resp.status_code))
    # logger.info("响应数据为：{}".format(resp.json()))
    return resp

def __handle_header(token=None):
    '''
    处理请求头。加上项目当中必带的请求头。
    :param token:token值
    :return: 处理之后 的headers字典
    '''
    headers = {"Content-Type": "application/json;charset=UTF-8"

            }
    if token:
        # token = {"accessToken": "/{}".format(token)}
        headers["accessToken"] = "{}".format(token)
    return headers




def __pre_url(url):
    """
    拼接接口的url地址。
    """
    base_url = conf.get("server", "base_url")
    if url.startswith("/"):
        return base_url + url
    else:
        return base_url + "/" + url

#
# def __pre_data(data):
#     """
#     如果data是字符串，则转换成字典对象。
#     """
#     if data is not None and isinstance(data,str):
#         # 如果有null，则替换为None
#         if data.find("null") != -1:
#             data = data.replace("null", "None")
#         # 使用eval转成字典.eval过程中，如果表达式有涉及计算，会自动计算。
#         data = eval(data)
#     return data
#



if __name__ == '__main__':
    logion_url = "http://192.168.66.67/ykt/token/get"
    logion_datas = {
    "loginName":"admin",
    "pssWord":"7c4a8d09ca3762af61e59520943dc26494f8941b"
}
    resp = send_requests("POST",logion_url,logion_datas)
    # print(resp.json())
    token = resp.json()["data"]["token"]
    # logger.info("登录的请求头为：{}".format(__handle_header()))
    # print(token)

    # visitor_reservation_url = "http://192.168.66.67/ykt/api/v1/visitor/create"
    # visitor_reservation__data = {
    #     "carNo":"粤B921981",
    #     "startTime":"2024-09-14 11:11:11",
    #     "endTime":"2024-09-17 11:11:11",
    #     "visitName":"张三",
    #     "visitorPhone":"19852461254",
    #     "visitorReason":"备注",
    #     "dsn":"145456784321,456451544653",
    #     "objectId":16
    # }
    # resp = send_requests("POST",visitor_reservation_url,visitor_reservation__data,token)
    # print(resp.json())