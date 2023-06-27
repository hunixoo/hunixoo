from tkinter import *
from tkinter import messagebox
import pymcprotocol

from main import MAIN
from define import *

window = Tk()
main = MAIN(window)
pymc3e = pymcprotocol.Type3E()

txtip_var = StringVar()
txtport_var = StringVar()
txtd1 = StringVar()
txtd2 = StringVar()
#----
def connect():
    if (txtip_var.get() !=''):
        try:
            print(txtport_var.get())
            pymc3e.setaccessopt(commtype="binary")
            pymc3e.connect(str(txtip_var.get()), int(txtport_var.get()))
            status.config(text="Connect Success",font=('Times New Roman',10),fg=COLOR_GREEN)
        except:
            status.config(text="Connect Faild", font=('Times New Roman', 10), fg=COLOR_RED)
    else:
        messagebox.showinfo("Error","Ban chua nhap IP - Port")
def read():
    #wordunits_values = pymc3e.batchread_wordunits("D10.1", 20)
    #print(wordunits_values)
    wordunits_values = pymc3e.batchread_bitunits("X640", 10)
    print(wordunits_values)

def write():
    pymc3e.batchwrite_wordunits("D1200",[20])
#-----Create Button
btncon = Button(window, text='CONNECT', width=8, font=('Times New Roman',10), padx=10, pady=10, command=connect)
btncon.place(x=30, y=130)
btnread = Button(window, text='READ', width=8, font=('Times New Roman',10), padx=10, pady=10, command=read)
btnread.place(x=130, y=130)
btnwrite = Button(window, text='WRITE', width=8, font=('Times New Roman',10), padx=10, pady=10, command=write)
btnwrite.place(x=230, y=130)
#-----Create textbox
txtip = Entry(window, width=20, font=('Times New Roman',10),textvariable=txtip_var).place(x=65, y=50)
txtport = Entry(window, width=20, font=('Times New Roman',10),textvariable=txtport_var).place(x=65, y=90)
txtd1 = Entry(window, width=20, font=('Times New Roman',10)).place(x=280, y=50)
txtd2 = Entry(window, width=20, font=('Times New Roman',10)).place(x=280, y=90)
#-----Create label
status = Label(window, text='........')
status.place(x=30, y=10)

window.mainloop()
#------



