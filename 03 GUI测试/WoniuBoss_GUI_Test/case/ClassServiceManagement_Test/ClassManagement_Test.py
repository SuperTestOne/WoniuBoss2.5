import unittest,re
from parameterized import parameterized
from WoniuBoss_GUI_Test.lib.ClassServiceManagement.ClassManagement_Action import CSM_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class CM_Test(unittest.TestCase):

    add_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\CSM_Excel.conf')[0]
    add_info = Util.get_excel(add_conf)

    query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\CSM_Excel.conf')[1]
    query_info = Util.get_excel(query_conf)


    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '/html/body/div[4]/div[2]/div[8]/div[2]/div/ul/li[1]/a']
        Service.open_module_connect_zz(self.driver, info)

    def tearDown(self):
        self.driver.close()


    @parameterized.expand(add_info)
    def test_CSM_add(cls, classnumber, public, tnumber, expect):
        old_text = cls.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text

        addclass_data = {'classnumber': classnumber, 'public': public,
                         'tnumber':tnumber, 'expect': expect}
        CSM_Action(cls.driver).CSM_add(addclass_data)

        new_text = cls.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text

        if old_text != new_text:
            add_actual = 'add_pass'
        else:
            add_actual = 'add_fail'

        cls.assertEqual(add_actual, addclass_data['expect'])


    @parameterized.expand(query_info)
    def test_CSM_query(cls, sclname, all, expect):

        queryclassdata = {'sclname': sclname, 'all': all, 'expect': expect}
        CSM_Action(cls.driver).CSM_query(queryclassdata)

        old_query_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')

        old_query_number = re.findall(r'共(.*?)条', old_query_num)[0]
        new_num = old_query_number.strip()

        if new_num.isdigit():
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        cls.assertEqual(query_actual, queryclassdata['expect'])
