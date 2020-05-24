class Util:

    # 读取json配置文件,需要传入路径
    @classmethod
    def get_json(cls, path):
        import json
        with open(path, encoding="utf-8") as op:
            contents = json.load(op)
        return contents

    #获取Excel里需要的数据
    @classmethod
    def get_excel(cls, conf):
        import xlrd,ast
        test_info = []
        workbook = xlrd.open_workbook(conf['TESTINFO_PATH'])
        contents = workbook.sheet_by_name(conf['SHEETNAME'])
        for i in range(conf['START_ROW'], conf['END_ROW']):
            test_url = contents.cell(i, conf['TESTURL_COL']).value
            test_data = contents.cell(i, conf['TESTDATA_COL']).value
            expect = contents.cell(i, conf['EXPECT_COL']).value
            data = ast.literal_eval(test_data)
            list = []
            list.append(test_url)
            list.append(data)
            list.append(expect)
            info = tuple(list)
            test_info.append(info)
            # temp = test_data.split('\n')
            # dict = {}
            # for j in temp:
            #     dict[j.split('=')[0]] = j.split('=')[1]
            # list = []
            # list.append(test_url)
            # list.append(dict)
            # list.append(expect)
            # info = tuple(list)
            # test_info.append(info)
        return test_info

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

    #获取当前系统时间
    @classmethod
    def get_ctime(cls):
        import time
        ctime = time.strftime('%Y-%m-%d_%H-%M-%S', time.localtime())
        return ctime
        
# =========================================================================================
    # 詹正
    # 获取Excel里需要的数据
    @classmethod
    def get_excel_zz(cls, conf):
        import xlrd, ast
        test_info = []
        workbook = xlrd.open_workbook(conf['TESTINFO_PATH'])
        contents = workbook.sheet_by_name(conf['SHEETNAME'])
        for i in range(conf['START_ROW'], conf['END_ROW']):
            test_url = contents.cell(i, conf['URL_COL']).value
            method = contents.cell(i, conf['METHOD_COL']).value
            test_data = contents.cell(i, conf['TESTDATA_COL']).value
            expect = contents.cell(i, conf['EXPECT_COL']).value
            data = ast.literal_eval(test_data)
            list = []
            list.append(test_url)
            list.append(method)
            list.append(data)
            list.append(expect)
            info = tuple(list)
            test_info.append(info)
        return test_info


# =========================================================================================