from tkinter import *
from tkinter.messagebox import * 
from db.db import *
import gui.UserPage as up
import op as op

class LendPage():
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
        top_label = Label(top_frame, text = "Lend books", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        bid_frame = Frame(self.page, bg='white')
        bid_frame.pack(side=TOP,ipady=10)
        Label(bid_frame, text='lend book id', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.bid = Entry(bid_frame, bg='white')
        self.bid.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='lend books', command=self.lend).pack(side=LEFT)
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

    def goback(self):
        self.page.destroy()
        up.UserPage(self.root)
    def lend(self):
        op.operations().lend_book(self.bid.get())
