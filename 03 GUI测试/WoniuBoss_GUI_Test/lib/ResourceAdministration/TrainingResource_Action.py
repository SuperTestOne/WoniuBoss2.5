from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util
import time

class TR_Action:

    def __init__(self,driver):
        self.driver = driver
        self.ele = Util.get_json('..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf')

    #输入跟踪资源下次跟踪时间
    def input_tail_time(self,time):
        # js去掉readonly属性
        js = 'document.getElementById("next_time").removeAttribute("readonly");'
        self.driver.execute_script(js)
        # js添加时间
        js_value = f'document.getElementById("next_time").value="{time}"'
        self.driver.execute_script(js_value)

    #输入跟踪资源状态为已报名时，缴费时间
    def input_tail_paytime(self,paytime):
        # js去掉readonly属性
        js = 'document.querySelector("#panel-element-enroll > div > div > div:nth-child(2) ' \
             '> div:nth-child(3) > input").removeAttribute("readonly");'
        self.driver.execute_script(js)
        # js添加时间
        js_value = 'document.querySelector("#panel-element-enroll > div > div > div:nth-child(2) ' \
             f'> div:nth-child(3) > input").value="{paytime}"'
        self.driver.execute_script(js_value)

    #完成新增动作
    def do_add(self,add_info):
        Service.click_motion(self.driver,'xpath',self.ele[1]["TR_add_xpath"])
        Service.input_motion(self.driver,'xpath',self.ele[1]["TR_phone_xpath"],add_info[0])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_name_xpath"], add_info[1])
        Service.select_motion(self.driver,'xpath', self.ele[1]["TR_sex_xpath"], add_info[2])
        Service.select_motion(self.driver,'xpath', self.ele[1]["TR_status_xpath"], add_info[3])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_WeChat_xpath"], add_info[4])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_QQ_xpath"], add_info[5])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_school_xpath"], add_info[6])
        Service.select_motion(self.driver,'xpath', self.ele[1]["TR_education_xpath"], add_info[7])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_major_xpath"], add_info[8])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_intent_xpath"], add_info[9])
        Service.select_motion(self.driver,'xpath', self.ele[1]["TR_workage_xpath"], add_info[10])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_salary_xpath"], add_info[11])
        Service.select_motion(self.driver,'xpath', self.ele[1]["TR_source_xpath"], add_info[12])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_email_xpath"], add_info[13])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_age_xpath"], add_info[14])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_eduexp_xpath"], add_info[15])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_experience_xpath"], add_info[16])
        Service.input_motion(self.driver,'xpath', self.ele[1]["TR_tracking_xpath"], add_info[17])
        Service.click_motion(self.driver,'id', self.ele[1]["TR_save_id"])
        time.sleep(1)
        Service.click_motion(self.driver,'xpath', self.ele[1]["TR_affirm_xpath"])
        if Service.is_element_present(self.driver,'xpath','/html/body/div[2]/div[2]/ul/li[2]/a') == False:
            Service.click_motion(self.driver, 'xpath', '//*[@id="form-add"]/div/div/div/button/span[1]')

    #完成随机删除动作
    def do_delete(self):
        num = Service.random_delete(self.driver,self.ele[0]["TR_student_list_xpath"])
        Service.click_motion(self.driver,"xpath",f"//*[@id='personal-table']/tbody/tr[{num}]/td[1]/input")
        Service.click_motion(self.driver,'id', self.ele[2]["TR_abandon_id"])
        time.sleep(1)
        Service.click_motion(self.driver,'xpath', self.ele[2]["TR_confirm_abandon_xpath"])

    #完成查询动作
    def do_query(self,query_info):
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_resource_xpath"], query_info[0])
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_status_xpath"], query_info[1])
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_source_xpath"], query_info[2])
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_area_xpath"], query_info[3])
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_department_xpath"], query_info[4])
        Service.select_motion(self.driver,'xpath', self.ele[3]["TR_counselor_xpath"], query_info[5])
        Service.input_motion(self.driver,'id', self.ele[3]["TR_starttime_id"], query_info[6])
        Service.input_motion(self.driver,'id', self.ele[3]["TR_endtime_id"], query_info[7])
        Service.input_motion(self.driver,'xpath', self.ele[3]["TR_condition_xpath"], query_info[8])
        Service.click_motion(self.driver,'xpath', self.ele[0]["TR_search_xpath"])

    #完成跟踪动作
    def do_tail(self,tail_info):
        Service.select_motion(self.driver,"xpath", self.ele[3]["TR_resource_xpath"], tail_info[0])
        num = Service.random_delete(self.driver,self.ele[0]["TR_student_list_xpath"])
        Service.click_motion(self.driver,"xpath", f"//*[@id='personal-table']/tbody/tr[{num}]/td[15]/button[1]")
        phone = Service.get_hint(self.driver,self.ele[4]["TR_phone_xpath"])
        Service.click_motion(self.driver,"xpath", self.ele[4]["TR_resource_xpath"])
        if len(tail_info) > 5:
            Service.select_motion(self.driver,"id", self.ele[4]["TR_status_id"], tail_info[1])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_grade_xpath"], tail_info[2])
            self.input_tail_time(tail_info[3])
            Service.input_motion(self.driver,"xpath", self.ele[4]["TR_content_xpath"], tail_info[4])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_inclass_xpath"], tail_info[5])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_tuition_xpath"], tail_info[6])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_deposit_xpath"], tail_info[7])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_pay_xpath"], tail_info[8])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_account_xpath"], tail_info[9])
            self.input_tail_paytime(tail_info[10])
            Service.click_motion(self.driver,"id", self.ele[4]["TR_save_id"])
        else:
            Service.select_motion(self.driver,"id", self.ele[4]["TR_status_id"], tail_info[1])
            Service.select_motion(self.driver,"xpath", self.ele[4]["TR_grade_xpath"], tail_info[2])
            self.input_tail_time(tail_info[3])
            Service.input_motion(self.driver,"xpath", self.ele[4]["TR_content_xpath"], tail_info[4])
            Service.click_motion(self.driver,"id", self.ele[4]["TR_save_id"])
        print(phone)
        return phone

    #完成修改动作
    def do_alter(self,alter_info):
        Service.click_motion(self.driver,"xpath", self.ele[0]["TR_search_xpath"])
        time.sleep(1)
        num = Service.random_delete(self.driver,self.ele[0]["TR_student_list_xpath"])
        time.sleep(1)
        Service.click_motion(self.driver,"xpath", f"//*[@id='personal-table']/tbody/tr[{num}]/td[15]/button[2]")
        Service.input_motion(self.driver,"xpath", self.ele[5]["TR_name_xpath"], alter_info[0])
        Service.input_motion(self.driver,"xpath", self.ele[5]["TR_phone_xpath"], alter_info[1])
        Service.select_motion(self.driver,"xpath", self.ele[5]["TR_status_xpath"], alter_info[2])
        Service.select_motion(self.driver,"xpath", self.ele[5]["TR_source_xpath"], alter_info[3])
        Service.click_motion(self.driver,"xpath", self.ele[5]["TR_save_xpath"])
