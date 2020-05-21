from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util
import time

class CR_Action:

    def __init__(self,driver):
        self.driver = driver
        self.ele = Util.get_json('..\\..\\conf\\ResourceAdministration_Conf\\RA_Element.conf')

    #完成查询动作
    def do_query(self,query_info):
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_area_xpath"], query_info[0])
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_department_xpath"], query_info[1])
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_abandon_xpath"], query_info[2])
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_status_xpath"], query_info[3])
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_source_xpath"], query_info[4])
        Service.select_motion(self.driver,'xpath', self.ele[6]["CR_education_xpath"], query_info[5])
        Service.input_motion(self.driver, 'xpath', self.ele[6]["CR_condition_xpath"], query_info[6])
        Service.click_motion(self.driver, 'xpath', self.ele[6]["CR_query_xpath"])

    #完成认领动作
    def do_claim(self):
        Service.click_motion(self.driver, 'xpath', self.ele[6]["CR_query_xpath"])
        num = Service.random_delete(self.driver, self.ele[0]["TR_student_list_xpath"])
        Service.click_motion(self.driver,'xpath',f'//*[@id="public-pool-table"]/tbody/tr[{num}]/td[1]/input')
        time.sleep(1)
        Service.click_motion(self.driver,'xpath',self.ele[7]["CR_claim_xpath"])
        Service.click_motion(self.driver, 'xpath',self.ele[7]["CR_confirm_claim_xpath"])
