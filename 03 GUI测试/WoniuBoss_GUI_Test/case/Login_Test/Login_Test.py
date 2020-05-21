import unittest,sys
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.Login.Login_Action import L_Action

class L_Test(unittest.TestCase):
    login = Util.get_json('..\\..\\conf\\Login_Conf\\L_Excel.conf')[0]
    login_info = Util.get_excel(login)

    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)

    @parameterized.expand(login_info)
    def test_login(self,username,userpass,expect):
        L_Action(self.driver).do_login(username,userpass)
        if Service.is_element_present(self.driver,"xpath","/html/body/div[2]/div[2]/ul/li[2]/a"):
            actual = "login_pass"
        else:
            actual = "login_fail"
        self.assertEqual(actual, expect)

    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass

