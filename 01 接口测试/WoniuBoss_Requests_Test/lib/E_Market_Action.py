# encoding: utf-8
# @author: yinqianjun
# @file: E_Market_Action.py
# @time: 2020/5/24 10:37
class M_Action():

    def __init__(self,session):
        self.session = session

    #发送post请求
    def do_post(self,url,data):
        resp = self.session.post(url=url, data=data)
        return resp

