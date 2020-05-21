#封装不操作软件的工具类
class Util:

    #读取json文件
    @classmethod
    def get_json(cls,path):
        import json
        with open(path,encoding="utf-8") as op:
            contents = json.load(op)
        return contents

    @classmethod
    def get_excel(cls,conf):
        import xlrd                                                     #导入xlrd模块,用于读取excel文件
        test_info = []                                                  #定义空列表,用于存储总测试数据
        workbook = xlrd.open_workbook(conf['TESTINFO_PATH'])#读取excel文件,路径为conf['TESTINFO_PATH']
        contents = workbook.sheet_by_name(conf['SHEETNAME'])            #根据名字读取excel文件中的子表格
        for i in range(conf['START_ROW'],conf['END_ROW']):              #遍历表格,从开始下标到结束下标
            test_data = contents.cell(i,conf['TESTDATA_COL']).value     #获取表格中的TESTDATA_COL列
            expect = contents.cell(i,conf['EXPECT_COL']).value          #获取表格中的TEXPECT_COL列
            temp = test_data.split('\n')                                #读取出来的该列数据为字符串,需要进行切割
            list = []
            for j in temp:
                list.append(j.split('=')[1])
            list.append(expect)
            test_info.append(tuple(list))
        return test_info                                                #返回列表套元组

    # 获取需要测试的类的路径
    @classmethod
    def get_path(cls, path):
        list = []
        with open(path, encoding="utf-8") as op:
            str_list = op.readlines()
        for str in str_list:
            if not str.strip().startswith("#"):
                list.append(str.strip())
        return list

    #计算差值
    @classmethod
    def compute_value(cls,old_num,new_num):
        if int(old_num) >= int(new_num):
            num = int(old_num) - int(new_num)
        else:
            num = int(new_num) - int(old_num)
        return num

    # 获取当前系统时间
    @classmethod
    def get_ctime(cls):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        return ctime





