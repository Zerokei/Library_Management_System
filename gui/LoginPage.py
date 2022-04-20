from tkinter import *
from tkinter.messagebox import * 
# class LoginPage(self):
#     def __init__(self) -> None:

class LoginPage():
    def __init__(self, main=None):
        self.root = main
        self.root.geometry('800x600')
        self.root.configure(background='white')
        self.Do()
    def Do(self):
        top_frame = Frame(self.root, bg='white')
        top_frame.pack(side=TOP, ipady=70)
        top_label = Label(top_frame, text = "Welcome to my Library Management System", bg= "white", font=("Calibri", 20))
        top_label.pack(side=LEFT)

        user_frame = Frame(self.root, bg='white')
        user_frame.pack(side=TOP, ipady=10)
        user_label = Label(user_frame, text='username', bg='white' ,font=("Calibri", 12))
        user_label.pack(side=LEFT)
        self.user_entry = Entry(user_frame, bg='white')
        self.user_entry.pack(side=LEFT)

        passward_frame = Frame(self.root, bg='white')
        passward_frame.pack(side=TOP,ipady=10)
        passward_label = Label(passward_frame, text='passward', bg='white', font=("Calibri", 12))
        passward_label.pack(side=LEFT)
        self.passward_entry = Entry(passward_frame, bg='white')
        self.passward_entry.pack(side=LEFT)

        btn_frame = Frame(self.root, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        login_btn = Button(btn_frame, text='login', command=self.try_login)
        login_btn.pack(side=LEFT)
        empty_btn = Label(btn_frame, bg='white')
        empty_btn.pack(side=LEFT,ipadx=20)
        register_btn = Button(btn_frame, text='register', command=self.register)
        register_btn.pack(side=LEFT)
    
    def try_login(self):
        username = self.user_entry.get()
        passward = self.passward_entry.get()
    def register(self):
        username = self.user_entry.get()
        passward = self.passward_entry.get()
        message_frame = Frame(self.root, bg='white')
        message_frame.pack(side=TOP,ipady=10)
        message_label = Label(message_frame, text='register success!', bg='white', font=("Calibri", 12))
        message_label.pack(side=LEFT)

