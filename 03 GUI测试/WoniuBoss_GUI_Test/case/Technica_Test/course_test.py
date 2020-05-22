import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.TeachingManagement.Course_Aaction import C_Action
class C_Test(unittest.TestCase):
    # 获取排课数据
    couk = Util.get_json('..\\..\\conf\\TeachingManagement_Conf\\testinfo.conf')[3]
    cour_info = Util.get_excel(couk)

    # 获取查询数据TeachingManagement
    query = Util.get_json('..\\..\\conf\\TeachingManagement_Conf\\testinfo.conf')[4]
    query_info = Util.get_excel(query)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD000','woniu123','woniu123','//*[@id="nav2"]/div[7]/div[1]/a','//*[@id="list-11"]/div/ul/li[1]/a']
        Service.open_module_connect_zz(self.driver,info)

    #排课测试
    @parameterized.expand(cour_info)
    def test_course(self,*cour_info):#*不定长参数
        C_Action(self.driver).do_course(cour_info[:-1])
        msg1 = Service.get_hint(self.driver,'/html/body/div[16]/div/div/div[2]/div')
        if '排课成功' in msg1:
            actual = "cour_pass"
        else:
            actual = "cour_fail"
        self.assertEqual(actual,cour_info[-1])

    #查询测试
    @parameterized.expand(query_info)
    def test_query(self,*query_info):#*不定长参数
        C_Action(self.driver).do_query(query_info[:-1])
        #C_Action(self.driver).click_query_button()
        msg  = Service.get_hint(self.driver,'//*[@id="course"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        if len(msg) >=1:
            actual = "query_pass"
        else:
            actual = "query_fail"
        self.assertEqual(actual,query_info[-1])

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    test_course()