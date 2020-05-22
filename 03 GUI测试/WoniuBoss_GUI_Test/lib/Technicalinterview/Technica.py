# 技术面试
import re
from WoniuBoss_GUI_Test.tools.service import Service


class Tech:

    def __init__(self, driver):
        self.driver = driver

    # 选择区域下拉框中的内容
    def select_area(self, value):
        area = self.driver.find_element_by_id('region_id')
        Service.select_value(area, value)

    # 选择面试下拉框中的内容
    def select_inter(self, value):
        inter = self.driver.find_element_by_id('studentSelect')
        Service.select_value(inter,value)

    # 选择班级下拉框中的内容
    def select_gra(self, value):
        gra = self.driver.find_element_by_id('semesterSelect')
        Service.select_value(gra,value)

    # 输入姓名
    def input_names(self, value):
        names = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div/div[1]/input[1]')
        Service.send_input(names,value)

    # 输入学号
    def input_num(self, value):
        num = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div/div[1]/input[2]')
        Service.send_input(num,value)

    # 选择面试结果下拉框中的内容
    def select_result(self, value):
        res = self.driver.find_element_by_xpath('//*[@id="isPassSkill"]')
        Service.select_value(res,value)
    # 输入评价内容
    def input_content(self,value):
        con = self.driver.find_element_by_xpath('//*[@id="sval"]')
        Service.send_input(con,value)

    # 点击搜索
    def click_search_button(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div/div[1]/button').click()

    # 点击面试
    def click_inter_button(self):
        self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div/div/div/div[2]/div[2]/div[2]/table/tbody/tr/td[9]/button').click()

    # 点击保存按钮
    def click_save_button(self):
        self.driver.find_element_by_id('saveSkillbtn').click()

    # 随机点击面试按钮
    def click_random_inter_button(self):
        number = Service.random_delete(self.driver,"/html/body/div[8]/div[2]/div/div/div/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        self.driver.find_element_by_xpath(f'//*[@id="stuInfo_table"]/tbody/tr[{number}]/td[9]/button').click()

    # 获取操作之后的提示信息
    def get_msg(self):
        return self.driver.find_element_by_xpath('/html/body/div[10]/div/div/div[2]/div').text

    # 完成搜索动作
    def do_search(self,sous_info):
        self.select_area(sous_info[0])
        self.select_inter(sous_info[1])
        self.select_gra(sous_info[2])
        self.input_names(sous_info[3])
        self.input_num(sous_info[4])
        self.click_search_button()

    # 随机面试动作组合
    def do_inter(self,inter_info):
        self.click_random_inter_button()
        import time
        time.sleep(10)
        self.select_result(inter_info[0])
        self.input_content(inter_info[1])
        self.click_save_button()


if __name__ == '__main__':
    pass
