
import unittest, warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class TD_Test(unittest.TestCase):
    #获取指定值班数据
    duty = Util.get_json('..\\conf\\H_TM_Excel.conf')[5]
    duty_info = Util.get_excel(duty)
    print(duty_info)

    #获取课程安排查询数据
    query_duty = Util.get_json('..\\conf\\H_TM_Excel.conf')[6]
    query_duty_info = Util.get_excel(query_duty)
    # print(query_duty_info)

    #获取课程安排查询数据
    alter_duty = Util.get_json('..\\conf\\H_TM_Excel.conf')[7]
    alter_duty_info = Util.get_excel(alter_duty)
    # print(alter_duty_info)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    # 指定值班测试
    @parameterized.expand(duty_info)
    def test_add_duty(self,duty_url,duty_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_TeacherDuty_Action import TD_Action
        resp = TD_Action(self.session).do_add_duty(duty_url,duty_data)
        # print(expect)

        if isinstance(resp , str):
            actual = "success"
        else:
            actual = "fail"

        self.assertEqual(actual, expect)
    # 查询值班测试
    @parameterized.expand(query_duty_info)
    def test_query_duty(self,query_duty_url,query_duty_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_TeacherDuty_Action import TD_Action
        resp6 = TD_Action(self.session).do_query_duty(query_duty_url,query_duty_data)
        # print(expect)
        if len(resp6) > 0:
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)


    # 修改排课测试
    @parameterized.expand(alter_duty_info)
    def test_alter_duty(self,alter_duty_url,alter_duty_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_TeacherDuty_Action import TD_Action
        resp3 = TD_Action(self.session).do_alter_duty(alter_duty_url,alter_duty_data)
        # print(expect)
        if resp3 =='success':
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