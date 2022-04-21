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
    def query_sql(self, sql):
        self.connect.cursor().execute(sql)
        return self.connect.cursor().fetchall()
    def update_sql(self, sql):
        self.connect.cursor().execute(sql)
        self.connect.commit()
