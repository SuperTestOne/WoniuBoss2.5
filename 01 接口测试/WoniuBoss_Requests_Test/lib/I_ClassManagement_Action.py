



class CM_Action:

    def __init__(self , session):
        self.session = session


    def do_query(self , query_url , query_method , query_data):
        return self.session.request(url=query_url , method=query_method , data=query_data)

    def do_add(self , add_url , add_method , add_data):
        return self.session.request(url=add_url , method=add_method , data=add_data)

    def do_decode(self , decode_url , decode_method , decode_data):
        return self.session.request(url=decode_url , method=decode_method , data=decode_data)
