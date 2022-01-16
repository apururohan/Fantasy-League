import tkinter as r
import tkinter.font as tkfont
page2=r.Tk()
page2.title("Login")
page2.configure(bg='cyan')
page2.geometry('770x500')

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=100)

l=r.Label(page2,text='WELCOME',font=labelsty)
l.pack(side='top')
l.place()
l.configure(bg='cyan')

buttonsty=tkfont.Font(family="Lucida Grande",size=2)
buttonsty.configure(size=20)

def user():
    page2.destroy()
    import user
def admin():
    page2.destroy()
    import admin




button1=r.Button(page2,text='User login',command=user,font=buttonsty)
button2=r.Button(page2,text='Admin Login',command=admin,font=buttonsty)

#button1.pack(size='top')
button1.place(x=315,y=250)
button2.place(x=302,y=310)
page2.mainloop()
