from tkinter import *
from tkinter.messagebox import * 
from tkinter import ttk
from db.db import *
import gui.AdminPage as ap
import gui.UserPage as up
import op as op

class QueryPage():
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
        top_label = Label(top_frame, text = "Books in the library", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

        ShowBooks.Do()

    def goback(self):
        self.page.destroy()
        up.UserPage(self.root)

class QueryAdminPage():
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
        top_label = Label(top_frame, text = "All of the Books in the library", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

        ShowBooks.Do()

    def goback(self):
        self.page.destroy()
        ap.AdminPage(self.root)
class ShowBooks():
    def Do():
        tree=ttk.Treeview(Tk())#表格
        tree["columns"]=("title","author",'year','category','price','status')
        tree.column("title",width=200)   
        tree.column("author",width=200)   
        tree.column("year",width=100)   
        tree.column("category",width=150)   
        tree.column("price",width=100)   
        tree.column("status",width=30)   
        
        tree.heading("title",text="title")  
        tree.heading("author",text="author")  
        tree.heading("year",text="year")  
        tree.heading("category",text="category")  
        tree.heading("price",text="price")
        tree.heading("status",text="free(Y/N)")

        books = op.operations().query_book()
        i = 0
        for book in books:
            i = i + 1
            value=[]
            value.append(book[1])
            value.append(book[2])
            value.append(book[3])
            value.append(book[4])
            value.append(book[5])
            if op.operations().if_lend(book[0]):
                s = 'N'
            else:
                s = 'Y'
            value.append(s)
            tree.insert("", i, text=book[0] ,values=value) #插入数据，
                   
        tree.pack()