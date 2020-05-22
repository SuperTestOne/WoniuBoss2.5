import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.Technicalinterview.Technica import Tech

class T_Test(unittest.TestCase):
    # 获取搜索数据
    puth1 = Util.get_file_path()
    sous = Util.get_json(f'{puth1}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[1]
    # print(sous)
    sous_info = Util.get_excel(sous)

    # 获取面试数据
    puth2 = Util.get_file_path()
    inter = Util.get_json(f'{puth2}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[2]
    inter_info = Util.get_excel(inter)


    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD000','woniu123','/html/body/div[4]/div[2]/div[7]/div[1]/a','/html/body/div[4]/div[2]/div[7]/div[2]/div/ul/li[2]/a']
        Service.open_module_connect(self.driver,info)

    @parameterized.expand(sous_info)
    def test_search(self,*sous_info):#*不定长参数
        Tech(self.driver).do_search(sous_info[:-1])
        Tech(self.driver).click_search_button()
        msg = Service.get_hint(self.driver,"/html/body/div[8]/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        num = int(re.findall(r'共(.*?)条',msg)[0])
        self.assertEqual(num,int(sous_info[-1]))

    @parameterized.expand(inter_info)
    def test_inter(self,*inter_info):
        Tech(self.driver).do_inter(inter_info[:-1])

        msg3 = Tech(self.driver).get_msg()
        if '保存成功' in msg3:
            actual = "search_pass"
        else:
            actual = "search_fail"
        self.assertEqual(actual,inter_info[:-1])



    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)