import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.TeachingManagement.Technica import Tech

class T_Test(unittest.TestCase):
    # 获取搜索数据
    sous = Util.get_json('..\\..\\conf\\TeachingManagement_Conf\\testinfo.conf')[1]
    sous_info = Util.get_excel(sous)

    # 获取面试数据
    interview = Util.get_json('..\\..\\conf\\TeachingManagement_Conf\\testinfo.conf')[2]
    interview_info = Util.get_excel(interview)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD000','woniu123','woniu123','//*[@id="nav2"]/div[7]/div[1]/a','//*[@id="list-11"]/div/ul/li[2]/a']
        Service.open_module_connect_zz(self.driver,info)

    #搜索功能测试
    @parameterized.expand(sous_info)
    def test_search(self,*sous_info):#*不定长参数
        Tech(self.driver).do_search(sous_info[:-1])
        Tech(self.driver).click_search_button()
        msg = Service.get_hint(self.driver,"/html/body/div[8]/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        if len(msg) >= 1:
            actual = "search_pass"
        else:
            actual = "search_fail"
        self.assertEqual(actual,sous_info[-1])

    #面试测试
    @parameterized.expand(interview_info)
    def test_interview(self,*interview_info):
        Tech(self.driver).do_interview(interview_info[:-1])
        msg = Service.get_hint(self.driver,'/html/body/div[10]/div/div/div[2]/div')
        if "保存成功" in msg:
            actual = "interview_pass"
        else:
            actual = "interview_fail"

        self.assertEqual(actual,interview_info[-1])

    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    test_search()