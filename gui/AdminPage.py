from tkinter import *
from tkinter.messagebox import * 
from db.db import *
import gui.LogPage as lp
import gui.QueryPage as qp
import gui.AddPage as adp

class AdminPage():
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
        top_label = Label(top_frame, text = "Admin Page", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='add', command=self.add).pack(side=LEFT)
        Button(btn_frame, text='query', command=self.query).pack(side=LEFT)
        empty_btn = Label(btn_frame, bg='white')
        empty_btn.pack(side=LEFT,ipadx=20)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)
    
    def query(self):
        self.page.destroy()
        qp.QueryAdminPage(self.root)
    def add(self):
        self.page.destroy()
        adp.AddPage(self.root)
    def goback(self):
        self.page.destroy()
        lp.LoginPage(self.root)
