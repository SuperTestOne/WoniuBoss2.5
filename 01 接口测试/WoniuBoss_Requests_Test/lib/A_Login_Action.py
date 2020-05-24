class L_Action:

    def __init__(self,session):
        self.session = session

    #登录动作
    def do_login(self,login_url,login_data):
        login_resp = self.session.post(login_url, login_data)
        return login_resp.text
