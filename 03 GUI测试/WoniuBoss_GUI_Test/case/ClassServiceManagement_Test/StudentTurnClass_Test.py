import unittest,time
from parameterized import parameterized
from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentTurnClass_Action import STC_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class STC_Test(unittest.TestCase):


    query_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[0]
    query_info = Util.get_excel(query_conf)


    two_query_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[1]
    two_query_info = Util.get_excel(two_query_conf)


    TurnClass_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[2]
    TurnClass_info = Util.get_excel(TurnClass_conf)


    def setUp(cls):
        cls.driver = Service.get_driver()
        Service.open_page(cls.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[4]/a']
        Service.open_module_connect_zz(cls.driver, info)

    def tearDown(self):
        self.driver.close()


    @parameterized.expand(query_info)
    def test_SSI_query(cls, stcarea, stcstate, stcname, expect):
        time.sleep(1)
        old_text = cls.driver.find_element_by_xpath\
            ('//*[@id="stuInfo"]/div[2]/div[2]/div[4]/div[1]/span[1]').text

        stcquerydata = {'stcarea': stcarea, 'stcstate': stcstate,
                        'stcname': stcname, 'expect': expect}
        STC_Action(cls.driver).do_query(stcquerydata)

        time.sleep(1)
        new_text = cls.driver.find_element_by_xpath\
            ('//*[@id="stuInfo"]/div[2]/div[2]/div[4]/div[1]/span[1]').text

        if old_text != new_text:
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        cls.assertEqual(query_actual, stcquerydata['expect'])


    @parameterized.expand(two_query_info)
    def test_SSI_query_tow(cls, stcarea, stcstate, stcname, expect):

        stcquerydata_two = {'stcarea': stcarea, 'stcstate': stcstate,
                        'stcname': stcname, 'expect': expect}
        STC_Action(cls.driver).do_query(stcquerydata_two)

        time.sleep(1)
        ele = cls.driver.find_element_by_xpath('//*[@id="stuInfo_table"]/tbody/tr/td')
        msg = ele.get_attribute('innerHTML')

        if "无符合" in msg:
            query_actual = 'query_fail'
        else:
            query_actual = 'query_pass'

        cls.assertEqual(query_actual, stcquerydata_two['expect'])


    @parameterized.expand(TurnClass_info)
    def test_STC_turnclass(cls , stcschool , stcclass , expect):

        turnclassdata = {'stcschool': stcschool, 'stcclass': stcclass, 'expect': expect}
        STC_Action(cls.driver).do_turnschool(turnclassdata)

        time.sleep(1)
        cls.driver.refresh()
        time.sleep(1)
        STC_Action(cls.driver).click_mould()
        text_contents = cls.driver.find_element_by_xpath\
            ('//*[@id="stuInfo_table"]/tbody/tr[3]/td[4]').text

        if text_contents == "WNCDC33":
            actual = 'TurnClass_pass'
        else:
            actual = 'TurnClass_fail'

        cls.assertEqual(actual, turnclassdata['expect'])
