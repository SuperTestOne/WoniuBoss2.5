# encoding: utf-8
# @author: yinqianjun
# @file: E_Market_Test.py
# @time: 2020/5/24 10:47
import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class L_Test(unittest.TestCase):

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    def tearDown(self):
        self.session.close()


    #获取新增资源数据
    add_data = Util.get_json('..\\conf\\E_M_Excel.conf')[0]
    add_info = Util.get_excel(add_data)
    # 新增市场资源测试
    @parameterized.expand(add_info)
    def test_add_resource(self,add_url,add_data,expect):
        from WoniuBoss_Requests_Test.lib.E_Market_Action import M_Action
        res = M_Action(self.session).do_post(add_url,add_data)
        if res.text=='success':
            actual = 'pass'
        else:
            actual ='fail'
        self.assertEqual(actual, expect)

    #获取查询资源数据
    search_data = Util.get_json('..\\conf\\E_M_Excel.conf')[1]
    search_info = Util.get_excel(search_data)
    # 查询市场资源测试
    @parameterized.expand(search_info)
    def test_add_resource(self,search_url,search_data,expect):
        from WoniuBoss_Requests_Test.lib.E_Market_Action import M_Action
        res = M_Action(self.session).do_post(search_url,search_data)
        if res.text == "":
            actual = 'fail'
        else:
            actual ='pass'
        self.assertEqual(actual, expect)

    #获取上传简历数据
    upload_data = Util.get_json('..\\conf\\E_M_Excel.conf')[2]
    upload_info = Util.get_excel(upload_data)
    #上传简历测试
    @parameterized.expand(upload_info)
    def test_upload_resource(self, upload_url, upload_data, expect):
        from WoniuBoss_Requests_Test.lib.E_Market_Action import M_Action
        res = M_Action(self.session).do_post(upload_url, upload_data)
        if res.text == "":
            actual = 'fail'
        else:
            actual = 'pass'
        self.assertEqual(actual, expect)

    #获取修改资源数据
    alter_data = Util.get_json('..\\conf\\E_M_Excel.conf')[3]
    alter_info = Util.get_excel(alter_data)
    #修改资源测试
    @parameterized.expand(alter_info)
    def test_upload_resource(self, alter_url, alter_data, expect):
        from WoniuBoss_Requests_Test.lib.E_Market_Action import M_Action
        res = M_Action(self.session).do_post(alter_url, alter_data)
        if res.text == "修改成功":
            actual = 'pass'
        else:
            actual = 'fail'
        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()

