import pymysql

class DB:
    def __init__(self):
        self.connect = pymysql.connect(
            host = '127.0.0.1',
            port = 3306,
            user = 'zerokei',
            passwd = '123456',
            db='Library_management_system',
            charset = 'utf8')
        self.cur = self.connect.cursor()
    def query_sql(self, sql):
        self.cur.execute(sql)
        message = self.cur.fetchall()
        return message

    def update_sql(self, sql):
        self.cur.execute(sql)
        self.connect.commit()