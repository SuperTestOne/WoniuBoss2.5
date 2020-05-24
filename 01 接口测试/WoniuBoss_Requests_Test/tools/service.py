class Service:
    #获取cookie
    @classmethod
    def get_session(cls):
        import requests
        from WoniuBoss_GUI_Test.tools.util import Util
        contents = Util.get_json('..\\conf\\base.conf')[0]
        session = requests.session()
        session.post(contents["login_url"], contents["login_data"])
        return session
        

# ========================================================================
    # 詹正
    #获取cookie
    @classmethod
    def get_session_zz(cls):
        import requests
        from WoniuBoss_GUI_Test.tools.util import Util
        contents = Util.get_json('..\\conf\\base.conf')[1]
        session = requests.session()
        session.post(contents["login_url"], contents["login_data"])
        return session
# ========================================================================