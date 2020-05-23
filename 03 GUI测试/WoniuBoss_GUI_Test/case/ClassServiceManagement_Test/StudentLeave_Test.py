import unittest,re,time
from parameterized import parameterized
from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util


class SL_Test(unittest.TestCase):

    add_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[0]
    add_info = Util.get_excel(add_conf)

    query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[1]
    query_info = Util.get_excel(query_conf)

    tow_query_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[2]
    two_query_info = Util.get_excel(tow_query_conf)

    edit_conf = Util.get_json(r'..\..\conf\ClassServiceManagement_Conf\SL_Excel.conf')[3]
    edit_info = Util.get_excel(edit_conf)
    print(edit_info)


    def setUp(self):
        self.driver = Service.get_driver()
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[3]/a']
        Service.open_module_connect_zz(self.driver, info)

    def tearDown(self):
        self.driver.close()


    @parameterized.expand(add_info)
    def test_CSM_add(cls, leavetype, days, sname, points, contents, manage, expect):
        old_text = cls.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text

        leavedata = {'leavetype': leavetype, 'days': days, 'sname':sname,
                          'points':points, 'contents':contents, 'manage':manage, 'expect': expect}
        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_add_leave(leavedata)

        new_text = cls.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]').text

        if old_text != new_text:
            add_actual = 'add_pass'
        elif old_text == new_text:
            add_actual = 'add_fail'
        else:
            add_actual = 'other_error'

        cls.assertEqual(add_actual, leavedata['expect'])


    @parameterized.expand(query_info)
    def test_CSM_query(cls, area, state, stuname, expect):

        leavequerydata = {'area': area, 'state': state, 'stuname':stuname, 'expect': expect}

        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_query_leavename(leavequerydata)

        old_query_num = Service.get_hint \
            (cls.driver, '//*[@id="content"]/div[2]/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]')
        new_query_num = re.findall(r'共(.*?)条', old_query_num)[0]
        new_num = new_query_num.strip()

        if new_num.isdigit():
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        cls.assertEqual(query_actual, leavequerydata['expect'])


    @parameterized.expand(two_query_info)
    def test_CSM_query_tow(cls, area, state, stuname, expect):

        leavequerydata = {'area': area, 'state': state, 'stuname':stuname, 'expect': expect}

        from WoniuBoss_GUI_Test.lib.ClassServiceManagement.StudentLeave_Action import STU_Action
        STU_Action(cls.driver).do_query_leavename(leavequerydata)

        time.sleep(1)
        ele = cls.driver.find_element_by_xpath("//div[2]/table/tbody/tr/td")
        msg = ele.get_attribute('innerHTML')

        if "无符合条件" in msg:
            query_actual = 'query_fail'
        else:
            query_actual = 'query_pass'

        cls.assertEqual(query_actual, leavequerydata['expect'])


    @parameterized.expand(edit_info)
    def test_CSM_edit(cls, editname , levtype, pointstype, managecontents, expect):
        old_content = cls.driver.find_element_by_xpath\
            ('//*[@id="leave-table"]/tbody/tr[1]/td[3]').text
        print(old_content)

        editleavedata = {'editname':editname, 'levtype': levtype, 'pointstype': pointstype, 'managecontents':managecontents,
                          'expect': expect}

        STU_Action(cls.driver).do_edit_leave(editleavedata)

        new_content = cls.driver.find_element_by_xpath('//*[@id="leave-table"]/tbody/tr[1]/td[3]').text
        print(new_content)

        if old_content not in new_content:
            edit_actual = 'edit_pass'
        else:
            edit_actual = 'edit_fail'


        cls.assertEqual(edit_actual, editleavedata['expect'])


    def test_click_delete_leave(self):
        STU_Action(self.driver).click_delete_leave()

        text_content = self.driver.find_element_by_xpath \
            ('//*[@id="leave-table"]/tbody/tr[1]/td[10]').text

        if "已销假" in text_content:
            delete_lev_actual = 'pass'
        else:
            delete_lev_actual = 'fail'

