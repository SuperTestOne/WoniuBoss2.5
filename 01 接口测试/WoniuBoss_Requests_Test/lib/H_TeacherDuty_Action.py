
class TD_Action:

    def __init__(self,session):
        self.session = session

    # 指定值班动作
    def do_add_duty(self, duty_url, duty_data):
        duty_resp = self.session.post(duty_url, duty_data)
        return duty_resp

    # 查询动作
    def do_query_duty(self, query_duty_url,query_duty_data):
        duty_query = self.session.post(query_duty_url,query_duty_data)
        return duty_query.text

    # 教师值班修改动作
    def do_alter_duty(self,alter_duty_url,alter_duty_data):
        alter_duty = self.session.post(alter_duty_url,alter_duty_data)
        return alter_duty.text

# if __name__ == '__main__':
# #     a = TD_Action()
# #     a.do_add_duty()