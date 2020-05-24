class DR_Action:

    def __init__(self,session):
        self.session = session

    #完成查询动作
    def do_query(self,query_url,query_data):
        query_resp = self.session.post(query_url,query_data)
        return query_resp.json()

    #完成转交动作
    def do_deliver(self,deliver_url,deliver_data):
        deliver_resp = self.session.post(deliver_url,deliver_data)
        return deliver_resp.text