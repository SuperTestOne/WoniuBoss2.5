class CR_Action:

    def __init__(self,session):
        self.session = session

    #完成查询动作
    def do_query(self,query_url,query_data):
        query_resp = self.session.post(query_url,query_data)
        return query_resp.json()

    #完成认领动作
    def do_claim(self,claim_url,claim_data):
        claim_resp = self.session.post(claim_url,claim_data)
        return claim_resp.text


