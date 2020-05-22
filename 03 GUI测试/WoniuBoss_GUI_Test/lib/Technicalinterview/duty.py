# 教师值班
from WoniuBoss_GUI_Test.tools.service import Service
class Duty:

    def __init__(self, driver):
        self.driver = driver
    # 选择值班人下拉框中的内容
    def select_duty(self, value):
        duty = self.driver.find_element_by_xpath('//*[@id="addDuty-table"]/tr/td[1]/select')
        Service.select_value(duty, value)
    # 选择区域下拉框中的内容
    def select_area(self, value):
        area = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div/select[1]')
        Service.select_value(area, value)

    # 选择日志情况下拉框中的内容
    def select_log(self, value):
        log1 = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div/select[2]')
        Service.select_value(log1, value)

    # 输入编号
    def input_serial(self,value):
        seri = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div[1]/div/input[1]')
        Service.send_input(seri,value)

    # 输入值班开始日期
    def input_stars_time(self,starttime):
        js2 = f"document.querySelector('#queryAera > div > input:nth-child(4)').removeAttribute('text/javascript');"
        self.driver.execute_script(js2)
        js_value2 = 'document.querySelector("#queryAera > div 'f' > input:nth-child(4)").value="{starttime}"'
        self.driver.execute_script(js_value2)
    # 输入值班结束日期
    def input_endu_time(self,starttime):
        js2 = f"document.querySelector('#queryAera > div > input:nth-child(4)').removeAttribute('text/javascript');"
        self.driver.execute_script(js2)
        js_value2 = 'document.querySelector("#queryAera > div 'f' > input:nth-child(4)").value="{starttime}"'
        self.driver.execute_script(js_value2)


    # 输入值班日期
    def input_startdu_time(self,stime):
        js1 = f"document.querySelector('#addDuty-table > tr > td:nth-child(2) > input').removeAttribute('text/javascript');"
        self.driver.execute_script(js1)
        js_value1 = 'document.querySelector("#addDuty-table > tr > td:nth-child(2) 'f'> input").value="{stime}"'
        self.driver.execute_script(js_value1)

    # 获取操作之后的提示信息
    def get_msg(self):
        return self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[2]/div').text



    # 点击保存按钮
    def click_dusave_button(self):
        self.driver.find_element_by_xpath('//*[@id="addDuty-modal"]/div/div/div[3]/button').click()

    # 点击指定值班按钮
    def click_spectify_button(self):
        self.driver.find_element_by_xpath('//*[@id="queryAera"]/div/button[2]').click()

    # 完成指定值班动作
    def do_specti(self,specti_info):
        self.click_spectify_button()
        self.select_duty()
        self.input_startdu_time()
        self.click_dusave_button()