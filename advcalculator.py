from tkinter import *
window=Tk()
window.title("Calculator")

op=""
variable=StringVar()

def click(no):
    global op
    op=op+str(no)
    variable.set(op)
def clear():
    global op
    op=""
    variable.set(op)
def sum():
    global op
    op=str(eval(op))
    variable.set(op)

display=Entry(window,font=("arial",20,"bold"),bd=25,textvariable=variable,justify="right")
display.grid(columnspan=5)

b7=Button(window,text="7",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(7))
b7.grid(row=1,column=0)

b8=Button(window,text="8",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(8))
b8.grid(row=1,column=1)

b9=Button(window,text="9",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(9))
b9.grid(row=1,column=2)

b4=Button(window,text="4",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(4))
b4.grid(row=2,column=0)

b5=Button(window,text="5",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(5))
b5.grid(row=2,column=1)

b6=Button(window,text="6",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(6))
b6.grid(row=2,column=2)

b1=Button(window,text="1",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(1))
b1.grid(row=3,column=0)

b2=Button(window,text="2",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(2))
b2.grid(row=3,column=1)

b3=Button(window,text="3",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(3))
b3.grid(row=3,column=2)

b0=Button(window,text="0",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click(0))
b0.grid(row=4,column=0)

bpoint=Button(window,text=".",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click("."))
bpoint.grid(row=4,column=1)

bclear=Button(window,text="c",font=("arial",20,"bold"),bd=5,padx=10,command=clear)
bclear.grid(row=4,column=2)

bplus=Button(window,text="+",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click("+"))
bplus.grid(row=1,column=4)

bminus=Button(window,text="-",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click("-"))
bminus.grid(row=2,column=4)

bmulti=Button(window,text="*",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click("*"))
bmulti.grid(row=3,column=4)

bdiv=Button(window,text="/",font=("arial",20,"bold"),bd=5,padx=10,command=lambda:click("/"))
bdiv.grid(row=4,column=4)

beq=Button(window,text="=",font=("arial",20,"bold"),bd=5,padx=10,command=sum)
beq.grid(row=5,column=5)

window.mainloop()


















