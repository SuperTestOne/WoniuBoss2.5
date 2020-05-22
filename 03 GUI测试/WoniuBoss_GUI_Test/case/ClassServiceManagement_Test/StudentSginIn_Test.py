import unittest,time
from parameterized import parameterized
from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentSginIn_Action import SSI_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class SSI_Test(unittest.TestCase):

    query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SSI_Excel.conf')[0]
    query_info = Util.get_excel(query_conf)


    two_query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SSI_Excel.conf')[1]
    two_query_info = Util.get_excel(two_query_conf)


    Sgin_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SSI_Excel.conf')[2]
    Sgin_info = Util.get_excel(Sgin_conf)


    Return_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SSI_Excel.conf')[3]
    Return_info = Util.get_excel(Return_conf)


    Bactch_ssi_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SSI_Excel.conf')[4]
    Bactch_ssi_info = Util.get_excel(Bactch_ssi_conf)



    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[2]/a']
        Service.open_module_connect_zz(self.driver, info)

    def tearDown(self):
        self.driver.close()


    @parameterized.expand(query_info)
    def test_SSI_query(cls, ssiname, expect):

        ssiquerydata = {'ssiname': ssiname, 'expect': expect}
        SSI_Action(cls.driver).do_query(ssiquerydata)

        time.sleep(1)
        text_contents = cls.driver.find_element_by_xpath('//*[@id="stu-table"]/tbody/tr/td[2]').text

        if text_contents == "WNCD202005007":
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        cls.assertEqual(query_actual, ssiquerydata['expect'])


    @parameterized.expand(two_query_info)
    def test_SSI_query_tow(cls, ssiname, expect):

        ssiquerydata_two = {'ssiname': ssiname, 'expect': expect}
        SSI_Action(cls.driver).do_query(ssiquerydata_two)

        time.sleep(1)
        ele = cls.driver.find_element_by_xpath('//*[@id="stu-table"]/tbody/tr/td')
        msg = ele.get_attribute('innerHTML')

        if "无符合" in msg:
            query_actual = 'query_fail'
        else:
            query_actual = 'query_pass'

        cls.assertEqual(query_actual, ssiquerydata_two['expect'])


    @parameterized.expand(Sgin_info)
    def test_SSI(cls, ssicontents, expect):
        SSI_Action(cls.driver).click_SSI_class()

        ssistetedata = {'ssicontents': ssicontents, 'expect': expect}
        SSI_Action(cls.driver).do_ssi(ssistetedata)

        time.sleep(1)
        text_content = cls.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[3]/td[6]').text

        # 断言
        if "正常" in text_content or "请假" in text_content:
            SginIn_actual = 'Sgin_pass'
        else:
            SginIn_actual = 'Sgin_fail'

        cls.assertEqual(SginIn_actual, ssistetedata['expect'])


    @parameterized.expand(Return_info)
    def test_SSI_Return(cls, ssiname, expect):

        SSI_Action(cls.driver).click_SSI_class()

        old_text = cls.driver.find_element_by_xpath\
            ('//*[@id="panel-element-236"]/div/div[1]/div[2]/div[4]/div[1]/span[1]').text

        rnssidata = {'ssiname': ssiname, 'expect': expect}
        SSI_Action(cls.driver).do_Return(rnssidata)

        time.sleep(1)
        new_text = cls.driver.find_element_by_xpath\
            ('//*[@id="panel-element-236"]/div/div[1]/div[2]/div[4]/div[1]/span[1]').text

        if old_text == new_text:
            Return_actual = 'Return_pass'
        else:
            Return_actual = 'Return_fail'

        cls.assertEqual(Return_actual, rnssidata['expect'])


    @parameterized.expand(Bactch_ssi_info)
    def test_SSI_Bactch(cls, ssicontents_one, ssicontents_two, ssicontents_three, expect):

        SSI_Action(cls.driver).click_SSI_class()

        Bactchdata = {'ssicontents_one': ssicontents_one, 'ssicontents_two': ssicontents_two,
                      'ssicontents_three': ssicontents_three, 'expect': expect}
        SSI_Action(cls.driver).do_Bactch_ssi(Bactchdata)

        time.sleep(1)
        text_content_one = cls.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[2]/td[6]').text
        print(text_content_one)

        text_content_two = cls.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[4]/td[6]').text
        print(text_content_two)

        text_content_three = cls.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[5]/td[6]').text
        print(text_content_three)

        if ("正常" in text_content_one) and ("正常" in text_content_two) and ("正常" in text_content_three):
            Bactch_ssi_actual = 'Bactch_ssi_pass'
        else:
            Bactch_ssi_actual = 'Bactch_ssi_fail'

        cls.assertEqual(Bactch_ssi_actual, Bactchdata['expect'])

