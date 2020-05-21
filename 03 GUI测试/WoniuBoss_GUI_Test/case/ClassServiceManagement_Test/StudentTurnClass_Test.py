import re
import time
import unittest

from parameterized import parameterized

from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentTurnClass_Action import STC_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class STC_Test(unittest.TestCase):

    # 查询info
    query_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[0]
    query_info = Util.get_excel_to_tuple(query_conf)
    # print(query_info)


    # 查询info
    two_query_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[1]
    two_query_info = Util.get_excel_to_tuple(two_query_conf)
    # print(two_query_info)



    # 考勤info
    TurnClass_conf = Util.get_json(r'..\..\conf\\ClassServiceManagement_Conf\STC_Excel.conf')[2]
    TurnClass_info = Util.get_excel_to_tuple(TurnClass_conf)
    # print(TurnClass_info)




# ================================================================================================

    @classmethod
    def setUpClass(cls):
        pass


    # 收尾工作
    @classmethod
    def tearDownClass(cls):
        cls.driver = Service.get_driver_zz()
        cls.driver.close()


    def setUp(cls):
        cls.driver = Service.get_driver_zz()
        Service.open_page_zz(cls.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[4]/a']
        Service.open_module_connect_zz(cls.driver, info)



    def tear(cls):
        pass

# ================================================================================================

    # 查询
    @parameterized.expand(query_info)
    def test_SSI_query(cls, stcarea, stcstate, stcname, expect):
        time.sleep(1)
        old_query_num = Service.get_hint \
            (cls.driver, '//*[@id="stuInfo"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        old_query_code = re.findall(r'共(.*?)条', old_query_num)[0]
        old_num = old_query_code.strip()

        stcquerydata = {'stcarea': stcarea, 'stcstate': stcstate,
                        'stcname': stcname, 'expect': expect}
        STC_Action(cls.driver).do_query(stcquerydata)

        time.sleep(1)
        new_query_num = Service.get_hint \
            (cls.driver, '//*[@id="stuInfo"]/div[2]/div[2]/div[4]/div[1]/span[1]')
        new_query_code = re.findall(r'共(.*?)条', new_query_num)[0]
        new_num = new_query_code.strip()

        # 断言
        if old_num != new_num:
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        # 断言测试是否通过
        cls.assertEqual(query_actual, stcquerydata['expect'])


# ================================================================================================

    # 查询
    @parameterized.expand(two_query_info)
    def test_SSI_query_tow(cls, stcarea, stcstate, stcname, expect):

        stcquerydata_two = {'stcarea': stcarea, 'stcstate': stcstate,
                        'stcname': stcname, 'expect': expect}
        STC_Action(cls.driver).do_query(stcquerydata_two)

        time.sleep(1)
        ele = cls.driver.find_element_by_xpath('//*[@id="stuInfo_table"]/tbody/tr/td')
        msg = ele.get_attribute('innerHTML')

        # 断言
        if "无符合" in msg:
            query_actual = 'query_fail'
        else:
            query_actual = 'query_pass'

        # 断言测试是否通过
        cls.assertEqual(query_actual, stcquerydata_two['expect'])

# ================================================================================================

    # 转班
    @parameterized.expand(TurnClass_info)
    def test_STC_turnclass(cls , stcschool , stcclass , expect):

        turnclassdata = {'stcschool': stcschool, 'stcclass': stcclass, 'expect': expect}
        STC_Action(cls.driver).do_turnschool(turnclassdata)

        # 刷新页面
        time.sleep(1)
        cls.driver.refresh()
        time.sleep(1)
        STC_Action(cls.driver).click_mould()
        text_contents = cls.driver.find_element_by_xpath\
            ('//*[@id="stuInfo_table"]/tbody/tr[3]/td[4]').text

        # 断言
        if text_contents == "WNCDC33":
            actual = 'TurnClass_pass'
        else:
            actual = 'TurnClass_fail'

        # 断言测试是否通过
        cls.assertEqual(actual, turnclassdata['expect'])


# ================================================================================================


if __name__ == '__main__':
    unittest.main()