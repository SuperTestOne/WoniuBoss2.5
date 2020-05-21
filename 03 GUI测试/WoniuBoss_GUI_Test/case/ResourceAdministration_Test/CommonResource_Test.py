import unittest,time
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.ResourceAdministration.CommonResource_Action import CR_Action

class CR_Test(unittest.TestCase):
    # 获取查询数据
    query = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[4]
    query_info = Util.get_excel(query)
    # 获取认领数据
    claim = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[5]
    claim_info = Util.get_excel(claim)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        #获取绕过登录的信息
        login_ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Login.conf")[1]
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        Service.open_module_connect(self.driver,login_ele)
        self.ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf")

    #公共资源查询测试
    @parameterized.expand(query_info)
    def test_query_CR(self,*query_info):
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        time.sleep(2)
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_commonality_xpath"])
        #执行测试动作
        CR_Action(self.driver).do_query(query_info[:-1])
        #获取列表信息,并提取总数
        msg = Service.get_hint(self.driver, msg_xpath)
        if len(msg) >=1 :
            actual = "query_pass"
        else:
            actual = "query_fail"
        self.assertEqual(actual, query_info[-1])

    #公共资源认领测试
    @parameterized.expand(claim_info)
    def test_claim_CR(self,*claim_info):
        num_msg = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        #在培训资源模块中选择资源库
        Service.select_motion(self.driver, 'xpath', self.ele[7]["CR_resource_xpath"],"临时池")
        #获取咨询师名字
        name_msg = Service.get_hint(self.driver, '/html/body/div[1]').split('.')[-1].strip()
        #选择咨询师名字
        Service.select_motion(self.driver, 'xpath', self.ele[7]["CR_counselor_xpath"], name_msg)
        #查询
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_query_xpath"])
        #获取学员信息条数
        old_msg = Service.get_hint(self.driver,num_msg)
        #完成认领动作
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_commonality_xpath"])
        CR_Action(self.driver).do_claim()
        self.driver.refresh()
        #回到培训资源模块查询数据条数
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_administration_xpath"])
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_train_xpath"])
        Service.select_motion(self.driver, 'xpath', self.ele[7]["CR_resource_xpath"], "临时池")
        Service.select_motion(self.driver, 'xpath', self.ele[7]["CR_counselor_xpath"], name_msg)
        Service.click_motion(self.driver, 'xpath', self.ele[7]["CR_query_xpath"])
        new_msg = Service.get_hint(self.driver, num_msg)

        if old_msg != new_msg:
            actual = "claim_pass"
        else:
            actual = "claim_fail"

        print(actual)
        print(claim_info[-1])
        self.assertEqual(actual, claim_info[-1])

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass