import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.ResourceAdministration.DeliverResource_Action import DR_Action

class DR_Test(unittest.TestCase):
    # 获取查询数据
    query = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[6]
    query_info = Util.get_excel(query)
    # 获取转交数据
    deliver = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[7]
    deliver_info = Util.get_excel(deliver)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        # 获取绕过登录的信息
        login_ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Login.conf")[2]
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        Service.open_module_connect(self.driver, login_ele)
        self.ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf")

    #转交资源认领测试
    @parameterized.expand(query_info)
    def test_query_DR(self,*query_info):
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        # 执行测试动作
        DR_Action(self.driver).do_query(query_info[:-1])
        # 获取列表信息,并提取总数
        msg = Service.get_hint(self.driver, msg_xpath)
        if len(msg) >= 1:
            actual = "query_pass"
        else:
            actual = "query_fail"
        self.assertEqual(actual, query_info[-1])

    #转交资源转交测试
    @parameterized.expand(deliver_info)
    def test_deliver_DR(self, *deliver_info):
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        Service.click_motion(self.driver, 'xpath', self.ele[8]["DR_query_xpath"])
        old_msg = Service.get_hint(self.driver, msg_xpath)
        DR_Action(self.driver).do_deliver(deliver_info[:-1])
        self.driver.refresh()
        Service.click_motion(self.driver, 'xpath', self.ele[8]["DR_query_xpath"])
        new_msg = Service.get_hint(self.driver, msg_xpath)

        if old_msg != new_msg:
            actual = "deliver_pass"
        else:
            actual = "deliver_fail"
        self.assertEqual(actual, deliver_info[-1])

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass