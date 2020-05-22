# 课程安排
from WoniuBoss_GUI_Test.tools.service import Service
class Cour:

    def __init__(self, driver):
        self.driver = driver
    # 选择讲师下拉框中的内容
    def select_lect(self, value):
        lect = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[1]/select')
        Service.select_value(lect, value)

    # 选择教室下拉框中的内容
    def select_classr(self,value):
        classr = self.driver.find_element_by_xpath('//*[@id="addCourse-table"]/tr/td[2]/select')
        Service.select_value(classr,value)

    # 选择班号下拉框中的内容
    def select_code(self,value):
        code = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/form/div[2]/table/tbody/tr/td[3]/select')
        Service.select_value(code,value)

    # 选择课程安排下拉框中的内容
    def select_course(self,value):
        course = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/div[2]/form/div[2]/table/tbody/tr/td[4]/select')
        Service.select_value(course,value)

    # 选择校区下拉框中的内容
    def select_campus(self,value):
        camp = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[1]/select[1]')
        Service.select_value(camp,value)

    # 选择讲师下拉框中的内容
    def select_teacher(self,value):
        teac = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[1]/select[2]')
        Service.select_value(teac,value)

    # 选择方向下拉框中的内容
    def select_direc(self,value):
        direc = self.driver.find_element_by_xpath('/html/body/div[8]/div[2]/div/div[1]/select[3]')
        Service.select_value(direc,value)

    # 选择修改讲师下拉框中的内容
    def select_altertear(self,value):
        altert = self.driver.find_element_by_xpath('/html/body/div[15]/div/div/form/div/div/div[3]/select')
        Service.select_value(altert,value)


    # 输入查询开始时间
    def input_start_time(self,stime):
        js1 = f"document.querySelector('#course > div.col-lg-12.col-md-12.col-sm-12.col-xs-12.con-body-padding.text-left > input:nth-child(8)').removeAttribute('text/javascript');"
        self.driver.execute_script(js1)
        js_value1 = 'document.querySelector("#course > div.col-lg-12.col-md-12.col-sm-12.col-xs-12.con-body-padding.text-left 'f'> input:nth-child(8)").value="{stime}"'
        self.driver.execute_script(js_value1)

    # 输入查询结束时间
    def input_endtime_time(self, etime):
        js2 = f"document.querySelector('#course > div.col-lg-12.col-md-12.col-sm-12.col-xs-12.con-body-padding.text-left > input:nth-child(9)').removeAttribute('text/javascript');"
        self.driver.execute_script(js2)
        js_value2 = 'document.querySelector("#course > div.col-lg-12.col-md-12.col-sm-12.col-xs-12.con-body-padding.text-left 'f'> input:nth-child(9)").value="{etime}"'
        self.driver.execute_script(js_value2)

    # 点击保存按钮
    def click_save_button(self):
        self.driver.find_element_by_xpath('//*[@id="course-add"]/div/div/div[3]/button').click()

    # 点击排课按钮
    def click_lesson_button(self):
        self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/button[2]').click()

    # 点击查询按钮
    def click_query_button(self):
        self.driver.find_element_by_xpath('//*[@id="course"]/div[1]/button[1]').click()

    # 点击修改按钮
    def click_alter_button(self):
        self.driver.find_element_by_xpath('//*[@id="course_table"]/tbody/tr[1]/td[9]/button').click()

    # 点击修改保存按钮
    def click_altersave_button(self):
        self.driver.find_element_by_xpath('//*[@id="modifyCourse"]/div/div/div[2]/button').click()

    # 随机点击修改按钮
    def click_random_alter_button(self):
        number = Service.random_delete(self.driver,"/html/body/div[8]/div[2]/div/div[2]/div[2]/div[4]/div[1]/span[1]")
        self.driver.find_element_by_xpath(f'//*[@id="course_table"]/tbody/tr[{number}]/td[9]/button').click()


    # 输入新增排课开始时间
    def input_star_time(self,starttime):
        js = f"document.querySelector('#addcourse > div.row > div:nth-child(1) > input').removeAttribute('text/javascript');"
        self.driver.execute_script(js)
        js_value = 'document.querySelector("#addcourse > div.row 'f'> div:nth-child(1) > input").value="{starttime}"'
        self.driver.execute_script(js_value)

    # 输入新增排课开始时间
    def input_end_time(self,endtime):
        js1 = f"document.querySelector('#addcourse > div.row > div:nth-child(2) > input').removeAttribute('text/javascript');"
        self.driver.execute_script(js1)
        js_value1 = 'document.querySelector("#addcourse > div.row 'f'> div:nth-child(2) > input").value="{endtime}"'
        self.driver.execute_script(js_value1)

    # 获取操作之后的提示信息
    def get_msg(self):
        return self.driver.find_element_by_xpath('/html/body/div[16]/div/div/div[2]/div').text


    # 完成排课动作
    def do_course(self,cour_info):
        self.click_lesson_button()
        import time
        time.sleep(10)
        self.select_lect(cour_info[0])
        self.select_classr(cour_info[1])
        self.select_code(cour_info[2])
        self.select_course(cour_info[3])
        self.input_star_time(cour_info[4])
        self.input_end_time(cour_info[5])
        self.click_save_button()
    # 完成查询动作
    def do_query(self,que_info):
        self.select_campus(que_info[0])
        self.select_teacher(que_info[1])
        self.select_direc(que_info[2])
        self.input_start_time(que_info[3])
        self.input_endtime_time(que_info[4])
        self.click_query_button()

    # 完成修改动作
    # def do_alter(self,alt_info):
    #     self.click_random_alter_button()
    #     import time
    #     time.sleep(10)
    #     self.select_altertear(alt_info[0])
    #     self.click_altersave_button()
