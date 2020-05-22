import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.lib.Technicalinterview.course import Cour
class C_Test(unittest.TestCase):
    # 获取排课数据
    puth3 = Util.get_file_path()
    couk = Util.get_json(f'{puth3}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[3]
    # print(couk)
    cour_info = Util.get_excel(couk)

    # 获取查询数据
    puths = Util.get_file_path()
    query = Util.get_json(f'{puths}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[4]
    que_info = Util.get_excel(query)

    # 获取修改数据
    puths1 = Util.get_file_path()
    alters = Util.get_json(f'{puths1}\\WoniuBoss_GUI_Test\\conf\\testinfo.conf')[5]
    alt_info = Util.get_excel(alters)


    @classmethod
    def setUpClass(cls):
        pass

    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD000','woniu123','/html/body/div[4]/div[2]/div[7]/div[1]/a','/html/body/div[4]/div[2]/div[7]/div[2]/div/ul/li[1]/a']
        Service.open_module_connect(self.driver,info)

    @parameterized.expand(cour_info)
    def test_cour(self,*cour_info):#*不定长参数
        Cour(self.driver).do_course(cour_info[:-1])
        msg1 = Cour(self.driver).get_msg()
        if '排课成功' in msg1:
            actual = "cour_pass"
        else:
            actual = "cour_fail"
        self.assertEqual(actual,cour_info[:-1])


    @parameterized.expand(que_info)
    def test_que(self,*que_info):#*不定长参数
        Cour(self.driver).do_query(que_info[:-1])
        Cour(self.driver).click_query_button()
        msg1 = Service.get_hint(self.driver,"/html/body/div[8]/div[2]/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        num = int(re.findall(r'共(.*?)条',msg1)[0])
        self.assertEqual(num,int(que_info[-1]))


    # @parameterized.expand(alt_info)
    # def test_alt(self,*alt_info):#*不定长参数
    #     Cour(self.driver).do_alter(alt_info[:-1])
    #     self.driver.refresh()
    #     msg5 = Service.get_hint(self.driver,"/html/body/div[8]/div[2]/div/div[2]/div[2]/div[2]/table/tbody/tr[1]/td[1]")
    #     self.assertEqual(msg5,int(alt_info[-1]))

        # if num2 != num3:
        #     acutal = 'alter_pass'
        # else:
        #     acutal = 'alter-fail'


        # self.assertEqual(acutal,alt_info[:-1])



    def tearDown(self):
        self.driver.close()

    @classmethod
    def tearDownClass(cls):
        pass

if __name__ == '__main__':
    unittest.main(verbosity=2)