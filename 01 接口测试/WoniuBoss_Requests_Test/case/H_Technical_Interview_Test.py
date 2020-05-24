import unittest, warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class TI_Test(unittest.TestCase):
    #获取搜索数据
    search_contents = Util.get_json('..\\conf\\H_TM_Excel.conf')[3]
    search_course_info = Util.get_excel(search_contents)
    print(search_course_info)

    #获取面试询数据
    alter_contents = Util.get_json('..\\conf\\H_TM_Excel.conf')[4]
    alter_course_info = Util.get_excel(alter_contents)
    print(alter_course_info)


    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    # 搜索测试
    @parameterized.expand(search_course_info)
    def test_query_course(self,query_interview_url,query_interview_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_Technical_Interview_Action import TI_Action
        resp = TI_Action(self.session).do_query_interview(query_interview_url,query_interview_data)
        print(expect)
        print(resp)
        if len(resp) > 0:
            actual = "pass"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)
    # 面试测试
    @parameterized.expand(alter_course_info)
    def test_interview_course(self,alter_interview_url,alter_interview_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_Technical_Interview_Action import TI_Action
        resp4 = TI_Action(self.session).do_add_interview(alter_interview_url,alter_interview_data)
        print(expect)
        if resp4 == 'success':
            actual = 'success'
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