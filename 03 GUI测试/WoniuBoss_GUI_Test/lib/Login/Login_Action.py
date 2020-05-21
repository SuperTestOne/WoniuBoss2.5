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