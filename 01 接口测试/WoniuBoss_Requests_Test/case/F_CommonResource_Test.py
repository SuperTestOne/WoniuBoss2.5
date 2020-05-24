import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util
from WoniuBoss_Requests_Test.tools.service import Service
from WoniuBoss_Requests_Test.lib.F_CommonResource_Action import CR_Action

class CR_Test(unittest.TestCase):
    #获取查询数据
    query_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[0]
    query_info = Util.get_excel(query_contents)
    # 获取认领数据
    claim_contents = Util.get_json('..\\conf\\F_CR_Execl.conf')[1]
    claim_info = Util.get_excel(claim_contents)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.session = Service.get_session()

    #查询测试
    @parameterized.expand(query_info)
    def test_query(self,query_url,query_data,expect):
        resp = CR_Action(self.session).do_query(query_url,query_data)
        if len(resp) >= 0:
            actual = "pass"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)

    #认领测试
    @parameterized.expand(claim_info)
    def test_query(self, claim_url, claim_data, expect):
        resp = CR_Action(self.session).do_claim(claim_url, claim_data)
        self.assertEqual(int(resp), int(expect))

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        pass