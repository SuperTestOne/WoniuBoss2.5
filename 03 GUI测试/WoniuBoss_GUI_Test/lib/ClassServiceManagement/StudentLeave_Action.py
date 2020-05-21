import time

from selenium.webdriver.support.select import Select

from WoniuBoss_GUI_Test.tools.service import Service


class STU_Action:

    def __init__(self , driver):
        self.driver = driver



    # 点击班务管理-学员请假的模块名
    def click_module_name(self):
        Service.open_page(self.driver)
        info = ['WNCD051', 'Woniu123', 'Woniu123', '/html/body/div[4]/div[2]/div[8]/div[1]/a',
                '//*[@id="list-31"]/div/ul/li[3]/a']
        Service.open_module_connect(self.driver, info)



    # 点击新增按钮
    def add_leave(self):
        time.sleep(1)
        addleave = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/div/button')
        addleave.click()


    # 开始时间
    def start_time(self):
        time.sleep(1)
        sta_time = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[1]/div[1]/input')
        js = "arguments[0].value='2020-05-19'"
        self.driver.execute_script(js , sta_time)




    # 结束时间
    def end_time(self):
        sta_time = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[1]/div[2]/input')
        js = "arguments[0].value='2020-05-19'"
        self.driver.execute_script(js, sta_time)



    # 请假类型
    def leave_type(self , leavetype):
        lev_type = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[2]/div[1]/select')
        Select(lev_type).select_by_visible_text(leavetype)


    # 请假天数
    def leave_days(self , days):
        lev_days = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[2]/div[2]/input')
        Service.send_input(lev_days , days)


    # 姓名
    def stu_name(self , sname):
        s_name = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[3]/div/input')
        Service.send_input(s_name , sname)
        # s_info = self.driver.find_element_by_xpath\
        #     ('//*[@id="leave-form"]/div[3]/div/ul/li/a')
        # s_info.click()
        clcik_text = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[4]/div/textarea')
        clcik_text.click()


    # 是否扣分
    def leave_points(self , points):
        lev_points = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[3]/select')
        Select(lev_points).select_by_visible_text(points)


    # 请假原因
    def leave_why(self , contents):
        lev_why = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[4]/div/textarea')
        Service.send_input(lev_why , contents)


    # 处理意见
    def leave_manage(self , manage):
        lev_manage = self.driver.find_element_by_xpath('//*[@id="leave-form"]/div[5]/div/textarea')
        Service.send_input(lev_manage , manage)


    # 点击保存
    def saveleave(self):
        lev_save = self.driver.find_element_by_xpath('//*[@id="leave-modal"]/div/div/div[3]/button')
        lev_save.click()


    #  新增请假后的确定
    def click_confirm(self):
        time.sleep(1)
        lev_confirm = self.driver.find_element_by_xpath\
            ('/html/body/div[17]/div/div/div[3]/button')
        lev_confirm.click()



    # 新增动作
    def do_add_leave(self , leavedata):
        self.add_leave()
        self.start_time()
        self.end_time()
        self.leave_type(leavedata["leavetype"])
        self.leave_days(leavedata["days"])
        self.stu_name(leavedata["sname"])
        self.leave_points(leavedata["points"])
        self.leave_why(leavedata["contents"])
        self.leave_manage(leavedata["manage"])
        self.saveleave()
        self.click_confirm()



    # 区域
    def Area(self , area):
        leave_area = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/select[1]')
        Select(leave_area).select_by_visible_text(area)


    # 请假状态
    def leave_state(self , state):
        lev_state = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/select[2]')
        Select(lev_state).select_by_visible_text(state)


    # 姓名
    def leave_stuname(self , stuname):
        lev_stuname = self.driver.find_element_by_xpath\
            ('//*[@id="content"]/div[2]/div/div/div/div[1]/input')
        Service.send_input(lev_stuname , stuname)


    # 点击查询按钮
    def click_query(self):
        time.sleep(1)
        ck_query = self.driver.find_element_by_xpath('//*[@id="content"]/div[2]/div/div/div/div[1]/button')
        ck_query.click()


    # 查询动作
    def do_query_leavename(self , leavequerydata):
        self.Area(leavequerydata['area'])
        self.leave_state(leavequerydata['state'])
        self.leave_stuname(leavequerydata['stuname'])
        self.click_query()



    # 销假
    def click_delete_leave(self):
        test_data = ['全部' , '全部']
        self.Area(test_data[0])
        self.leave_state(test_data[1])
        self.click_query()
        time.sleep(1)
        del_lev = self.driver.find_element_by_xpath\
            ('//*[@id="leave-table"]/tbody/tr[1]/td[12]/button[2]')
        del_lev.click()
        time.sleep(1)
        self.driver.find_element_by_xpath\
            ('/html/body/div[16]/div/div/div[3]/button[2]').click()
        self.driver.refresh()
        time.sleep(1)
        self.Area(test_data[0])
        self.leave_state(test_data[1])
        self.click_query()





    # 点击修改、张三
    def levae_edit(self):
        lev_edit = self.driver.find_element_by_xpath\
            ('//*[@id="leave-table"]/tbody/tr[3]/td[12]/button[3]')
        lev_edit.click()


    # 修改姓名
    def edit_name(self , editname):
        ed_name = self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[3]/div[1]/input')
        Service.send_input(ed_name , editname)
        clcik_text = self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[4]/div/textarea')
        clcik_text.click()



    # 修改请假类型
    def edit_leave_type(self , levtype):
        edit_lev = self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[2]/div[1]/select')
        Select(edit_lev).select_by_visible_text(levtype)


    # 修改是否扣分
    def edit_points(self , pointstype):
        ed_points = self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[3]/div[2]/select')
        Select(ed_points).select_by_visible_text(pointstype)


    # 处理意见
    def edit_manage(self , managecontents):
        ed_manage = self.driver.find_element_by_xpath('//*[@id="modLeave-form"]/div[5]/div/textarea')
        Service.send_input(ed_manage , managecontents)


    # 点击修改保存
    def edit_save(self):
        ed_save = self.driver.find_element_by_xpath\
            ('//*[@id="modLeave-modal"]/div/div/div[3]/button').click()



    # 修改动作
    def do_edit_leave(self , editleavedata):
        self.levae_edit()
        self.edit_name(editleavedata['editname'])
        self.edit_leave_type(editleavedata['levtype'])
        self.edit_points(editleavedata['pointstype'])
        self.edit_manage(editleavedata['managecontents'])
        self.edit_save()







