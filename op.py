import db.db as db

class operations:
    def __init__(self):
        self.db = db.DB()
    def login(self, user, passward):
        sql = "use Library_management_system; select password from students where sid = '%s'"%(user)
        t_passward = self.db.query_sql(sql)
        if t_passward != passward:
            return False
        else :
            self.user = user
            return True
    # def insert_book(self, book, )