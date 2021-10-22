from tkinter import *
from tkinter import ttk
import sqlite3
import tkinter


win=Tk()
win.title=("View")
win.geometry('400x400')

con = sqlite3.connect("Account.db")
cur = con.cursor()
cur.execute("SELECT * FROM log")
rows = cur.fetchall()
con.close()

viu=ttk.Treeview(win)

viu['Columns']=('no','user','pass')

viu.column('no',width=50,minWidth=50,anchor=tkinter.CENTER)
viu.column('user',width=50,minWidth=50,anchor=tkinter.CENTER)
viu.column('pass',width=50,minWidth=50,anchor=tkinter.CENTER)

viu.heading('no',text="No",anchor=tkinter.CENTER)

viu.heading('user',text="user",anchor=tkinter.CENTER)

viu.heading('pass',text="pass",anchor=tkinter.CENTER)


i=0
for ro in con:
    viu.insert('',i,text="",values=(ro[0],ro[1],ro[2]))
    i=i+1


viu.pack()

win.mainloop()