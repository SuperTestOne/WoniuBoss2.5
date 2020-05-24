
class TI_Action:

    def __init__(self,session):
        self.session = session

    # 技术面试搜索动作
    def do_query_interview(self, query_interview_url,query_interview_data):
        course_query = self.session.post(query_interview_url,query_interview_data)
        return course_query.text

    # 技术面试动作
    def do_add_interview(self,alter_interview_url,alter_interview_data):
        alter_course = self.session.post(alter_interview_url,alter_interview_data)
        return alter_course.text