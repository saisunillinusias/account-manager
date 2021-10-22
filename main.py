from tkinter import *
import tkinter
import sqlite3
import os
from tkinter.ttk import LabeledScale

win=tkinter.Tk()
win.title("Account Log")
win.geometry("500x500")

def show():
    LabeledScale.config( text = clicked.get() )
  
# Dropdown menu options
options = [
    "Google",
    "Facebook",
    "twitter",
    "yahoo",
    "Apple",
    "outloook"
    
]
  
# datatype of menu text
clicked = StringVar()
  
# initial menu text
clicked.set( "Other" )

drop = OptionMenu( win , clicked , *options ).place(x=130,y=100)


def setup():
    db=sqlite3.connect("Account.db")
    db.cursor
    db.execute("CREATE TABLE IF NOT EXISTS log(No INT PRIMARY KEY,username text NOT NULL, password text NOT NULL) ")
    db.commit()
    db.close()

def add_data():
    nuser=user.get()
    npass=passw.get()
    db=sqlite3.connect("Account.db")
    db.cursor
    db.execute("INSERT INTO log(username,password) VALUES(?,?)",(nuser,npass))
    db.commit()
    db.close()

def view():
    os.system('view.py')
    



user = tkinter.StringVar()
Label(win,text="USERNAME :").place(x=20,y=20)
Entry(win,textvariable=user).place(x=130,y=20)


passw = tkinter.StringVar()   #varb
Label(win,text="PASSWORD :").place(x=20,y=60)
Entry(win,textvariable=passw).place(x=130,y=60)

Label(win,text="Account :").place(x=20,y=100)

Label(win,text="OTHER :").place(x=20,y=140)
PASS=Entry(win).place(x=130,y=140)

Button(win,text="Add Account",command=add_data).place(x=20,y=180)
Button(win,text="View Account",command=view).place(x=130,y=180)
Button(win,text="Set",command=setup).place(x=230,y=180)


Label(win).place(x=20,y=220)

win.mainloop()