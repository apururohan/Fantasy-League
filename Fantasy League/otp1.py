import tkinter as r
import tkinter.font as tkfont
otp1=r.Tk()
otp1.title("NEW USER")
otp1.configure(bg='cyan')
otp1.geometry('770x500')

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=100)

l=r.Label(otp1,text='New User',font=labelsty)
l.pack(side='top')
l.place()
l.configure(bg='cyan')

f1=tkfont.Font(family="Lucida Grande",size=10)
f1.configure(size=25)

f2=tkfont.Font(family="Lucida Grande",size=7)
f2.configure(size=15)

f3=tkfont.Font(family="Lucida Grande",size=10)
f3.configure(size=10)


l1=r.Label(otp1,text='Enter the gmail id',font=f1)
e1=r.Entry(otp1,width=22,font=f1)


l1.configure(bg='cyan')
l1.place(x=250,y=250)
e1.place(x=185,y=295)
e1=e1.get()

def otp():
    import smtplib
    import random
    s = smtplib.SMTP(e1,587)  
    s.starttls()
    s.login("160220k012@gmail.com" , "Sonu1409")
    otp = random.randint(1000, 9999)
    otp = str(otp)
    s.sendmail("160220k012@gmail.com" , e1 , otp)
    print("OTP sent succesfully..")
    

b1=r.Button(otp1,text="Send",font=f2,command=otp)
b1.place(x=345,y=350)
