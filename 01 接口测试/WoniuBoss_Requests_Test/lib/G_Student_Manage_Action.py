# encoding: utf-8
# @author: yinqianjun
# @file: G_Student_Manage_Action.py
# @time: 2020/5/24 14:50
class SM_Action():

    def __init__(self,session):
        self.session = session

    #发送post请求
    def do_post(self,url,data):
        resp = self.session.post(url=url, data=data)
        return resp

    #文件上传
    def do_upload(self,url,data,path):
        resp = self.session.post(url=url, data=data,files=path)
        return resp

