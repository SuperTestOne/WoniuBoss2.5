
class STC_Action:

    def __init__(self, session):
        self.session = session


    def do_query(self, query_url , query_method , query_data):
        return self.session.request(url=query_url, method=query_method, data=query_data)

    def do_turn_class(self, turn_class_url , turn_class_method , turn_class_data):
        return self.session.request(url=turn_class_url, method=turn_class_method, data=turn_class_data)

    def do_decode(self , decode_url , decode_method , decode_data):
        return self.session.request(url=decode_url , method=decode_method , data=decode_data)

    def do_sum_show(self , sum_show_url , sum_show_method , sum_show_data):
        return self.session.request(url=sum_show_url , method=sum_show_method , data=sum_show_data)

    def do_turn_page(self , turn_page_url , turn_page_method , turn_page_data):
        return self.session.request(url=turn_page_url, method=turn_page_method, data=turn_page_data)