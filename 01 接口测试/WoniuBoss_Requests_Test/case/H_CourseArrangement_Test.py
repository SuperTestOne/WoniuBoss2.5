
import unittest, warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.tools.util import Util

class CA_Test(unittest.TestCase):
    #获取新增排课数据
    contents = Util.get_json('..\\conf\\H_TM_Excel.conf')[0]
    course_info = Util.get_excel(contents)
    print(course_info)

    #获取课程安排查询数据
    query_contents = Util.get_json('..\\conf\\H_TM_Excel.conf')[1]
    query_course_info = Util.get_excel(query_contents)
    print(query_course_info)

    #获取课程安排查询数据
    alter_contents = Util.get_json('..\\conf\\H_TM_Excel.conf')[2]
    alter_course_info = Util.get_excel(alter_contents)
    print(alter_course_info)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.session = Service.get_session()

    # 新增排课测试
    @parameterized.expand(course_info)
    def test_add_course(self,course_url,course_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_CourseArrangement_Action import CA_Action
        resp1 = CA_Action(self.session).do_add_course(course_url, course_data)
        # print(expect)
        # print(resp1)
        if resp1 == "success":
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)
    # 查询排课测试
    @parameterized.expand(query_course_info)
    def test_query_course(self,query_course_url, query_course_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_CourseArrangement_Action import CA_Action
        resp2 = CA_Action(self.session).do_query_course(query_course_url,query_course_data)
        print(expect)
        if len(resp2) > 0:
            actual = "success"
        else:
            actual = "fail"
        self.assertEqual(actual, expect)


    # 修改排课测试
    @parameterized.expand(alter_course_info)
    def test_alter_course(self,alter_course_url,alter_course_data,expect):
        warnings.simplefilter('ignore', ResourceWarning)
        from WoniuBoss_Requests_Test.lib.H_CourseArrangement_Action import CA_Action
        resp3 = CA_Action(self.session).do_alter_course(alter_course_url,alter_course_data)
        print(expect)
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