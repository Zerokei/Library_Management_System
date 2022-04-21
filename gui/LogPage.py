from tkinter import *
from tkinter.messagebox import * 
import gui.RegPage as rp
import gui.UserPage as up
import gui.AdminPage as ap
import op as op

class LoginPage():
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
        user_label = Label(user_frame, text='username', bg='white' ,font=("Calibri", 12))
        user_label.pack(side=LEFT)
        self.user_entry = Entry(user_frame, bg='white')
        self.user_entry.pack(side=LEFT)

        passward_frame = Frame(self.page, bg='white')
        passward_frame.pack(side=TOP,ipady=10)
        passward_label = Label(passward_frame, text='passward', bg='white', font=("Calibri", 12))
        passward_label.pack(side=LEFT)
        self.passward_entry = Entry(passward_frame, bg='white')
        self.passward_entry.pack(side=LEFT)

        btn_frame = Frame(self.page, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        Button(btn_frame, text='login', command=self.try_login).pack(side=LEFT)
        empty_btn = Label(btn_frame, bg='white')
        empty_btn.pack(side=LEFT,ipadx=10)
        Button(btn_frame, text='login_admin', command=self.admin_login).pack(side=LEFT)
        empty_btn = Label(btn_frame, bg='white')
        empty_btn.pack(side=LEFT,ipadx=10)
        register_btn = Button(btn_frame, text='register', command=self.register)
        register_btn.pack(side=LEFT)
    
    def try_login(self):
        if(op.operations().login(self.user_entry.get(),self.passward_entry.get()) == False):
            showinfo(title='Error', message='Wrong username or wrong passward!')
            return        
        self.page.destroy()
        up.UserPage(self.root)

    def register(self):
        self.page.destroy()
        rp.RegisterPage(self.root)

    def admin_login(self):
        username = self.user_entry.get()
        passward = self.passward_entry.get()
        if(username != 'admin' or passward != 'admin'):
            showinfo(title='Error', message='Wrong username or wrong passward!')
        else:
            self.page.destroy()
            ap.AdminPage(self.root)

