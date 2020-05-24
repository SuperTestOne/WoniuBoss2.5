# encoding: utf-8
# @author: yinqianjun
# @file: G_StudentManage_Test.py
# @time: 2020/5/24 15:02
import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util
from WoniuBoss_Requests_Test.lib.G_Student_Manage_Action import SM_Action

class SM_Test(unittest.TestCase):

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    def tearDown(self):
        self.session.close()

    # 获取查询学员信息数据
    search_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[0]
    search_stuInfo = Util.get_excel(search_stuData)
    # 查询学员信息测试
    @parameterized.expand(search_stuInfo)
    def test_search_stuInfo(self, search_url, search_data, expect):
        res = SM_Action(self.session).do_post(search_url, search_data)
        res_list = res.json()['list']
        if len(res_list) == 0:
            actual = 'fail'
        else:
            actual = 'pass'
        self.assertEqual(actual, expect)

    # 获取修改学员信息数据
    #alter_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[1]
    #alter_stuInfo = Util.get_excel(alter_stuData)
    #修改学员信息测试
    #@parameterized.expand(alter_stuInfo)
    #def test_alter_studentInfo(self):
     #   pass

    #获取查询日常考评evaluation数据
    evaluation_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[2]
    evaluation_stuInfo = Util.get_excel(evaluation_stuData)
    #查询日常考评测试
    @parameterized.expand(evaluation_stuInfo)
    def test_search_evaluation(self,search_url,search_data,expect):
        res = SM_Action(self.session).do_post(search_url, search_data)
        if res.text !='' :
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #获取查询周考信息
    weekExam_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[3]
    weekExam_stuInfo = Util.get_excel(weekExam_stuData)
    #查询周考测试
    @parameterized.expand(weekExam_stuInfo)
    def test_search_weekExam(self,search_url,search_data,expect):
        res = SM_Action(self.session).do_post(search_url, search_data)
        res_list = res.json()['list']
        if len(res_list) == 0:
            actual = 'fail'
        else:
            actual = 'pass'
        self.assertEqual(actual, expect)

    #获取录入周考成绩数据
    add_weekExam_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[4]
    add_weekExam_stuInfo = Util.get_excel(add_weekExam_stuData)
    #录入周考测试
    @parameterized.expand(add_weekExam_stuInfo)
    def test_add_weekExam(self,add_url,add_data,expect):
        res = SM_Action(self.session).do_post(add_url, add_data)
        if res.text == 'success':
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #获取上传文件的参数
    upload_weekExam_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[5]
    upload_weekExam_stuInfo = Util.get_excel(upload_weekExam_stuData)
    #上传周考文件测试
    @parameterized.expand(upload_weekExam_stuInfo)
    def test_add_weekExam(self, add_url, add_data, expect):
        res = SM_Action(self.session).do_post(add_url, add_data)
        if '上传成功' in res.text:
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #获取阶段考评查询数据
    search_examination_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[6]
    search_examination_stuInfo = Util.get_excel(search_examination_stuData)
    #阶段考评查询测试
    @parameterized.expand(search_examination_stuInfo)
    def test_search_examination(self, search_url, search_data, expect):
        res = SM_Action(self.session).do_post(search_url, search_data)
        res_list = res.json()['list']
        if len(res_list) == 0:
            actual = 'fail'
        else:
            actual = 'pass'
        self.assertEqual(actual, expect)

    #获取阶段考评录入数据
    add_examination_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[7]
    add_examination_stuInfo = Util.get_excel(add_examination_stuData)
    #阶段考评录入测试
    @parameterized.expand(add_examination_stuInfo)
    def test_add_examination(self,add_url,add_data,expect):
        res = SM_Action(self.session).do_post(add_url, add_data)
        if res.text == 'success':
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

    #获取阶段考上传文件数据
    upload_examination_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[8]
    upload_examination_stuInfo = Util.get_excel(upload_examination_stuData)
    #阶段考文件上传测试
    @parameterized.expand(upload_examination_stuInfo)
    def upload_examination(self):
        pass

    #获取综合成绩查询数据
    search_comprehensive_stuData = Util.get_json('..\\conf\\G_SM_Excel.conf')[9]
    search_comprehensive_stuInfo = Util.get_excel(search_comprehensive_stuData)
    #综合成绩查询测试
    @parameterized.expand(search_comprehensive_stuInfo)
    def test_search_comprehensive(self, search_url, search_data, expect):
        res = SM_Action(self.session).do_post(search_url, search_data)
        res_list = res.json()['list']
        if len(res_list) == 0:
            actual = 'fail'
        else:
            actual = 'pass'
        self.assertEqual(actual, expect)
