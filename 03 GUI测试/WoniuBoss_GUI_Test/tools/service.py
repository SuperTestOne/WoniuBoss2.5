from WoniuBoss_GUI_Test.tools.util import Util
from selenium.webdriver.support.select import Select
from selenium.webdriver.support.wait import WebDriverWait

#封装操作软件的工具类
class Service:

    #点击、清理、输入,需要传入元素对象和输入的内容
    @classmethod
    def send_input(cls,ele,value):
            ele.click()
            ele.clear()
            ele.send_keys(value)

    #获取软件网址,需要传入元素对象和网址配置文件路径
    @classmethod
    def open_page(cls,driver):
        contents = Util.get_json("..\\..\\conf\\base.conf")[0]
        url = f"{contents['PROTOCOL']}://{contents['IP']}:{contents['PORT']}/{contents['PROGRAM']}"
        driver.get(url)

    # 获取driver
    @classmethod
    def get_driver(cls):
        from selenium import webdriver
        contents = Util.get_json("..\\..\\conf\\base.conf")[0]
        driver = getattr(webdriver, contents['BROWSER'])()
        driver.implicitly_wait(10)
        return driver

    #查询元素是否存在
    @classmethod
    def is_element_present(cls, driver, how, what):
        from selenium.common.exceptions import NoSuchElementException
        try:
            driver.find_element(by=how, value=what)
        except NoSuchElementException as e:
            return False
        return True

    #截取图片,需要传入元素对象和存储路径
    @classmethod
    def get_png(cls, driver, path):
        WebDriverWait(driver, 10, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body").text)
        driver.get_screenshot_as_file(path)

    #测试失败时截取图片,需要传入元素对象
    @classmethod
    def get_error_png(cls,driver):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S',time.localtime())
        screenshot_path = f"..\\..\\img\\fail{ctime}.png"
        cls.get_png(driver,screenshot_path)

    #获取页面信息
    @classmethod
    def get_hint(cls,driver,xpath):
        global msg
        try:
            WebDriverWait(driver, 10, 0.5).until(lambda driver: driver.find_element_by_xpath("/html/body").text)
            msg = driver.find_element_by_xpath(xpath).text
        except Exception:
            msg = ""
        finally:
            return msg

    # 根据当前页面列表总数,生成随机数
    @classmethod
    def random_delete(cls,driver,xpath):
        import random,re
        msg = cls.get_hint(driver,xpath)
        number = int(re.findall(r'共(.*?)条', msg)[0])
        if number >= 10:
            number = 10
        randnum = random.randint(1, number)
        return randnum

    #登录,解码并打开模块
    @classmethod
    def open_module_connect(cls,driver,ele):
        from WoniuBoss_GUI_Test.lib.Login.Login_Action import L_Action
        ele2 = Util.get_json("..\\..\\conf\\Login_Conf\\L_Element.conf")
        #登录
        L_Action(driver).do_login(ele["username"],ele["userpass"])
        #输入二级密码
        cls.click_motion(driver,"xpath",ele2[0]["decode_xpath"])
        cls.input_motion(driver,"xpath",ele2[0]["secondary_password_xpath"],ele["secondary_password"])
        cls.click_motion(driver,"xpath",ele2[0]["confirm_decode_xpath"])
        #点击大模块
        driver.find_element_by_xpath(ele["big_module"]).click()
        #点击子模块
        driver.find_element_by_xpath(ele["small_module"]).click()

    #点击的动作,需要传入元素,值
    @classmethod
    def click_motion(cls,driver,how,what):
        driver.find_element(by=how, value=what).click()

    #输入值的动作,需要传入元素,值以及需要输入的值
    @classmethod
    def input_motion(cls,driver,how,what,value):
        im = driver.find_element(by=how, value=what)
        im.click()
        im.clear()
        im.send_keys(value)

    #选择的动作,需要传入元素,值以及需要选择的值
    @classmethod
    def select_motion(cls,driver,how,what,value):
        sm = driver.find_element(by=how, value=what)
        Select(sm).select_by_visible_text(value)
#***************殷*****************#
    # 从文本中读取内容
    @classmethod
    def get_txt(cls, path):
        with open(path, encoding='utf8') as file:
            contents = file.readlines()
        return contents
    #只做登录操作
    @classmethod
    def only_login(cls,driver):
        username = driver.find_element_by_name("userName")
        username.click()
        username.send_keys('wncd000')
        pword = driver.find_element_by_name("userPass")
        pword.click()
        pword.send_keys('woniu123')
        driver.find_element_by_xpath('/html/body/div[1]/div/div/div[2]/button').click()

    #点击进入某个模块
    @classmethod
    def into_module(cls,driver,moduleName):
        driver.find_element_by_link_text(moduleName).click()

    # 根据下拉框的值选择
    @classmethod
    def droplist(cls, ele, value):
        from selenium.webdriver.support.ui import Select
        Select(ele).select_by_visible_text(value)

#***************殷*****************#

# ================================================================================================
    # 詹正
    #登录并打开模块
    @classmethod
    def open_module_connect_zz(cls,driver,info):
        from WoniuBoss_GUI_Test.lib.Login.Login_Action import L_Action
        #登录
        L_Action(driver).new_do_login(info[0],info[1])
        L_Action(driver).click_decode()
        L_Action(driver).input_secondary_password(info[2])
        L_Action(driver).click_confirm_decode()
        #点击大模块
        driver.find_element_by_xpath(info[3]).click()
        #点击子模块
        driver.find_element_by_xpath(info[4]).click()

# ================================================================================================