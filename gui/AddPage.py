from tkinter import *
from tkinter.messagebox import * 
from db.db import *
import gui.LogPage as lp
import gui.AdminPage as ap
import op.op as op

class AddPage():
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
        top_label = Label(top_frame, text = "Add books", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        bid_frame = Frame(self.page, bg='white')
        bid_frame.pack(side=TOP,ipady=10)
        Label(bid_frame, text='bid', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.bid = Entry(bid_frame, bg='white')
        self.bid.pack(side=LEFT)

        tit_frame = Frame(self.page, bg='white')
        tit_frame.pack(side=TOP,ipady=10)
        Label(tit_frame, text='title', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.title = Entry(tit_frame, bg='white')
        self.title.pack(side=LEFT)
        
        aut_frame = Frame(self.page, bg='white')
        aut_frame.pack(side=TOP,ipady=10)
        Label(aut_frame, text='author', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.author = Entry(aut_frame, bg='white')
        self.author.pack(side=LEFT)
        
        yea_frame = Frame(self.page, bg='white')
        yea_frame.pack(side=TOP,ipady=10)
        Label(yea_frame, text='year', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.year = Entry(yea_frame, bg='white')
        self.year.pack(side=LEFT)
        
        cat_frame = Frame(self.page, bg='white')
        cat_frame.pack(side=TOP,ipady=10)
        Label(cat_frame, text='category', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.category = Entry(cat_frame, bg='white')
        self.category.pack(side=LEFT)
        
        pri_frame = Frame(self.page, bg='white')
        pri_frame.pack(side=TOP,ipady=10)
        Label(pri_frame, text='price', bg='white' ,font=("Calibri", 12)).pack(side=LEFT)
        self.price = Entry(pri_frame, bg='white')
        self.price.pack(side=LEFT)


        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='insert', command=self.insert).pack(side=LEFT)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

    def goback(self):
        self.page.destroy()
        ap.AdminPage(self.root)
    def insert(self):
        ops=op.operations()
        ops.insert_book(self.bid.get(), self.title.get(), self.author.get(), self.year.get(), self.category.get(), self.price.get())
