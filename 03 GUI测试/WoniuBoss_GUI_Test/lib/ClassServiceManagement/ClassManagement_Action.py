
# 班务管理
import time

from selenium.webdriver.support.select import Select

from WoniuBoss_GUI_Test.tools.service import Service


class CSM_Action:

    def __init__(self , driver):
        self.driver = driver




    # 点击模块名
    def click_module_name(self):
        Service.open_page(self.driver)
        info = ['WNCD051', 'woniu123', 'woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '/html/body/div[4]/div[2]/div[8]/div[2]/div/ul/li[1]/a']
        Service.open_module_connect(self.driver, info)


    # 点击新增按钮
    def CSM_AddButton(self):
        time.sleep(1)
        csm_addbt = self.driver.find_element_by_xpath\
            ('//*[@id="cmDiv"]/div[1]/button')
        csm_addbt.click()


    # 班号
    def CSM_Cid(self , classnumber):
        classid = self.driver.find_element_by_xpath\
            ('//*[@id="addClass-form"]/div/div[1]/input')
        Service.send_input(classid , classnumber)


    # 方向
    def CSM_Direction(self , public):
        direction = self.driver.find_element_by_xpath\
            ('//*[@id="addClass-form"]/div/div[2]/select')
        Select(direction).select_by_visible_text(public)


    # 时间
    def CSM_Time(self):
        c_time = self.driver.find_element_by_xpath('//*[@id="addClass-form"]/div/div[3]/input')
        js = "arguments[0].value='2020-05-19'"
        self.driver.execute_script(js, c_time)


    # 班主任
    def CSM_teacher(self , tname):
        teacher = self.driver.find_element_by_xpath\
            ('//*[@id="addClass-form"]/div/div[4]/select')
        Select(teacher).select_by_value(tname)


    # 点击保存
    def CSM_Save(self):
        time.sleep(1)
        save = self.driver.find_element_by_xpath\
            ('//*[@id="addClass-modal"]/div/div/div[3]/button')
        save.click()


    # 校区
    def CSM_School(self , sclname):
        school = self.driver.find_element_by_xpath\
            ('//*[@id="cmDiv"]/div[1]/select[1]')
        Select(school).select_by_visible_text(sclname)


    # 开班状态
    def CSM_ClassState(self , all):
        state = self.driver.find_element_by_xpath\
            ('//*[@id="cmDiv"]/div[1]/select[2]')
        Select(state).select_by_visible_text(all)

    # 点击新增成功确定按钮
    def click_ok(self):
        time.sleep(1)
        c_ok = self.driver.find_element_by_xpath('/html/body/div[11]/div/div/div[3]/button')
        c_ok.click()


    # 班级新增组合
    def CSM_add(self , addclass_data):
        self.CSM_AddButton()
        self.CSM_Cid(addclass_data['classnumber'])
        self.CSM_Direction(addclass_data['public'])
        self.CSM_Time()
        self.CSM_teacher(addclass_data['tnumber'])
        self.CSM_Save()
        self.click_ok()


    # 班级查询
    def CSM_query(self , queryclassdata):
        self.CSM_School(queryclassdata["sclname"])
        self.CSM_ClassState(queryclassdata["all"])



# if __name__ == '__main__':
#     driver = Service.get_driver()
#     CSM_Action(driver).click_module_name()
#     addclass_data = ["WNCD005" , "测试" , "6"]
    # CSM_Action(driver).CSM_add(addclass_data)
    # queryclass_data = ["成都" , "全部"]
    # CSM_Action(driver).CSM_query_new(queryclass_data[0] , queryclass_data[1])



