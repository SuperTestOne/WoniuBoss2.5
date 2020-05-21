import unittest,time
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.ResourceAdministration.TrainingResource_Action import TR_Action

class TR_Test(unittest.TestCase):
    #获取新增数据
    add = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[0]
    add_info = Util.get_excel(add)
    #获取查询数据
    query = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[1]
    query_info = Util.get_excel(query)
    #获取跟踪数据
    tail = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[2]
    tail_info = Util.get_excel(tail)
    # 获取修改数据
    alter = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Excel.conf")[3]
    alter_info = Util.get_excel(alter)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Login.conf")[0]
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        Service.open_module_connect(self.driver,ele)
        self.ele = Util.get_json("..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf")

    #培训资源新增测试
    @parameterized.expand(add_info)
    def test_add_TR(self,*add_info):
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        #第一次默认查询，获取数据总条数
        Service.click_motion(self.driver,'xpath',self.ele[0]["TR_search_xpath"])
        old_msg = Service.get_hint(self.driver,msg_xpath)
        #完成新增
        TR_Action(self.driver).do_add(add_info[:-1])
        self.driver.refresh()
        #第二次默认查询，获取数据总条数
        Service.click_motion(self.driver,'xpath',self.ele[0]["TR_search_xpath"])
        new_msg = Service.get_hint(self.driver,msg_xpath)

        if old_msg != new_msg:
            actual = "add_pass"
        else:
            actual = "add_fail"
        self.assertEqual(actual, add_info[-1])

    #培训资源废弃测试
    def test_delete_TR(self):
        expect = "delete_pass"
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        # 第一次默认查询，获取数据总条数
        Service.click_motion(self.driver,'xpath',self.ele[0]["TR_search_xpath"])
        old_msg = Service.get_hint(self.driver, msg_xpath)
        #完成删除
        TR_Action(self.driver).do_delete()
        self.driver.refresh()
        # 第二次默认查询，获取数据总条数
        Service.click_motion(self.driver,'xpath',self.ele[0]["TR_search_xpath"])
        new_msg = Service.get_hint(self.driver, msg_xpath)

        if old_msg != new_msg:
            actual = "delete_pass"
        else:
            actual = "delete_fail"
        self.assertEqual(actual, expect)

    #培训资源查询测试
    @parameterized.expand(query_info)
    def test_query_TR(self,*query_info):
        msg_xpath = '//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]'
        #完成查询
        TR_Action(self.driver).do_query(query_info[:-1])
        #获取信息
        msg = Service.get_hint(self.driver,msg_xpath)
        #提取信息
        if len(msg) >= 1:
            actual = "query_pass"
        else:
            actual = "query_fail"
        self.assertEqual(actual, query_info[-1])

    #培训资源跟踪资源
    @parameterized.expand(tail_info)
    def test_tail_TR(self,*tail_info):
        #获取返回的电话
        phone = TR_Action(self.driver).do_tail(tail_info[:-1])
        self.driver.refresh()
        #输入电话并查询
        Service.input_motion(self.driver,"xpath",self.ele[3]["TR_condition_xpath"],phone)
        Service.click_motion(self.driver,'xpath', self.ele[0]["TR_search_xpath"])
        #获取查询出来的学员信息的状态
        time.sleep(1)
        status = self.driver.find_element_by_xpath('//*[@id="personal-table"]/tbody/tr[1]/td[5]').text
        if tail_info[1] == status:
            actual = "tail_pass"
        else:
            actual = "tail_fail"
        self.assertEqual(actual, tail_info[-1])

    #培训资源修改测试
    @parameterized.expand(alter_info)
    def test_alter_TR(self,*alter_info):
        print(alter_info)
        TR_Action(self.driver).do_alter(alter_info[:-1])
        self.driver.refresh()
        Service.input_motion(self.driver,"xpath","//*[@id='content']/div[2]/div/input[3]", alter_info[1])
        Service.click_motion(self.driver,"xpath","//*[@id='content']/div[2]/div/button")
        msg = Service.get_hint(self.driver,'//*[@id="content"]/div[3]/div/div[1]/div[2]/div[4]/div[1]/span[1]')
        if "总共 1 条记录" in msg:
            actual = "alter_pass"
        else:
            actual = "alter_fail"
        self.assertEqual(actual, alter_info[-1])

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass
