import pymysql

from gui.LoginPage import *
from tkinter import *


window = Tk()
# 設定視窗標題、大小和背景顏色
window.title('Library Management System')
LoginPage(window)
window.mainloop()

db = pymysql.connect(
    host = '127.0.0.1',
    port = 3306,
    user = 'zerokei',
    passwd = '123456',
    db='Library_management_system',
    charset = 'utf8')
