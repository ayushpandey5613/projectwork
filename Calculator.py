import tkinter as tk
from tkinter import ttk


w=tk.Tk()

w.title("Calculator")
  
operator=""

def action(number): 
    global operator
    operator=operator+str(number)   
    U.set(operator)  
  
 
def equal():
    global operator  
    if("x" in operator):
        operator=operator.replace("x","*")
 
        try:
          operator=eval(operator)
          U.set(operator)
          operator=" "
        except:
          U.set("Syntax Error")
        

    if("√" in operator):
       x=operator.find("√")
       k=operator[x-1]
       if(k=="2" or k=="3" or k=="4" or k=="5" or k=="6" or k=="7" or k=="8" or k=="9" ):
         y=(int(operator[x+1])**(.5))
         operator=operator.replace(operator[x:x+2],"*"+str(y))
         try:
          operator=eval(operator)
          U.set(operator)
          operator=""
         except:
          U.set("Syntax Error")
       else:
         y=(int(operator[x+1])**(.5))
         operator=operator.replace(operator[x:x+2],str(y))
         try:
           operator=eval(operator)
           U.set(operator)
           operator=""
         except:
           U.set("Syntax Error")
    elif("^" in operator):
       x=operator.find("^")
       y=(int(operator[x-1])**int(operator[x+1]))
       operator=operator.replace(operator[x-1:x+2],str(y))
       try:
         operator=eval(operator)
         U.set(operator)
         operator=""
       except:
         U.set("Syntex Error")


    elif("%" in operator ):
       operator=operator.replace("%","*1/100*")
       try:
         operator=eval(operator)
         U.set(operator)
         operator=" "
       except:
         U.set("Syntax Error")
    else:
      try:
        operator=eval(operator)
        U.set(operator)
        operator=" "
      except:
        U.set("Syntax error")
      
    


def clr():
    global operator
    U.set("")
    operator=""

  
  
b7=ttk.Button(w,width=25,text="7",command=(lambda :action(7)))
b7.grid(row=1,column=0)


b8=ttk.Button(w,width=25,text="8",command=(lambda :action(8)))
b8.grid(row=1,column=1)

b9=ttk.Button(w,width=25,text="9",command=(lambda :action(9)))
b9.grid(row=1,column=2)

bop=ttk.Button(w,width=25,text="+",command=(lambda :action("+")))
bop.grid(row=1,column=3)

bp=ttk.Button(w,width=25,text=".",command=(lambda :action(".")))
bp.grid(row=1,column=4)

b4=ttk.Button(w,width=25,text="4",command=(lambda :action(4)))
b4.grid(row=2,column=0)

b5=ttk.Button(w,width=25,text="5",command=(lambda :action(5)))
b5.grid(row=2,column=1)

b6=ttk.Button(w,width=25,text="6",command=(lambda :action(6)))
b6.grid(row=2,column=2)

bm=ttk.Button(w,width=25,text="-",command=(lambda :action("-")))
bm.grid(row=2,column=3)

bpr=ttk.Button(w,width=25,text="%",command=(lambda :action("%")))
bpr.grid(row=2,column=4)

b1=ttk.Button(w,width=25,text="1",command=(lambda :action(1)))
b1.grid(row=3,column=0)

b2=ttk.Button(w,width=25,text="2",command=(lambda :action(2)))
b2.grid(row=3,column=1)

b3=ttk.Button(w,width=25,text="3",command=(lambda :action(3)))
b3.grid(row=3,column=2)

bd=ttk.Button(w,width=25,text="/",command=(lambda :action("/")))
bd.grid(row=3,column=3)

bpw=ttk.Button(w,width=25,text="^",command=(lambda :action("^")))
bpw.grid(row=3,column=4)

bz=ttk.Button(w,width=25,text="0",command=(lambda :action(0)))
bz.grid(row=4,column=0)

bsqrt=ttk.Button(w,width=25,text="√",command=(lambda :action("√")))
bsqrt.grid(row=4,column=1)

be=ttk.Button(w,width=25,text="=",command=(lambda :equal()))
be.grid(row=4,column=2)

bm=ttk.Button(w,width=25,text="x",command=(lambda :action("*")))
bm.grid(row=4,column=3)

bc=ttk.Button(w,width=25,text="Clear",command=(lambda :clr()))
bc.grid(row=4,column=4)


U=tk.StringVar()
Ub1=ttk.Entry(w,width=125,textvariable=U)
Ub1.grid(row=0,column=0,columnspan=5)
Ub1.focus()





w.mainloop()
