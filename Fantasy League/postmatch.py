'''import openpyxl
import tkinter as r
import tkinter.font as tkfont

postmatch=r.Tk()
postmatch.title("POST MATCH")

labelsty=tkfont.Font(family="Lucida Grande",size=10)
labelsty.configure(size=100)

wb=openpyxl.load_workbook("Project.xlsx")
sh1=wb['Sheet1']

rows=sh1.max_row
cols=sh1.max_column

def launch(name):
    f1=open("name.txt","w")
    f1.write(name+".txt")
    f1.close()
    f2=open("user.txt","w")
    f2.write("adminmowa")
    f2.write("\n")
    f2.write("2")
    f2.close()
    import answer1
    
    

for i in range(4,cols,7):
    namenew=""
    if(sh1.cell(2,i).value=='#'):
        
        name=sh1.cell(1,i).value
        for j in name:
            print(j+'\n')
            if(j=="%" or j=="1" or j=="2" or j=="7" or j=="8"):
                pass
            else:
                namenew=namenew+j
    print(namenew)
    b = r.Button(postmatch,text=namenew,command=launch(namenew))
    b.pack()

    
'''

f2=open("user.txt","w")
f2.write("adminmowa")
f2.write("\n")
f2.write("2")
f2.close()
import bet1
