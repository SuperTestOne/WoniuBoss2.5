import unittest,warnings
from parameterized import parameterized

from WoniuBoss_Requests_Test.lib.I_StudentLevae_Action import SL_Action
from WoniuBoss_Requests_Test.tools.util import Util

class SL_Test(unittest.TestCase):

    query_conf = Util.get_json('../conf/I_CSM_Excel.conf')[7]
    query_info = Util.get_excel_zz(query_conf)

    add_conf = Util.get_json('../conf/I_CSM_Excel.conf')[8]
    add_info = Util.get_excel_zz(add_conf)

    decode_conf = Util.get_json('../conf/I_CSM_Excel.conf')[9]
    decode_info = Util.get_excel_zz(decode_conf)

    del_lev_conf = Util.get_json('../conf/I_CSM_Excel.conf')[10]
    del_lev_info = Util.get_excel_zz(del_lev_conf)

    edit_conf = Util.get_json('../conf/I_CSM_Excel.conf')[11]
    edit_info = Util.get_excel_zz(edit_conf)

    sum_show_conf = Util.get_json('../conf/I_CSM_Excel.conf')[12]
    sum_show_info = Util.get_excel_zz(sum_show_conf)

    turn_page_conf = Util.get_json('../conf/I_CSM_Excel.conf')[13]
    turn_page_info = Util.get_excel_zz(turn_page_conf)





    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.SL = SL_Action(Service.get_session_zz())

    @parameterized.expand(query_info)
    def test_SSI_query(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        query_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        query_resp = self.SL.do_query(query_data['URL'], query_data['METHOD'],
                                              query_data['QUERYDATA'])

        contents = query_resp.json()

        if len(contents['list']) > 0:
            query_actual = 'query_pass'
        elif len(contents['list']) == 0:
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        self.assertEqual(query_actual, query_data['EXPECT'])


    @parameterized.expand(add_info)
    def test_CM_add(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        add_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        add_resp = self.SL.do_add(add_data['URL'], add_data['METHOD'],
                                              add_data['QUERYDATA'])

        contents = add_resp.text

        if contents == "success":
            add_actual = 'add_pass'
        else:
            add_actual = 'add_fail'

        self.assertEqual(add_actual, add_data['EXPECT'])



    @parameterized.expand(decode_info)
    def test_SSI_decode(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        decode_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        decode_resp = self.SL.do_decode(decode_data['URL'], decode_data['METHOD'],
                                              decode_data['QUERYDATA'])

        contents = decode_resp.text

        if contents == "yes":
            decode_actual = 'decode_pass'
        elif contents == "二级密码输入错误":
            decode_actual = 'decode_fail'
        else:
            decode_actual = 'other_error'

        self.assertEqual(decode_actual, decode_data['EXPECT'])


    @parameterized.expand(del_lev_info)
    def test_CM_del_lev(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        del_lev_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        del_lev_resp = self.SL.do_del_lev(del_lev_data['URL'], del_lev_data['METHOD'],
                                              del_lev_data['QUERYDATA'])

        contents = del_lev_resp.text

        if contents == "success":
            del_lev_actual = 'del_lev_pass'
        else:
            del_lev_actual = 'del_lev_fail'

        self.assertEqual(del_lev_actual, del_lev_data['EXPECT'])


    @parameterized.expand(edit_info)
    def test_CM_edit(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        edit_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        edit_resp = self.SL.do_edit(edit_data['URL'], edit_data['METHOD'], edit_data['QUERYDATA'])

        contents = edit_resp.text

        if contents == "success":
            edit_actual = 'edit_pass'
        else:
            edit_actual = 'edit_fail'

        self.assertEqual(edit_actual, edit_data['EXPECT'])


    @parameterized.expand(sum_show_info)
    def test_SSI_sum_show(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        sum_show_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        sum_show_resp = self.SL.do_sum_show(sum_show_data['URL'], sum_show_data['METHOD'],
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

        turn_page_resp = self.SL.do_turn_page(turn_page_data['URL'], turn_page_data['METHOD'],
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