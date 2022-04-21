from tkinter import *
from tkinter.messagebox import * 
class RegisterPage():
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

        name_frame = Frame(self.root, bg='white')
        name_frame.pack(side=TOP, ipady=10)
        name_label = Label(name_frame, text='name', bg='white' ,font=("Calibri", 12))
        name_label.pack(side=LEFT)
        self.name_entry = Entry(name_frame, bg='white')
        self.name_entry.pack(side=LEFT)

        gender_frame = Frame(self.root, bg='white')
        gender_frame.pack(side=TOP, ipady=10)
        gender_label = Label(gender_frame, text='gender(F/M)', bg='white' ,font=("Calibri", 12))
        gender_label.pack(side=LEFT)
        self.gender_entry = Entry(gender_frame, bg='white')
        self.gender_entry.pack(side=LEFT)

        passward_frame = Frame(self.root, bg='white')
        passward_frame.pack(side=TOP,ipady=10)
        passward_label = Label(passward_frame, text='passward', bg='white', font=("Calibri", 12))
        passward_label.pack(side=LEFT)
        self.passward_entry = Entry(passward_frame, bg='white')
        self.passward_entry.pack(side=LEFT)

        passward2_frame = Frame(self.root, bg='white')
        passward2_frame.pack(side=TOP,ipady=10)
        passward2_label = Label(passward2_frame, text='passward_again', bg='white', font=("Calibri", 12))
        passward2_label.pack(side=LEFT)
        self.passward2_entry = Entry(passward2_frame, bg='white')
        self.passward2_entry.pack(side=LEFT)

        btn_frame = Frame(self.root, bg='white')
        btn_frame.pack(side=TOP,ipady=10)
        submit_btn = Button(btn_frame, text='submit', command=self.try_login)
        submit_btn.pack(side=LEFT)

        message_frame = Frame(self.root, bg='white')
        message_frame.pack(side=TOP,ipady=10)
        message_label = Label(message_frame, text='register success!', bg='white', font=("Calibri", 12))
        message_label.pack(side=LEFT)