from tkinter import *
from tkinter import ttk
import sqlite3




win=Tk()
win.title=("View")
win.geometry('400x400')

con = sqlite3.connect("Account.db")
cur = con.cursor()
cur.execute("SELECT * FROM log")
rows = cur.fetchall()


viu=ttk.Treeview(win,columns=(1, 2, 3), show='headings',height=8)

viu["columns"]=("no","user","pass")

viu.column("no",width=50,minwidth=50,anchor=CENTER)
viu.column("user",width=50,minwidth=50,anchor=CENTER)
viu.column("pass",width=50,minwidth=50,anchor=CENTER)

viu.heading("no",text="No",anchor=CENTER)

viu.heading("user",text="user",anchor=CENTER)

viu.heading("pass",text="pass",anchor=CENTER)


i=0
for ro in con :
    viu.insert('',i,text="",values=(ro[0],ro[1],ro[2]))
    i=i+1

viu.pack()

con.close()
win.mainloop()