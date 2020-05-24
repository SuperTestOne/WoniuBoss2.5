class TR_Action:

    def __init__(self,session):
        self.session = session

    #查询动作
    def do_query(self,query_url,query_data):
        query_resp = self.session.post(query_url,query_data)
        return query_resp.json()

    #完成新增动作
    def do_add(self,add_url, add_data):
        add_resp = self.session.post(add_url, add_data)
        return add_resp.text

    #完成修改动作
    def do_edit(self,edit_url, edit_data):
        edit_resp = self.session.post(edit_url, edit_data)
        return edit_resp.text

    #完成跟踪动作
    def do_track(self,track_url, track_data):
        track_resp = self.session.post(track_url, track_data)
        return track_resp.text

    #完成废弃动作
    def do_abandon(self,abandon_url,abandon_data):
        abandon_resp = self.session.post(abandon_url,abandon_data)
        return abandon_resp.text
