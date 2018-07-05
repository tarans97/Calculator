from tkinter import* #root is variable
root=Tk()

root.geometry("1600x800") #giving size to window
root.title("Calculator")


text_input=StringVar()
op=""



f1=Frame(root,height=100,width=1600,bg="blue")
f1.pack(side=TOP)
f2=Frame(root,height=700,width=800,bg="green")
f2.pack(side=BOTTOM)
lb1=Label(f1,font=("ALGERIAN",50),bg="yellow",bd=10,text="calculator")
lb1.grid() #row=0,col=0

def cal(num):
    global op
    op=op+str(num)
    text_input.set(op)
#eval() takes op value and convert into string    
def btneq():
    global op
    ans=str(eval(op))
    text_input.set(ans)
    op=""

def btnclr():
    global op
    op=""
    text_input.set(op)

#lambda:makes function elligible for particular input


e1=Entry(f2,insertwidth=10,width=10,bd=10,justify="right",bg="Sky blue",font=("ALGERIAN",50),textvariable=text_input)#creating entry
e1.grid(columnspan=4)

b1=Button(f2,padx=25,command=lambda:cal(1),pady=15,font=("arial",10),bd=10,bg="blue",text="1").grid(row=1,column=0)
b2=Button(f2,padx=25,command=lambda:cal(2),pady=15,font=("arial",10),bd=10,bg="blue",text="2").grid(row=1,column=1)
b3=Button(f2,padx=25,command=lambda:cal(3),pady=15,font=("arial",10),bd=10,bg="blue",text="3").grid(row=1,column=2)

bpls=Button(f2,padx=25,command=lambda:cal('+'),pady=15,font=("arial",10),bd=10,bg="blue",text="+").grid(row=1,column=3)

b4=Button(f2,padx=25,command=lambda:cal(4),pady=15,font=("arial",10),bd=10,bg="blue",text="4").grid(row=2,column=0)
b5=Button(f2,padx=25,command=lambda:cal(5),pady=15,font=("arial",10),bd=10,bg="blue",text="5").grid(row=2,column=1)
b6=Button(f2,padx=25,command=lambda:cal(6),pady=15,font=("arial",10),bd=10,bg="blue",text="6").grid(row=2,column=2)

bmin=Button(f2,padx=25,command=lambda:cal('-'),pady=15,font=("arial",10),bd=10,bg="blue",text="-").grid(row=2,column=3)

b7=Button(f2,padx=25,command=lambda:cal(7),pady=15,font=("arial",10),bd=10,bg="blue",text="7").grid(row=3,column=0)
b8=Button(f2,padx=25,command=lambda:cal(8),pady=15,font=("arial",10),bd=10,bg="blue",text="8").grid(row=3,column=1)
b9=Button(f2,padx=25,command=lambda:cal(9),pady=15,font=("arial",10),bd=10,bg="blue",text="9").grid(row=3,column=2)
bmul=Button(f2,command=lambda:cal('*'),padx=25,pady=15,font=("arial",10),bd=10,bg="blue",text="*").grid(row=3,column=3)

b0=Button(f2,padx=25,command=lambda:cal(0),pady=15,font=("arial",10),bd=10,bg="blue",text="0").grid(row=4,column=0)
beql=Button(f2,padx=25,command=lambda:btneq(),pady=15,font=("arial",10),bd=10,bg="blue",text="=").grid(row=4,column=1)
bclr=Button(f2,padx=25,command=lambda:btnclr(),pady=15,font=("arial",10),bd=10,bg="blue",text="clr").grid(row=4,column=2)
bdiv=Button(f2,padx=25,command=lambda:btneq(),pady=15,font=("arial",10),bd=10,bg="blue",text="/").grid(row=4,column=3)




root.mainloop() #root will run until we close  root window
