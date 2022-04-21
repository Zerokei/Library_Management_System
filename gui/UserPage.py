from tkinter import *
from tkinter.messagebox import * 
from db.db import *
import gui.LogPage as lp
import gui.LendPage as rtp
import gui.QueryPage as qp
import gui.ReturnPage as rp
import op as op

class UserPage():
    def __init__(self, main=None):
        self.root = main
        self.root.geometry('800x600')
        self.root.configure(background='white')
        self.Do()

    def Do(self):
        self.page = Frame(self.root) #创建Frame 
        self.page.pack() 
        self.page.configure(background='white')
        top_frame = Frame(self.page, bg='white')
        top_frame.pack(side=TOP, ipady=70)
        top_label = Label(top_frame, text = "Welcome! {}".format(op.operations().login_name), bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='lend books', command=self.rent).pack(side=LEFT)
        Label(btn_frame, bg='white').pack(side=LEFT,ipadx=10)
        Button(btn_frame, text='show books', command=self.query).pack(side=LEFT)
        Label(btn_frame, bg='white').pack(side=LEFT,ipadx=10)
        Button(btn_frame, text='return books', command=self.ret).pack(side=LEFT)
        Label(btn_frame, bg='white').pack(side=LEFT,ipadx=10)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

    def query(self):
        self.page.destroy()
        qp.QueryPage(self.root)
    def rent(self):
        self.page.destroy()
        rtp.LendPage(self.root)
    def goback(self):
        self.page.destroy()
        lp.LoginPage(self.root)
    def ret(self):
        self.page.destroy()
        rp.ReturnPage(self.root)
        
