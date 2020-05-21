import re
import time
import unittest

from parameterized import parameterized

from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class SL_Test(unittest.TestCase):

    # 新增info
    add_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[0]
    add_info = Util.get_excel_to_tuple(add_conf)
    # print(add_info)


    # 查询info
    query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[1]
    query_info = Util.get_excel_to_tuple(query_conf)
    # print(query_info)

    tow_query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[2]
    two_query_info = Util.get_excel_to_tuple(tow_query_conf)
    # print(two_query_info)


    # 修改info
    edit_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[3]
    edit_info = Util.get_excel_to_tuple(edit_conf)
    # print(edit_info)



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
                '//*[@id="list-31"]/div/ul/li[3]/a']
        Service.open_module_connect_zz(cls.driver, info)



    def tear(cls):
        pass

# ================================================================================================
    # 新增学员请假
    @parameterized.expand(add_info)
    def test_CSM_add(cls, leavetype, days, sname, points, contents, manage, expect):
        old_num = Service.get_hint\
            (cls.driver , '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')

        leavedata = {'leavetype': leavetype, 'days': days, 'sname':sname,
                          'points':points, 'contents':contents, 'manage':manage, 'expect': expect}
        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_add_leave(leavedata)

        new_num = Service.get_hint\
            (cls.driver , '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')


        old_add_number = re.findall(r'共(.*?)条', old_num)[0]
        old_add_code = old_add_number.strip()
        new_add_number = re.findall(r'共(.*?)条', new_num)[0]
        new_add_code = new_add_number.strip()


        # 断言
        if int(new_add_code) - int(old_add_code) == 1:
            add_actual = 'add_pass'
        elif int(new_add_code) - int(old_add_code) == 0:
            add_actual = 'add_fail'
        else:
            add_actual = 'other_error'


        # 断言测试是否通过
        cls.assertEqual(add_actual, leavedata['expect'])



# ================================================================================================

    # 查询学生请假
    @parameterized.expand(query_info)
    def test_CSM_query(cls, area, state, stuname, expect):

        leavequerydata = {'area': area, 'state': state, 'stuname':stuname, 'expect': expect}
        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_query_leavename(leavequerydata)

        old_query_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        new_query_num = re.findall(r'共(.*?)条', old_query_num)[0]
        new_num = new_query_num.strip()


        # 断言
        if new_num.isdigit():
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'


        # 断言测试是否通过
        cls.assertEqual(query_actual, leavequerydata['expect'])


# ================================================================================================

     # 查询学生请假
    @parameterized.expand(two_query_info)
    def test_CSM_query_tow(cls, area, state, stuname, expect):

        leavequerydata = {'area': area, 'state': state, 'stuname':stuname, 'expect': expect}
        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_query_leavename(leavequerydata)

        time.sleep(1)
        ele = cls.driver.find_element_by_xpath("//div[2]/table/tbody/tr/td")
        msg = ele.get_attribute('innerHTML')


        # 断言
        if "无符合条件" in msg:
            query_actual = 'query_fail'
        else:
            query_actual = 'query_pass'



        # 断言测试是否通过
        cls.assertEqual(query_actual, leavequerydata['expect'])



# ================================================================================================
    # 修改学员请假
    @parameterized.expand(edit_info)
    def test_CSM_edit(cls, editname , levtype, pointstype, managecontents, expect):
        old_content = cls.driver.find_element_by_xpath\
            ('//*[@id="leave-table"]/tbody/tr[3]/td[3]').text
        # print(old_content+"old")



        editleavedata = {'editname':editname, 'levtype': levtype, 'pointstype': pointstype, 'managecontents':managecontents,
                          'expect': expect}
        STU_Action(cls.driver).do_edit_leave(editleavedata)

        new_content = cls.driver.find_element_by_xpath('//*[@id="leave-table"]/tbody/tr[3]/td[3]').text
        # print(new_content+"new")

        # 断言
        if old_content not in new_content:
            edit_actual = 'edit_pass'
        else:
            edit_actual = 'edit_fail'



        # 断言测试是否通过
        cls.assertEqual(edit_actual, editleavedata['expect'])


# ================================================================================================

    # 销假
    def test_click_delete_leave(self):
        STU_Action(self.driver).click_delete_leave()

        text_content = self.driver.find_element_by_xpath \
            ('//*[@id="leave-table"]/tbody/tr[1]/td[10]').text


        # 断言
        if "已销假" in text_content:
            delete_lev_actual = 'pass'
        else:
            delete_lev_actual = 'fail'

# ================================================================================================





if __name__ == '__main__':
    unittest.main()