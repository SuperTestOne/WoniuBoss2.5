import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util
from WoniuBoss_Requests_Test.tools.service import Service
from WoniuBoss_Requests_Test.lib.F_DeliverResource_Action import DR_Action

class DR_Test(unittest.TestCase):
    #获取查询数据
    query_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[7]
    query_info = Util.get_excel(query_contents)
    # 获取转交数据
    deliver_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[8]
    deliver_info = Util.get_excel(deliver_contents)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.session = Service.get_session()

    #查询测试
    @parameterized.expand(query_info)
    def test_query(self,query_url,query_data,expect):
        resp = DR_Action(self.session).do_query(query_url,query_data)
        if len(resp) >= 0:
            actual = "pass"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)

    #转交测试
    @parameterized.expand(deliver_info)
    def test_deliver(self,deliver_url,deliver_data,expect):
        query_data = {"pageSize":"10","pageIndex":"1","cusInfo":"","workId":"","region":"","deptId":"","source":"","status":""}
        query_url = 'http://47.96.74.65:8080/WoniuBoss4.0/transmit/queryResourcesByInfo'
        old_query = len(DR_Action(self.session).do_query(query_url, query_data))
        resp = DR_Action(self.session).do_deliver(deliver_url,deliver_data)
        new_query = len(DR_Action(self.session).do_query(query_url, query_data))
        if resp == '' and old_query != new_query:
            actual = "pass"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        pass
