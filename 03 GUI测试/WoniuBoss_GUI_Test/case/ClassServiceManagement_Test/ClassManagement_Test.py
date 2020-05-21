import re
import time
import unittest

from parameterized import parameterized

from WoniuBoss_GUI_Test.lib.ClassServiceManagement.ClassManagement_Action import CSM_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util



class CM_Test(unittest.TestCase):

    # 新增info
    add_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\CSM_Excel.conf')[0]
    add_info = Util.get_excel_to_tuple(add_conf)
    # print(add_info)

    # 查询info
    query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\CSM_Excel.conf')[1]
    query_info = Util.get_excel_to_tuple(query_conf)
    # print(query_info)



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
                '/html/body/div[4]/div[2]/div[8]/div[2]/div/ul/li[1]/a']
        Service.open_module_connect_zz(cls.driver, info)


    def tear(cls):
        pass

# ================================================================================================

    # 通过参数化装饰器传入参数
    # 支持传参的方式[(),(),()]
    @parameterized.expand(add_info)
    def test_CSM_add(cls, classnumber, public, tnumber, expect):
        # 先获取页面数据个数
        old_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')

        addclass_data = {'classnumber': classnumber, 'public': public,
                         'tnumber':tnumber, 'expect': expect}
        CSM_Action(cls.driver).CSM_add(addclass_data)

        new_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')

        old_add_number = re.findall(r'共(.*?)条', old_num)[0]
        old_add_code = old_add_number.strip()
        new_add_number = re.findall(r'共(.*?)条', new_num)[0]
        new_add_code = new_add_number.strip()


        # 断言
        if int(new_add_code) - int(old_add_code) == 1:
            add_actual = 'add_pass'
        else:
            add_actual = 'add_fail'


        # 断言测试是否通过
        cls.assertEqual(add_actual, addclass_data['expect'])

# ================================================================================================
    # 班级管理查询
    @parameterized.expand(query_info)
    def test_CSM_query(cls, sclname, all, expect):

        queryclassdata = {'sclname': sclname, 'all': all, 'expect': expect}
        CSM_Action(cls.driver).CSM_query(queryclassdata)

        old_query_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')

        old_query_number = re.findall(r'共(.*?)条', old_query_num)[0]
        new_num = old_query_number.strip()


        # 断言
        if new_num.isdigit():
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'


        # 断言测试是否通过
        cls.assertEqual(query_actual, queryclassdata['expect'])

# ================================================================================================


if __name__ == '__main__':
    unittest.main()