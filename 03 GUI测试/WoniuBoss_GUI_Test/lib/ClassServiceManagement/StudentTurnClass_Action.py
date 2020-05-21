import time

from selenium.webdriver.support.select import Select

from WoniuBoss_GUI_Test.tools.service import Service


class STC_Action:

    def __init__(self , driver):
        self.driver = driver

    # 点击班务管理-学员考勤的模块名
    def click_module_name(self):
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[4]/a']
        Service.open_module_connect(self.driver, info)

    # 区域
    def Area(self, stcarea):
        stc_area = self.driver.find_element_by_xpath \
            ('//*[@id="stuInfo"]/div[1]/select[1]')
        Select(stc_area).select_by_visible_text(stcarea)


    # 班级
    # def click_class(self , stcclass):
    #     stc_class = self.driver.find_element_by_xpath \
    #         ('//*[@id="stuInfo"]/div[1]/select[1]')
    #     Select(stc_class).select_by_visible_text(stcclass)


    # 状态
    def click_state(self , stcstate):
        stc_state = self.driver.find_element_by_xpath \
            ('//*[@id="stuInfo"]/div[1]/select[3]')
        Select(stc_state).select_by_visible_text(stcstate)


    # 姓名
    def click_name(self , stcname):
        stc_name = self.driver.find_element_by_xpath \
            ('//*[@id="stuInfo"]/div[1]/input')
        Service.send_input(stc_name , stcname)


    # 点击搜索
    def clcik_query(self):
        time.sleep(1)
        stc_query = self.driver.find_element_by_xpath \
            ('//*[@id="stuInfo"]/div[1]/button')
        stc_query.click()


    # 搜索动作
    def do_query(self , querydata):
        self.Area(querydata['stcarea'])
        self.click_state(querydata['stcstate'])
        self.click_name(querydata['stcname'])
        self.clcik_query()



    # 点击转班
    def click_turnclass(self):
        stc_turnclass = self.driver.find_element_by_xpath\
            ('//*[@id="stuInfo_table"]/tbody/tr[3]/td[12]/button')
        stc_turnclass.click()


    # 转班校区
    def click_school(self , stcschool):
        stc_school = self.driver.find_element_by_xpath \
            ('//*[@id="changeClass-modal"]/div/div/div[2]/div[1]/select')
        Select(stc_school).select_by_visible_text(stcschool)



    # 点击班级
    def turnclass(self , stcturnclass):
        stc_class = self.driver.find_element_by_xpath \
            ('//*[@id="changeClass-modal"]/div/div/div[2]/div[2]/select')
        Select(stc_class).select_by_visible_text(stcturnclass)


    # 点击确定
    def click_confirm(self):
        time.sleep(1)
        stc_confirm = self.driver.find_element_by_xpath\
            ('//*[@id="changeClass-modal"]/div/div/div[3]/button')
        stc_confirm.click()
        time.sleep(1)
        stc_confirm_two = self.driver.find_element_by_xpath\
            ('/html/body/div[11]/div/div/div[3]/button[2]')
        stc_confirm_two.click()

    # 刷新页面之后点击班务管理-学员转班
    def click_mould(self):
        time.sleep(2)
        cm = self.driver.find_element_by_xpath('//*[@id="list-31"]/div/ul/li[4]/a')
        cm.click()

    # 转校动作
    def do_turnschool(self , turnclassdata):
        self.click_turnclass()
        self.click_school(turnclassdata['stcschool'])
        self.turnclass(turnclassdata['stcclass'])
        self.click_confirm()