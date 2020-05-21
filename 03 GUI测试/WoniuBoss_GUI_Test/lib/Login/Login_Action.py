from WoniuBoss_GUI_Test.tools.service import Service
from WoniuBoss_GUI_Test.tools.util import Util
from WoniuBoss_GUI_Test.bin.Start.start import start

class L_Action:

    def __init__(self,driver):
        self.driver = driver
        self.ele = Util.get_json('..\\..\\conf\\Login_Conf\\L_Element.conf')

    #完成登录动作
    def do_login(self,username,userpass):
        Service.input_motion(self.driver,"name",self.ele[0]["username_name"],username)
        Service.input_motion(self.driver,"name",self.ele[0]["userpass_name"],userpass)
        Service.click_motion(self.driver,"xpath",self.ele[0]["blank_xpath"])
        Service.click_motion(self.driver,"xpath",self.ele[0]["login_xpath"])
        
# ================================================================================================
    # 詹正
    #输入用户名
    def input_username(self,username):
        un = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div/div[1]/input")
        Service.send_input(un,username)

    #输入密码
    def input_userpass(self,userpass):
        up = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div/div[2]/input")
        Service.send_input(up,userpass)

    #点击登陆按钮
    def click_login(self):
        cl = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/div[2]/button")
        cl.click()

    #点击取消保存
    def click_blank(self):
        cb = self.driver.find_element_by_xpath("/html/body/div[1]/div/div/form/div/div[4]/input[1]")
        cb.click()

    #点击解密按钮
    def click_decode(self):
        import time
        time.sleep(5)
        self.driver.find_element_by_id('btn-decrypt').click()

    #输入二级密码
    def input_secondary_password(self,password):
        isp = self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[2]/input')
        Service.send_input(isp, password)

    #点击确定解密按钮
    def click_confirm_decode(self):
        import time
        time.sleep(1)
        self.driver.find_element_by_xpath('/html/body/div[12]/div/div/div[3]/button').click()

    def new_do_login(self, username, userpass):
        self.input_username(username)
        self.input_userpass(userpass)
        self.click_blank()
        self.click_login()


# ================================================================================================