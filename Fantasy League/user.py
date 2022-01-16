


import tkinter as r
import tkinter.font as tkfont
user=r.Tk()
user.title("User")
user.configure(bg='cyan')
user.geometry('770x500')

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=100)

l=r.Label(user,text='LOGIN',font=labelsty)
l.pack(side='top')
l.place()
l.configure(bg='cyan')

buttonsty=tkfont.Font(family="Lucida Grande",size=2)
buttonsty.configure(size=20)

def existing():
        user.destroy()
        import existingdemo
def new():
        user.destroy()
        import new

def back():
        user.destroy()
        import page1
        
f3=tkfont.Font(family="Lucida Grande",size=10)
f3.configure(size=10)

button1=r.Button(user,text='Existing user',command=existing,font=buttonsty)
button2=r.Button(user,text='New user',command=new,font=buttonsty)
button3=r.Button(user,text='Back',font=f3,command=back)

button1.place(x=302,y=250)
button2.place(x=325,y=310)
button3.place(x=15,y=450)
user.mainloop()

