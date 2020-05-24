import unittest,warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.lib.I_StudentTurnClass_Action import STC_Action
from WoniuBoss_Requests_Test.tools.util import Util

class STC_Test(unittest.TestCase):

    query_conf = Util.get_json('../conf/I_CSM_Excel.conf')[14]
    query_info = Util.get_excel_zz(query_conf)

    turn_class_conf = Util.get_json('../conf/I_CSM_Excel.conf')[15]
    turn_class_info = Util.get_excel_zz(turn_class_conf)

    decode_conf = Util.get_json('../conf/I_CSM_Excel.conf')[16]
    decode_info = Util.get_excel_zz(decode_conf)

    sum_show_conf = Util.get_json('../conf/I_CSM_Excel.conf')[17]
    sum_show_info = Util.get_excel_zz(sum_show_conf)

    turn_page_conf = Util.get_json('../conf/I_CSM_Excel.conf')[18]
    turn_page_info = Util.get_excel_zz(turn_page_conf)


    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.STC = STC_Action(Service.get_session_zz())

    @parameterized.expand(query_info)
    def test_SSI_query(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        query_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        query_resp = self.STC.do_query(query_data['URL'], query_data['METHOD'],
                                              query_data['QUERYDATA'])

        contents = query_resp.json()

        if len(contents['list']) > 0:
            query_actual = 'query_pass'
        elif len(contents['list']) == 0:
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        self.assertEqual(query_actual, query_data['EXPECT'])


    @parameterized.expand(turn_class_info)
    def test_CM_turn_class(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        turn_class_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        turn_class_resp = self.STC.do_turn_class(turn_class_data['URL'], turn_class_data['METHOD'],
                                                 turn_class_data['QUERYDATA'])

        contents = turn_class_resp.text

        if contents == "success":
            turn_class_actual = 'turn_class_pass'
        else:
            turn_class_actual = 'turn_class_fail'

        self.assertEqual(turn_class_actual, turn_class_data['EXPECT'])


    @parameterized.expand(decode_info)
    def test_SSI_decode(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        decode_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        decode_resp = self.STC.do_decode(decode_data['URL'], decode_data['METHOD'],
                                              decode_data['QUERYDATA'])

        contents = decode_resp.text

        if contents == "yes":
            decode_actual = 'decode_pass'
        elif contents == "二级密码输入错误":
            decode_actual = 'decode_fail'
        else:
            decode_actual = 'other_error'

        self.assertEqual(decode_actual, decode_data['EXPECT'])

    @parameterized.expand(sum_show_info)
    def test_SSI_sum_show(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        sum_show_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        sum_show_resp = self.STC.do_sum_show(sum_show_data['URL'], sum_show_data['METHOD'],
                                              sum_show_data['QUERYDATA'])

        contents = sum_show_resp.json()

        if len(contents['list']) > 0:
            sum_show_actual = 'sum_show_pass'
        elif len(contents['list']) == 0:
            sum_show_actual = 'sum_show_pass'
        else:
            sum_show_actual = 'sum_show_fail'

        self.assertEqual(sum_show_actual, sum_show_data['EXPECT'])


    @parameterized.expand(turn_page_info)
    def test_SSI_turn_page(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        turn_page_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        turn_page_resp = self.STC.do_turn_page(turn_page_data['URL'], turn_page_data['METHOD'],
                                              turn_page_data['QUERYDATA'])

        contents = turn_page_resp.json()

        if len(contents['list']) > 0:
            turn_page_actual = 'turn_page_pass'
        elif len(contents['list']) == 0:
            turn_page_actual = 'turn_page_pass'
        else:
            turn_page_actual = 'turn_page_fail'

        self.assertEqual(turn_page_actual, turn_page_data['EXPECT'])




if __name__ == '__main__':
    unittest.main()
