import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util
from WoniuBoss_Requests_Test.tools.service import Service
from WoniuBoss_Requests_Test.lib.F_TrainingResource_Action import TR_Action

class TR_Test(unittest.TestCase):
    #获取查询数据
    query_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[2]
    query_info = Util.get_excel(query_contents)
    #获取新增数据
    add_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[3]
    add_info = Util.get_excel(add_contents)
    #获取修改数据
    edit_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[4]
    edit_info = Util.get_excel(edit_contents)
    #获取跟踪数据
    track_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[5]
    track_info = Util.get_excel(track_contents)
    # 获取废弃数据
    abandon_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[6]
    abandon_info = Util.get_excel(abandon_contents)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.session = Service.get_session()

    #查询测试
    @parameterized.expand(query_info)
    def test_query(self,query_url,query_data,expect):
        resp = TR_Action(self.session).do_query(query_url,query_data)
        if len(resp) >= 0:
            actual = "pass"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)

    #新增测试
    @parameterized.expand(add_info)
    def test_add(self, add_url, add_data, expect):
        resp = TR_Action(self.session).do_add(add_url, add_data)
        self.assertEqual(resp, expect)

    #修改测试
    @parameterized.expand(edit_info)
    def test_edit(self, edit_url, edit_data, expect):
        resp = TR_Action(self.session).do_edit(edit_url, edit_data)
        self.assertEqual(resp, expect)

    #跟踪测试
    @parameterized.expand(track_info)
    def test_track(self, track_url, track_data, expect):
        resp = TR_Action(self.session).do_track(track_url, track_data)
        self.assertEqual(resp, expect)

    #废弃测试
    @parameterized.expand(abandon_info)
    def test_abandon(self, abandon_url,abandon_data, expect):
        resp = TR_Action(self.session).do_abandon(abandon_url,abandon_data)
        self.assertEqual(resp, expect)

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        pass