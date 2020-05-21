# encoding: utf-8
# @author: yinqianjun
# @file: StudentManage_Action.py
# @time: 2020/5/19 11:59
from selenium.webdriver.support.wait import WebDriverWait
from WoniuBoss_GUI_Test.tools.service import Service
import time
class Student_Manage:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)

    #输入查询内容
    def input_value(self,content):
        self.driver.find_element_by_xpath("//input[@class='text']").send_keys(content)

    #进入到学员管理-学员信息模块
    def into_stu_manage(self):
        Service.open_page(self.driver)
        Service.only_login(self.driver)
        # time.sleep(2)
        Service.into_module(self.driver,'学员管理')

    #查询学员信息
    def search_stu_info(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '学员信息')
        self.input_value(info['name'])
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-padding']").click()
        time.sleep(1)

    #随机修改学员信息
    def alter_stu_info(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '学员信息')
        #先点击查询
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-padding']").click()
        time.sleep(1)
        xpath = "//span[@class='pagination-info']"
        num = Service.random_delete(self.driver,xpath)
        #点击随机到的资源修改按钮
        self.driver.find_element_by_xpath(f"//tr[{num}]/td[12]/button[@class='btn btn-info'][2]").click()
        time.sleep(1)
        #修改电话
        phone = self.driver.find_element_by_name("stu.tel")
        Service.send_input(phone,info['phone'])
        #修改状态
        status = self.driver.find_element_by_name("stu.status")
        Service.droplist(status, info['status'])
        self.driver.find_element_by_xpath("//div[@class='modal-content']/div[@class='modal-footer']/button[@class='btn btn-primary btn-save']").click()

    #日常考评查询
    def search_evaluate(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '日常考评')
        #找到姓名输入框，输入
        name = self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div/div/div/div[1]/input")
        Service.send_input(name,info['name'])
        self.driver.find_element_by_xpath("//button[@class='btn btn-info btn-padding']").click()

    #随机录入周考成绩
    def add_week_grade(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '周考成绩')
        xpath = "//span[@class='pagination-info']"
        num = Service.random_delete(self.driver,xpath)
        #点击随机到的录入按钮
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//tr[{num}]/td[9]/button[@class='btn btn-padding btn-info']").click()
        #输入阶段
        stage= self.driver.find_element_by_xpath("//select[@id='we_phase']")
        Service.droplist(stage, info['stage'])
        #输入周数
        # weekinfo=self.driver.find_element_by_xpath("//select[@id='we_week']")
        # Service.droplist(stage, info['weekinfo'])
        #输入分数
        grade =self.driver.find_element_by_xpath("//div[@class='col-md-12 col-sm-12 col-xs-12 form-group'][4]/input[@class='text']")
        Service.send_input(grade, info['grade'])
        #点击保存
        self.driver.find_element_by_xpath("//div[9]/div/div/div[3]/button").click()

    #周考成绩查询
    def search_week_grade(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '周考成绩')
        #选择区域
        area = self.driver.find_element_by_xpath("//select[@class='sel-text'][1]")
        Service.droplist(area, info['area'])
        #选择班级
        classes = self.driver.find_element_by_xpath("//select[@class='sel-text'][2]")
        Service.droplist(classes, info['classes'])
        #输入姓名
        name = self.driver.find_element_by_xpath("//div[2]/div/div/div/div[1]/input")
        Service.send_input(name, info['name'])
        #点击查询
        self.driver.find_element_by_xpath("//div[2]/div/div/div/div[1]/button").click()

    #阶段考评查询
    def search_stage_grade(self,info):
        self.into_stu_manage()
        Service.into_module(self.driver, '阶段考评')
        #选择区域
        area = self.driver.find_element_by_xpath("//select[@class='sel-text'][1]")
        Service.droplist(area, info['area'])
        #选择班级
        classes = self.driver.find_element_by_xpath("//select[@class='sel-text'][2]")
        Service.droplist(classes, info['classes'])
        #输入姓名
        name = self.driver.find_element_by_xpath("//div[2]/div/div/div/div[1]/input")
        Service.send_input(name, info['name'])
        #点击查询
        self.driver.find_element_by_xpath("//div[2]/div/div/div/div[1]/button").click()

    # 随机录入阶段考评成绩
    def add_stage_grade(self, info):
        self.into_stu_manage()
        Service.into_module(self.driver, '阶段考评')
        xpath = "//span[@class='pagination-info']"
        num = Service.random_delete(self.driver, xpath)
        # 点击随机到的录入按钮
        time.sleep(1)
        self.driver.find_element_by_xpath(f"//tr[{num}]/td[9]/button[@class='btn btn-padding btn-info']").click()
        #输入班级
        classes = self.driver.find_element_by_xpath('//*[@id="ph_cl"]')
        Service.droplist(classes, info['classes'])
        # 输入阶段
        stage = self.driver.find_element_by_xpath("//select[@id='ph_phase']")
        Service.droplist(stage, info['stage'])
        # 输入分数
        grade = self.driver.find_element_by_xpath("//div[3]/div[1]/input")
        Service.send_input(grade, info['grade'])
        #输入评语
        evaluate = self.driver.find_element_by_xpath("//div[3]/div[3]/textarea")
        Service.send_input(evaluate, info['evaluate'])
        # 点击保存
        self.driver.find_element_by_xpath("//div[9]/div/div/div[3]/button").click()



if __name__ == '__main__':
    driver = Service.get_driver()
    s = Student_Manage(driver)
    info = {'classes':'WNCDC33','stage':'第二阶段','grade':80,'evaluate':'良好'}
    s.add_stage_grade(info)

