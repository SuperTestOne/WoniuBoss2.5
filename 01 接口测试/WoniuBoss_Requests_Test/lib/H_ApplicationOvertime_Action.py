
class AOA_Action:

    def __init__(self,session):
        self.session = session

    # 新增加班申请动作
    def do_add_application(self, application_url, application_data):
        application_resp = self.session.post(application_url, application_data)
        return application_resp.text

    # 查询动作
    def do_query_application(self, query_application_url,query_application_data):
        application_query = self.session.post(query_application_url,query_application_data)
        return application_query.text

    # 撤销动作
    def do_alter_application(self,alter_application_url,alter_application_data):
        alter_application = self.session.post(alter_application_url,alter_application_data)
        return alter_application.text