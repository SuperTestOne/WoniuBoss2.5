import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.Technicalinterview.duty import Duty
class D_Test(unittest.TestCase):
    # 获取排课数据
    puth6 = Util.get_file_path()
    sp1 = Util.get_json(f'{puth6}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[6]
    specti_info = Util.get_excel(sp1)

    @classmethod
    def setUpClass(cls):
        pass


    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD000','woniu123','/html/body/div[4]/div[2]/div[7]/div[1]/a','/html/body/div[4]/div[2]/div[7]/div[2]/div/ul/li[3]/a']
        Service.open_module_connect(self.driver,info)

    @parameterized.expand(specti_info)
    def test_cour(self,*specti_info):#*不定长参数
        Duty(self.driver).do_specti(specti_info[:-1])
        msg2 = Duty(self.driver).get_msg()
        if '新增值班成功' in msg2:
            actual = "duty_pass"
        else:
            actual = "duty_fail"
        self.assertEqual(actual,specti_info[:-1])