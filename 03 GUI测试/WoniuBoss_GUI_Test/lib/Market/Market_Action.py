# encoding: utf-8
# @author: yinqianjun
# @file: Market_Action.py
# @time: 2020/5/17 20:55
from selenium.webdriver.support.wait import WebDriverWait
from WoniuBoss_GUI_Test.tools.service import Service
import time
class Market:
    def __init__(self,driver):
        self.driver = driver
        self.driver.implicitly_wait(10)
    #进入资源管理—简历资源模块
    def into_resource(self):
        Service.open_page(self.driver)
        Service.only_login(self.driver)
        time.sleep(2)
        Service.into_module(self.driver,'市场营销')
        Service.into_module(self.driver, '简历资源')

    #选择区域
    def input_area(self,area):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[1]/select')
        Service.droplist(ele,area)

    #输入电话
    def input_phone(self,phone):
        ele =self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[3]/input')
        ele.click()
        ele.send_keys(phone)

    #选择部门
    def input_partment(self,partment):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[2]/select')
        Service.droplist(ele, partment)

    #输入姓名
    def input_name(self,name):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[4]/input')
        ele.send_keys(name)

     #选择性别
    def input_sex(self,sex):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[5]/select')
        Service.droplist(ele, sex)

    #选择状态
    def input_status(self,status):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[6]/select')
        Service.droplist(ele, status)

    #输入微信
    def input_wx(self,wx):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[7]/input')
        ele.click()
        ele.send_keys(wx)

    #输入qq
    def input_qq(self,qq):
        ele =self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[8]/input')
        ele.click()
        ele.send_keys(qq)

    #输入学校
    def input_school(self,school):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[9]/input')
        ele.send_keys(school)

    #选择学历
    def input_education(self,education):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[10]/select')
        Service.droplist(ele, education)

    #输入专业
    def input_major(self,major):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[11]/input')
        ele.send_keys(major)

    #输入工作年限
    def input_workage(self,workage):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[12]/select')
        Service.droplist(ele, workage)

    #输入年龄
    def input_age(self,age):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[13]/input')
        ele.send_keys(age)

    #输入渠道来源
    def input_source(self,source):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[14]/select')
        Service.droplist(ele, source)

    #输入教育经历
    def input_eduexp(self,eduexp):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[15]/textarea')
        ele.send_keys(eduexp)

    #输入工作经历
    def input_experience(self,experience):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[16]/textarea')
        ele.send_keys(experience)

    #输入最后跟踪内容
    def input_tracking(self,tracking):
        ele = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/form/div/div/div[17]/textarea')
        ele.send_keys(tracking)

    #增加简历资源
    def add_resource(self,resource_info):
        self.into_resource()
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[2]/button[4]').click()
        self.input_phone(resource_info['phone'])
        self.input_name(resource_info['name'])
        self.input_age(resource_info['age'])
        self.input_area(resource_info['area'])
        self.input_partment(resource_info['partment'])
        self.input_education(resource_info['education'])
        self.input_eduexp(resource_info['eduexp'])
        self.input_experience(resource_info['experience'])
        self.input_sex(resource_info['sex'])
        self.input_school(resource_info['school'])
        self.input_source(resource_info['source'])
        self.input_status(resource_info['status'])
        self.input_workage(resource_info['workage'])
        self.input_wx(resource_info['wx'])
        self.input_qq(resource_info['qq'])
        self.input_major(resource_info['major'])
        self.driver.find_element_by_id('addCusBtn').click()
        if Service.is_element_present(self.driver,'xpath','/html/body/div[12]/div/div/div[3]/button'):
            return True
        else:
            return False

    #输入查询内容
    def input_value(self,content):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[2]/input[3]').send_keys(content)

    #根据电话qq微信姓名精确查询
    def search_resource(self,info):
        self.into_resource()
        self.input_value(info['value'])
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[2]/button[1]').click()
        if Service.is_element_present(self.driver,'xpath',"//td[12]/button[@class='btn btn-info']")==True:
            return True
        else:
            return False

    #上传简历
    def upload_resource(self,info):
        self.into_resource()
        self.driver.find_element_by_xpath("/html/body/div[8]/div[2]/div[2]/button[3]").click()#点击上传按钮
        area=self.driver.find_element_by_xpath("//select[@id='regionSelect']")#区域下拉框
        Service.droplist(area,info['area'])
        partment=self.driver.find_element_by_xpath("//select[@id='dpetSelect']")#部门下拉框
        Service.droplist(partment, info['partment'])
        self.driver.find_element_by_xpath('//*[@id="files"]').send_keys(info['path'])#传入文件路径
        self.driver.find_element_by_xpath("//div[@class='modal-footer']/button[@class='btn btn-primary btn-padding']").click()
        msg = self.driver.find_element_by_xpath("//div[@class='bootbox-body']").get_attribute("innerHTML")
        return msg
if __name__ == '__main__':
    driver = Service.get_driver()
    mk =Market(driver)
    info = {'path': 'D:\\woniuboss接口信息.xls','area':'成都','partment':'咨询部'}
    mk.upload_resource(info)

