from tkinter import *
import tkinter

win=Tk()
win.title=('LOG')
win.geometry("500x500")

def mains():
    s=v.get()
    print (s)



v = tkinter.StringVar()
e = tkinter.Entry(win, textvariable=v)
e.pack()

b=Button(win,command=mains).pack()


win.mainloop()