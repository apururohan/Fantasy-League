import tkinter as r
import tkinter.font as tkfont
match=r.Tk()
match.title("Match setup")
match.configure(bg='cyan')
match.geometry('770x500')

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=50)

l=r.Label(match,font=labelsty,text='MATCH')
l.pack(side='top')
l.place()
l.configure(bg='cyan')

f1=tkfont.Font(family="Lucida Grande",size=10)
f1.configure(size=25)

f3=tkfont.Font(family='Lucida Grande',size=10)
f3.configure(size=10)

def prematch():
    match.destroy()
    import prematch
def postmatch():
    match.destroy()
    import postmatch
def bonus():
    match.destroy()
    import add

b1=r.Button(match,font=f1,text='Pre-match Setup',command=prematch)
b1.configure(bg='yellow')
b1.place(x=250,y=170)

b2=r.Button(match,font=f1,text='Post-match Setup',command=postmatch)
b2.configure(bg='yellow')
b2.place(x=244,y=250)

b3=r.Button(match,font=f1,text="Bonus",command=bonus)
b3.configure(bg='yellow')
b3.place(x=330,y=330)

def back():
    match.destroy()
    import admin

b2=r.Button(match,text='Back',font=f3,command=back)
b2.place(x=15,y=450)
