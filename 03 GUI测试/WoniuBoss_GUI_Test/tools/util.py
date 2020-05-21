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

# ================================================================================================
    # 詹正
    # 从测试数据配置文件中读取测试数据内容,返回json格式数据
    @classmethod
    def get_excel_zz(cls, conf):

        # 获取配置信息
        # testinfo_conf = cls.get_json(path)
        # conf = testinfo_conf[index]
        import xlrd
        # 将excel读取到内存中,返回workbook对象
        workbook = xlrd.open_workbook(conf['TESTINFO_PATH'])
        # 可以通过下标获取sheet页对象，下标从0开始
        # workbook.sheet_by_index(0)
        # 可以通过sheet页的名字返回sheet页对象
        contents = workbook.sheet_by_name(conf['SHEETNAME'])
        # 定义空列表用于存储测试信息
        testinfo = []
        # 通过sheet页对象读取其内容
        for i in range(conf['START_ROW'], conf['END_ROW']):
            testdata = contents.cell(i, conf['TESTDATA_COL']).value
            expect = contents.cell(i, conf['EXPECT_COL']).value
            # 使用换行符作为分隔符
            temp = testdata.split('\n')
            # 定义字典用于存放每一项测试数据
            tup = {}
            for t in temp:
                # 给字典添加元素
                tup[t.split('=')[0]] = t.split('=')[1]
            # 在字典中添加期望结果的元素
            tup['expect'] = expect
            testinfo.append(tup)
        return testinfo                #返回列表套元组

    # 把从excle中读取的结果[{},{}]转化成[(),()]
    @classmethod
    def get_excel_to_tuple(cls, xls_file_info):
        result = cls.get_excel_zz(xls_file_info)
        li = []
        for di in result:
            # 通过tuple(dict.values())转化成元组
            tup = tuple(di.values())
            li.append(tup)
        return li

# ================================================================================================



