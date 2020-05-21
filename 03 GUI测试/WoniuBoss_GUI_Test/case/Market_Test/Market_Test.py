# encoding: utf-8
# @author: yinqianjun
# @file: Market_Test.py
# @time: 2020/5/18 15:07
import unittest,time
from WoniuBoss_GUI_Test.lib.Market.Market_Action import Market
from WoniuBoss_GUI_Test.tools.util import Util
from parameterized import parameterized
from WoniuBoss_GUI_Test.tools.service import Service
class Market_Test(unittest.TestCase):

    def setUp(self) -> None:
        self.driver = Service.get_driver()
    def tearDown(self) -> None:
        self.driver.close()

    #获取需要添加的数据
    add_conf = Util.get_json('../../conf/Market_Conf/Market_Excel.conf')[0]
    add_data = Util.get_excel(add_conf)
    # print(add_data)
    @parameterized.expand(add_data)
    #新增资源测试
    def test_add_resource(self,phone,name,age,area,partment,education,eduexp,experience
                          ,sex,school,source,status,workage,wx,qq,major,expect):
        add_info ={'phone':phone,'name':name,'age':age,'area':area,'partment':partment,'education':education
                   ,'eduexp':eduexp,'experience':experience,'sex':sex,'school':school,'source':source,
                   'status':status,'workage':workage,'wx':wx,'qq':qq,'major':major,'expect':expect}
        if Market(self.driver).add_resource(add_info) == True:
            actual = 'add-success'
        else:
            actual = 'add-fail'

        self.assertEqual(actual, expect)

    # 获取需要查询的测试数据
    search_conf = Util.get_json('../../conf/Market_Conf/Market_Excel.conf')[1]
    search_data= Util.get_excel(search_conf)
    # print(search_data)
    @parameterized.expand(search_data)
    def test_search_resource(self,value,expect):
        search_info = {'value':value,'expect':expect}

        if Market(self.driver).search_resource(search_info)==True:
            actual = 'search-success'
        else:
            actual = 'search-fail'
        self.assertEqual(actual, expect)

    # 获取需要上传简历的测试数据
    upload_conf = Util.get_json('../../conf/Market_Conf/Market_Excel.conf')[2]
    upload_data= Util.get_excel(upload_conf)
    # print(upload_data)
    @parameterized.expand(upload_data)
    def test_upload_resource(self, path, area,partment,expect):
        upload_info = {'path':path,'area':area,'partment':partment,'expect':expect}
        msg = Market(self.driver).upload_resource(upload_info)
        if '总共上传' in msg:
            actual = 'upload-success'
        else:
            actual = 'upload-fail'

        self.assertEqual(actual, expect)

if __name__ == '__main__':
    unittest.main()