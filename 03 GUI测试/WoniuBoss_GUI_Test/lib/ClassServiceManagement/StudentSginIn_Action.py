import time

from selenium.webdriver.support.select import Select

from WoniuBoss_GUI_Test.tools.service import Service


class SSI_Action:

    def __init__(self , driver):
        self.driver = driver

    # 点击班务管理-学员考勤的模块名
    def click_module_name(self):
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[2]/a']
        Service.open_module_connect(self.driver, info)


    # 点击班、阶段
    def click_SSI_class(self):
        ssi_class = self.driver.find_element_by_xpath\
            ('/html/body/div[8]/div[2]/div/div/div/div[3]/div/div/div/div[2]/div[1]/a/span')
        # //*[@id="class_msg"]
        ssi_class.click()
        time.sleep(3)



    # 点击姓名
    def click_SSI_name(self , ssiname):
        time.sleep(3)
        ssi_name = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/input')
        Service.send_input(ssi_name, ssiname)


    # 点击搜索
    def click_SSI_query(self):
        ssi_query = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/button[1]')
        ssi_query.click()



    # 学员状态,李四20
    def click_stu_state(self , ssicontents):
        time.sleep(1)
        stu_state = self.driver.find_element_by_xpath\
            ('//*[@id="236"]/tbody/tr[3]/td[8]/select')
        Select(stu_state).select_by_visible_text(ssicontents)


    # 点击考勤，李四20
    def click_SginIn(self):
        time.sleep(1)
        ssi = self.driver.find_element_by_xpath('//*[@id="confirmAttenBtn_3549"]')
        ssi.click()



    # 返回
    def click_Return(self):
        ssi_rn = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/button[2]')
        ssi_rn.click()


    # 批量考勤
    def clcik_Batch_ssi(self):
        bat_ssi = self.driver.find_element_by_xpath\
            ('//*[@id="panel-element-236"]/div/button')
        bat_ssi.click()
        # 点击确定
        time.sleep(1)
        click_confirm = self.driver.find_element_by_xpath\
            ('/html/body/div[9]/div/div/div[3]/button[2]')
        click_confirm.click()




    # 查询动作
    def do_query(self , ssiquerydata):
        self.click_SSI_name(ssiquerydata['ssiname'])
        self.click_SSI_query()


    # 考勤动作
    def do_ssi(self , ssistetedata):
        self.click_stu_state(ssistetedata['ssicontents'])
        self.click_SginIn()


    # 返回动作
    def do_Return(self , rnssidata):
        self.click_SSI_name(rnssidata['ssiname'])
        self.click_SSI_query()
        self.click_Return()


    # 批量考勤动作
    def do_Bactch_ssi(self , Bactchdata):
        # 张三06
        stu_state_one = self.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[2]/td[8]/select')
        Select(stu_state_one).select_by_visible_text(Bactchdata['ssicontents_one'])

        # 张三
        stu_state_two = self.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[4]/td[8]/select')
        Select(stu_state_two).select_by_visible_text(Bactchdata['ssicontents_two'])

        # 张三08
        stu_state_three = self.driver.find_element_by_xpath \
            ('//*[@id="236"]/tbody/tr[5]/td[8]/select')
        Select(stu_state_three).select_by_visible_text(Bactchdata['ssicontents_three'])

        self.clcik_Batch_ssi()

