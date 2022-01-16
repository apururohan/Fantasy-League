import tkinter as r
import tkinter.font as tkfont
admin=r.Tk()
admin.title("Admin Login")
admin.configure(bg='cyan')
admin.geometry('770x500')

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=100)

l=r.Label(admin,font=labelsty,text='ADMIN')
l.pack(side='top')
l.place()
l.configure(bg='cyan')

f1=tkfont.Font(family="Lucida Grande",size=10)
f1.configure(size=25)

f2=tkfont.Font(family='Lucida Grande',size=10)
f2.configure(size=20)

f3=tkfont.Font(family='Lucida Grande',size=10)
f3.configure(size=10)

    

l1=r.Label(admin,text='Enter the passkey',font=f1)
e1=r.Entry(admin,width=10,font=f1)
l1.place(x=150,y=250)
l1.configure(bg='cyan')
e1.place(x=410,y=250)

def launch():
    passkey=e1.get()
    if(passkey=='1409'):
        admin.destroy()
        #print("Thaggade lee")
        import matchsetup
    else:
        l5=r.Label(admin,text="Wrong passkey",font=f2)
        l5.place(x=290,y=175)
        l5.configure(bg='red')

b1=r.Button(admin,text='Launch',font=f2,command=launch)
b1.place(x=350,y=357)

def back():
    admin.destroy()
    import page1

b2=r.Button(admin,text='Back',font=f3,command=back)
b2.place(x=15,y=450)
admin.mainloop()
