# encoding: utf-8
# @author: yinqianjun
# @file: StudentManage_Test.py
# @time: 2020/5/19 14:36

import unittest,re
from WoniuBoss_GUI_Test.lib.StudentManage.StudentManage_Action import Student_Manage
from WoniuBoss_GUI_Test.tools.util import Util
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.service import Service
class Stu_Manage_Test(unittest.TestCase):
    def setUp(self) -> None:
        self.driver = Service.get_driver()
    def tearDown(self) -> None:
        self.driver.close()

    # 获取要查询的数据
    search_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[3]
    search_data = Util.get_excel(search_conf)
    @parameterized.expand(search_data)
    #学员信息查询测试
    def test_search_stuInfo(self,name,expect):
        search_info = {'name':name,'expect':expect}
        Student_Manage(self.driver).search_stu_info(search_info)
        #获取查询后的记录数
        msg = self.driver.find_element_by_xpath("//span[@class='pagination-info']").get_attribute("innerHTML")
        regex = re.compile('总共.(\d+?)')
        num = regex.findall(msg)[0]
        if int(num) >= 1: #大于等于1条，说明查到数据了
            actual = 'search-success'
        else:
            actual = 'search-fail'
        self.assertEqual(actual, expect)

    alter_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[4]
    alter_data = Util.get_excel(alter_conf)
    @parameterized.expand(alter_data)
    #随机修改学员信息测试
    def test_alter_stu_info(self,phone,status,expect):
        alter_info = {'phone':phone,'status':status,'expect':expect}
        Student_Manage(self.driver).alter_stu_info(alter_info)
        ele = self.driver.find_element_by_xpath("//div[@class='bootbox-body']")
        msg = ele.get_attribute('innerHTML')
        if msg == '操作成功':
            actual = 'alter-success'
        else:
            actual = 'alter-fail'
        self.assertEqual(actual, expect)

    evaluate_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[5]
    evaluate_data = Util.get_excel(evaluate_conf)
    @parameterized.expand(evaluate_data)
    #日常考评查询测试
    def test_search_evaluate(self,name,expect):
        search_info = {'name':name,'expect':expect}
        Student_Manage(self.driver).search_evaluate(search_info )
        ele = self.driver.find_element_by_xpath("//div[2]/table/tbody/tr/td")
        msg = ele.get_attribute('innerHTML')
        if msg == '无符合条件的记录':
            actual = 'search-fail'
        else:
            actual = 'search-success'
        self.assertEqual(actual, expect)

    #随机录入周考成绩测试
    add_grade_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[6]
    add_grade_data = Util.get_excel(add_grade_conf)
    @parameterized.expand(add_grade_data)
    def test_add_week_grade(self,stage,grade,expect):
        grade_info = {'stage':stage,'grade':grade,'expect':expect}
        Student_Manage(self.driver).add_week_grade(grade_info )
        if Service.is_element_present(self.driver,'xpath',"//div[@class='bootbox-body']") == True:
            actual = 'add-fail'
        else:
            actual = 'add-success'
        self.assertEqual(actual, expect)

    #查询周考成绩测试
    search_grade_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[7]
    search_grade_data = Util.get_excel(search_grade_conf)
    @parameterized.expand(search_grade_data)
    def test_search_week_grade(self,area,classes,name,expect):
        search_grade_info = {'area': area, 'classes': classes, 'name':name,'expect': expect}
        Student_Manage(self.driver).search_week_grade(search_grade_info)
        ele = self.driver.find_element_by_xpath("//div[2]/table/tbody/tr/td")
        msg = ele.get_attribute('innerHTML')
        if msg == '无符合条件的记录':
            actual = 'search-fail'
        else:
            actual = 'search-success'
        self.assertEqual(actual, expect)
    # 阶段考评查询测试
    search_stagegrade_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[8]
    search_stagegrade_data = Util.get_excel(search_stagegrade_conf)
    @parameterized.expand(search_stagegrade_data)
    def test_search_week_grade(self,area,classes,name,expect):
        search_stagegrade_info = {'area': area, 'classes': classes, 'name':name,'expect': expect}
        Student_Manage(self.driver).search_week_grade(search_stagegrade_info)
        ele = self.driver.find_element_by_xpath("//div[2]/table/tbody/tr/td")
        msg = ele.get_attribute('innerHTML')
        if msg == '无符合条件的记录':
            actual = 'search-fail'

        else:
            actual = 'search-success'
        self.assertEqual(actual, expect)

    #阶段考评录入测试
    add_stagegrade_conf = Util.get_json('../../conf/StuManage_Conf/StuManage_Excel.conf')[9]
    add_stagegrade_data = Util.get_excel(add_stagegrade_conf)
    @parameterized.expand(add_stagegrade_data)
    def test_add_week_grade(self,classes,stage,grade,evaluate,expect):
        grade_info = {'classes':classes,'stage':stage,'grade':grade,'evaluate':evaluate,'expect':expect}
        Student_Manage(self.driver).add_stage_grade(grade_info )
        if Service.is_element_present(self.driver,'xpath',"//div[@class='bootbox-body']") == True:
            actual = 'add-fail'

        else:
            actual = 'add-success'
        self.assertEqual(actual, expect)



if __name__ == '__main__':
    unittest.main()