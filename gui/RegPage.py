from tkinter import *
from tkinter.messagebox import * 
from db.db import *
import gui.LogPage as lp
import op.op as op

class RegisterPage():
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
        top_label = Label(top_frame, text = "Welcome to my Library Management System", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        user_frame = Frame(self.page, bg='white')
        user_frame.pack(side=TOP, ipady=10)
        user_label = Label(user_frame, text='userid', bg='white' ,font=("Calibri", 12))
        user_label.pack(side=LEFT)
        self.user = Entry(user_frame, bg='white')
        self.user.pack(side=LEFT)


        name_frame = Frame(self.page, bg='white')
        name_frame.pack(side=TOP, ipady=10)
        name_label = Label(name_frame, text='name', bg='white' ,font=("Calibri", 12))
        name_label.pack(side=LEFT)
        self.name = Entry(name_frame, bg='white')
        self.name.pack(side=LEFT)

        gender_frame = Frame(self.page, bg='white')
        gender_frame.pack(side=TOP, ipady=10)
        gender_label = Label(gender_frame, text='gender(F/M)', bg='white' ,font=("Calibri", 12))
        gender_label.pack(side=LEFT)
        self.gender = Entry(gender_frame, bg='white')
        self.gender.pack(side=LEFT)

        passward_frame = Frame(self.page, bg='white')
        passward_frame.pack(side=TOP,ipady=10)
        passward_label = Label(passward_frame, text='passward', bg='white', font=("Calibri", 12))
        passward_label.pack(side=LEFT)
        self.password = Entry(passward_frame, bg='white')
        self.password.pack(side=LEFT)

        passward2_frame = Frame(self.page, bg='white')
        passward2_frame.pack(side=TOP,ipady=10)
        passward2_label = Label(passward2_frame, text='passward_again', bg='white', font=("Calibri", 12))
        passward2_label.pack(side=LEFT)
        self.password2 = Entry(passward2_frame, bg='white')
        self.password2.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='submit', command=self.try_register).pack(side=LEFT)
        empty_btn = Label(btn_frame, bg='white')
        empty_btn.pack(side=LEFT,ipadx=20)
        Button(btn_frame, text='return', command=self.goback).pack(side=LEFT)

    def try_register(self):
        if self.user.get().isdigit() == False:
            showinfo(title='Error', message='the userid must be digits!')    
            return
        if self.gender.get() != 'F' and self.gender.get() != 'M':
            showinfo(title='Error', message='Gender should be M or F!')    
            return
        if self.password.get() != self.password2.get():
            showinfo(title='Error', message='Inconsistent passwords!')
            return
        ops=op.operations()
        ops.register(self.user.get(), self.name.get(), self.gender.get(), self.password.get(), self.password2.get())
    def goback(self):
        self.page.destroy()
        lp.LoginPage(self.root)
