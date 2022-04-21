from numpy import empty
import db.db as db
from tkinter import *
from tkinter.messagebox import *
from urllib.parse import quote, unquote
from datetime import datetime

class operations(object):
    login_user = 9999
    login_name = "YZK"
    def __init__(self):
        self.db = db.DB()
    def register(self, user, name, gender, password, password2):
        sql = "select password from students where sid = {};".format(user)
        if(self.db.query_sql(sql) == ""):
            showinfo(title='Error', message='Duplicate serial number!')
            return
        else:
            sql = "insert into students values({},'{}','{}','{}');".format(user, name, gender, password)
            self.db.update_sql(sql)
            showinfo(title='Info', message='Register successfully!')
        
    def login(self, user, password):
        sql = "select password from students where sid = {}".format(user)
        t_password = self.db.query_sql(sql)
        if str(password) != t_password[0][0]:
            return False
        else :
            operations.login_user = user
            sql = "select name from students where sid = {}".format(user)
            operations.login_name = self.db.query_sql(sql)[0][0]
            return True

    def insert_book(self, bid, title, author, year, category, price):
        sql = "insert into book values({},'{}','{}',{},'{}',{});".format(bid, title, author, year, category, price)
        self.db.update_sql(sql)
        showinfo(title='Info', message='Add book successfully!')

    def query_book(self, person=None):
        sql = "select * from book"
        books = self.db.query_sql(sql)
        return books

    def lend_book(self, bid):
        sql = "select * from book where bid={}".format(bid)
        book = self.db.query_sql(sql)
        if not book:
            showinfo(title='Error', message='Book is not exist!') 
            return

        if operations().if_lend(bid) == True:
            sql = "insert into borrow values({},{},{},'{}');".format(bid, bid, operations().login_user, datetime.today().strftime('%Y-%m-%d'))
            self.db.update_sql(sql)
            showinfo(title='Info', message='Lend book successfully!')
            return
        else:
            showinfo(title='Error', message='This book has been lent!')
            return

    def ret_book(self, bid):
        sql = "select * from book where bid={}".format(bid)
        book = self.db.query_sql(sql)
        if not book:
            showinfo(title='Error', message='Book is not exist!') 
            return

        if operations().if_lend(bid) == False:
            showinfo(title='Error', message='This book has not been lent!')
            return
        elif res[0][2] != operations().login_user:
            showinfo(title='Error', message='Sorry! This book is not lent by you!')
        else:
            sql = "delete from borrow where cid = {};".format(bid)
            self.db.update_sql(sql)
            showinfo(title='Info', message='Return book successfully!')
            return
            
    def if_lend(self, bid):
        sql = "select * from borrow where cid ={}".format(bid)
        res = self.db.query_sql(sql)
        if not res:
            return False
        return True