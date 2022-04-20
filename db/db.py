import pymysql

db = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'zerokei',
    passwd = '123456',
    db='Library_management_system',
    charset = 'utf8')