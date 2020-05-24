

class SSI_Action:

    def __init__(self, session):
        self.session = session


    def do_SSI_query(self, query_url , query_method , query_data):
        return self.session.request(url=query_url , method=query_method , data=query_data)


    def do_ssi(self , ssi_url , ssi_method , ssi_data):
        return self.session.request(url=ssi_url, method=ssi_method, data=ssi_data)

    def do_decode(self , decode_url , decode_method , decode_data):
        return self.session.request(url=decode_url , method=decode_method , data=decode_data)
