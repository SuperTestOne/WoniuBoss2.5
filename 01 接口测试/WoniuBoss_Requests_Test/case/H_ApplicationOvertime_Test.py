
import unittest, warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class AOA_Test(unittest.TestCase):
    #获取新增加班数据
    add_application = Util.get_json('..\\conf\\H_TM_Excel.conf')[8]
    application_info = Util.get_excel(add_application)
    print(application_info)


    #获取查询数据
    query_application = Util.get_json('..\\conf\\H_TM_Excel.conf')[9]
    query_application_info = Util.get_excel(query_application)
    # print(query_application_info)

    #获取课撤销数据
    alter_application = Util.get_json('..\\conf\\H_TM_Excel.conf')[10]
    alter_application_info = Util.get_excel(alter_application)
    # print(alter_application_info)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    # 新增加班测试
    @parameterized.expand(application_info)
    def test_add_application(self,application_url, application_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_ApplicationOvertime_Action import AOA_Action
        resps1 = AOA_Action(self.session).do_add_application(application_url, application_data)
        print(expect)
        print(resps1)
        if resps1 == "success":
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)
    # 查询测试
    @parameterized.expand(query_application_info)
    def test_query_application(self,query_application_url,query_application_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_ApplicationOvertime_Action import AOA_Action
        resps2 = AOA_Action(self.session).do_query_application(query_application_url,query_application_data)
        print(expect)
        if len(resps2) > 0:
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)


    # 撤销测试
    @parameterized.expand(alter_application_info)
    def test_alter_application(self,alter_application_url,alter_application_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_ApplicationOvertime_Action import AOA_Action
        resps3 = AOA_Action(self.session).do_alter_application(alter_application_url,alter_application_data)
        print(expect)
        if resps3 =='success':
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)

    def tearDown(self):
        self.session.close()


    @classmethod
    def tearDownClass(cls):
        pass
if __name__ == '__main__':
    unittest.main(verbosity=2)