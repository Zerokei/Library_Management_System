import tkinter
from gui.LogPage import *
import op.op as op

window = tkinter.Tk()
# 設定視窗標題、大小和背景顏色
window.title('Library Management System')
LoginPage(window)
op.operations().query_book()
window.mainloop()