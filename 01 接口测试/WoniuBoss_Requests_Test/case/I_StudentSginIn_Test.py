import unittest,warnings
from parameterized import parameterized
from WoniuBoss_Requests_Test.lib.I_StudentSginIn_Action import SSI_Action
from WoniuBoss_Requests_Test.tools.util import Util

class SSI_Test(unittest.TestCase):

    query_conf = Util.get_json('../conf/I_CSM_Excel.conf')[3]
    query_info = Util.get_excel_zz(query_conf)

    ssi_conf = Util.get_json('../conf/I_CSM_Excel.conf')[4]
    ssi_info = Util.get_excel_zz(ssi_conf)

    Batch_ssi_conf = Util.get_json('../conf/I_CSM_Excel.conf')[5]
    Batch_ssi_info = Util.get_excel_zz(Batch_ssi_conf)

    decode_conf = Util.get_json('../conf/I_CSM_Excel.conf')[6]
    decode_info = Util.get_excel_zz(decode_conf)


    def setUp(self):
        from WoniuBoss_Requests_Test.tools.service import Service
        self.SSI = SSI_Action(Service.get_session_zz())

    @parameterized.expand(query_info)
    def test_SSI_query(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        query_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        query_resp = self.SSI.do_SSI_query(query_data['URL'], query_data['METHOD'],
                                              query_data['QUERYDATA'])

        contents = query_resp.json()

        if len(contents['list']) > 0:
            query_actual = 'query_pass'
        elif len(contents['list']) == 0:
            query_actual = 'query_pass'
        else:
            query_actual = 'query_fail'

        self.assertEqual(query_actual, query_data['EXPECT'])



    @parameterized.expand(ssi_info)
    def test_ssi(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        ssi_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        ssi_resp = self.SSI.do_SSI_query(ssi_data['URL'], ssi_data['METHOD'],
                                              ssi_data['QUERYDATA'])

        contents = ssi_resp.text

        if contents == 'success':
            ssi_actual = 'ssi_pass'
        else:
            ssi_actual = 'ssi_fail'

        self.assertEqual(ssi_actual, ssi_data['EXPECT'])




    @parameterized.expand(Batch_ssi_info)
    def test_Batch_ssi(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        Batch_ssi_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        Batch_ssi_resp = self.SSI.do_SSI_query(Batch_ssi_data['URL'], Batch_ssi_data['METHOD'],
                                              Batch_ssi_data['QUERYDATA'])

        contents = Batch_ssi_resp.text

        if contents == 'success':
            Batch_ssi_actual = 'Batch_ssi_pass'
        else:
            Batch_ssi_actual = 'Batch_ssi_fail'

        self.assertEqual(Batch_ssi_actual, Batch_ssi_data['EXPECT'])


    @parameterized.expand(decode_info)
    def test_SSI_decode(self, url, method , data, expect):
        warnings.simplefilter('ignore', ResourceWarning)

        decode_data = {'URL': url, 'METHOD':method, 'QUERYDATA': data, 'EXPECT': expect}

        decode_resp = self.SSI.do_decode(decode_data['URL'], decode_data['METHOD'],
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