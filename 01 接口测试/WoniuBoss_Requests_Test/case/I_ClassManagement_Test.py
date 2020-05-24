import unittest,warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.lib.I_ClassManagement_Action import CM_Action
from WoniuBoss_Requests_Test.tools.util import Util

class CM_Test(unittest.TestCase):

    query_conf = Util.get_json('../conf/I_CSM_Excel.conf')[0]
    query_info = Util.get_excel_zz(query_conf)


    add_conf = Util.get_json('../conf/I_CSM_Excel.conf')[1]
    add_info = Util.get_excel_zz(add_conf)


    decode_conf = Util.get_json('../conf/I_CSM_Excel.conf')[2]
    decode_info = Util.get_excel_zz(decode_conf)


    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.CM = CM_Action(Service.get_session_zz())

    @parameterized.expand(query_info)
    def test_CM_query(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        query_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        query_resp = self.CM.do_query(query_data['URL'], query_data['METHOD'],
                                              query_data['QUERYDATA'])

        # 获取json格式字符串
        contents = query_resp.json()
        # print(contents)

        contents_result = int(contents['totalRow'])
        if isinstance(contents_result, int):
            query_one_actual = 'query_pass'
        else:
            query_one_actual = 'query_fail'

        self.assertEqual(query_one_actual, query_data['EXPECT'])



    @parameterized.expand(add_info)
    def test_CM_add(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        add_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        add_resp = self.CM.do_add(add_data['URL'], add_data['METHOD'],
                                              add_data['QUERYDATA'])

        contents = add_resp.text
        # print(contents)

        if contents == "success":
            add_actual = 'add_pass'
        else:
            add_actual = 'add_fail'

        self.assertEqual(add_actual, add_data['EXPECT'])


    @parameterized.expand(decode_info)
    def test_CM_decode(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        decode_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        decode_resp = self.CM.do_decode(decode_data['URL'], decode_data['METHOD'],
                                              decode_data['QUERYDATA'])

        contents = decode_resp.text
        # print(contents)

        if contents == "yes":
            decode_actual = 'decode_pass'
        elif contents == "二级密码输入错误":
            decode_actual = 'decode_fail'
        else:
            decode_actual = 'other_error'

        self.assertEqual(decode_actual, decode_data['EXPECT'])



if __name__ == '__main__':
    unittest.main(verbosity=2)