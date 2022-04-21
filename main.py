import pymysql

from gui.RegisterPage import *
from gui.LoginPage import *
from tkinter import *


window = Tk()
# 設定視窗標題、大小和背景顏色
window.title('Library Management System')
LoginPage(window)
window.mainloop()


