

class SL_Action:

    def __init__(self, session):
        self.session = session


    def do_query(self, query_url , query_method , query_data):
        return self.session.request(url=query_url, method=query_method, data=query_data)


    def do_add(self , add_url , add_method , add_data):
        return self.session.request(url=add_url , method=add_method , data=add_data)

    def do_decode(self , decode_url , decode_method , decode_data):
        return self.session.request(url=decode_url , method=decode_method , data=decode_data)

    def do_del_lev(self , del_lev_url , del_lev_method , del_lev_data):
        return self.session.request(url=del_lev_url , method=del_lev_method , data=del_lev_data)

    def do_edit(self , edit_url , edit_method , edit_data):
        return self.session.request(url=edit_url , method=edit_method , data=edit_data)

    def do_sum_show(self , sum_show_url , sum_show_method , sum_show_data):
        return self.session.request(url=sum_show_url , method=sum_show_method , data=sum_show_data)

    def do_turn_page(self , turn_page_url , turn_page_method , turn_page_data):
        return self.session.request(url=turn_page_url, method=turn_page_method, data=turn_page_data)