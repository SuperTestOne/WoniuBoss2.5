


class CA_Action:

    def __init__(self,session):
        self.session = session

    # 新增排课动作
    def do_add_course(self, course_url, course_data):
        course_resp = self.session.post(course_url, course_data)
        return course_resp.text

    # 课程安排查询动作
    def do_query_course(self, query_course_url,query_course_data):
        course_query = self.session.post(query_course_url,query_course_data)
        return course_query.text

    # 课程安排修改动作
    def do_alter_course(self,alter_course_url,alter_course_data):
        alter_course = self.session.post(alter_course_url,alter_course_data)
        return alter_course.text
