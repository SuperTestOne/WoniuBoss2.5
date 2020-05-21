from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util
import time

class DR_Action:

    def __init__(self,driver):
        self.driver = driver
        self.ele = Util.get_json('..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf')

    #完成查询动作
    def do_query(self,query_info):
        Service.select_motion(self.driver,'xpath', self.ele[8]["DR_area_xpath"], query_info[0])
        Service.select_motion(self.driver, 'xpath', self.ele[8]["DR_department_xpath"], query_info[1])
        Service.select_motion(self.driver, 'xpath', self.ele[8]["DR_counselor_xpath"], query_info[2])
        Service.select_motion(self.driver, 'xpath', self.ele[8]["DR_status_xpath"], query_info[3])
        Service.select_motion(self.driver, 'xpath', self.ele[8]["DR_source_xpath"], query_info[4])
        Service.input_motion(self.driver, 'xpath', self.ele[8]["DR_condition_xpath"], query_info[5])
        Service.click_motion(self.driver, 'xpath', self.ele[8]["DR_query_xpath"])

    #完成转交动作
    def do_deliver(self,deliver_info):
        Service.click_motion(self.driver, 'xpath', self.ele[8]["DR_query_xpath"])
        num = Service.random_delete(self.driver, self.ele[0]["TR_student_list_xpath"])
        Service.click_motion(self.driver, 'xpath', f'//*[@id="transmit-table"]/tbody/tr[{num}]/td[1]/input')
        Service.select_motion(self.driver, 'xpath', self.ele[9]["DR_area_xpath"], deliver_info[0])
        Service.select_motion(self.driver, 'xpath', self.ele[9]["DR_department_xpath"], deliver_info[1])
        Service.select_motion(self.driver, 'xpath', self.ele[9]["DR_counselor_xpath"], deliver_info[2])
        self.driver.execute_script('window.scrollBy(0,-100)')
        time.sleep(3)
        Service.click_motion(self.driver, 'xpath', self.ele[9]["DR_put_xpath"])
        time.sleep(3)
        Service.click_motion(self.driver, 'xpath', self.ele[9]["DR_confirm_put_xpath"])
        time.sleep(3)
        Service.click_motion(self.driver, 'xpath', self.ele[9]["DR_put_pass_xpath"])
        time.sleep(3)