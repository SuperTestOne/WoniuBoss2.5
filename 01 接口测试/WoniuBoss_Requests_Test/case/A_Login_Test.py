import unittest
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class L_Test(unittest.TestCase):
    #获取登录数据
    contents = Util.get_json('..\\conf\\A_L_Excel.conf')[0]
    login_info = Util.get_excel(contents)
    print(login_info)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    #登录测试
    @parameterized.expand(login_info)
    def test_login(self,login_url,login_data,expect):
        from WoniuBoss_Requests_Test.lib.A_Login_Action import L_Action
        resp = L_Action(self.session).do_login(login_url,login_data)
        print(expect)
        print(resp)
        if resp == "":
            resp = "error"
        self.assertEqual(resp, expect)

    def tearDown(self):
        self.session.close()

    @classmethod
    def tearDownClass(cls):
        pass
if __name__ == '__main__':
    unittest.main()
