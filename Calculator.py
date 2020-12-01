
from tkinter import *

win = Tk()
button_frame = Frame()
win.title("Calculator@ansel")
entry = Entry (win,width=25,bg = "white",fg="black",borderwidth="9")#input box
entry.grid(row=0,column=1,columnspan=60)

def but1(number):
    current =entry.get()
    entry.delete(0,END)
    entry.insert(0,str(current) + str(number))
    #converting from int to str

def but_clear():
    entry.delete(0, END)

def add():
    f_num = entry.get()
    global x_num
    global math
    math = "addition"
    x_num = int(f_num)
    entry.delete(0, END)

def but_equals():
    sec_num = entry.get()
    entry.delete(0,END)
    if math =="addition":
        entry.insert(0,x_num + int(sec_num))
    elif math =="multiply":
        entry.insert(0, x_num * int(sec_num))
    elif math == "minus":
        entry.insert(0, x_num - int(sec_num))
    elif math =="divide":
        entry.insert(0, x_num / int(sec_num))
  
def product():
    f_num = entry.get()
    global x_num
    global math
    math = "multiply"
    x_num = int(f_num)
    entry.delete(0, END)

def subtract():
    f_num = entry.get()
    global x_num
    global math
    math = "minus"
    x_num = int(f_num)
    entry.delete(0, END)

def quotient():
    f_num = entry.get()
    global x_num
    global math
    math = "divide"
    x_num = int(f_num)
    entry.delete(0, END)
def square():
    f_num = entry.get()
    global x_num
    global math
    math = "sq"
    x_num = int(f_num)
    entry.delete(0, END)
    entry.insert(0, x_num * x_num)

#buttons &function calling
#lambda is used to pass parameters in functions
mybut1= Button(win, text ="7",command = lambda:but1(7),bg="grey" ,fg="black",padx=20)
mybut2 = Button(win, text ="8",command =lambda:but1(8),bg="grey" ,fg="black",padx=20)
mybut3 = Button(win, text ="9",command =lambda:but1(9),bg="grey" ,fg="black",padx=20)
mybut4 = Button(win, text ="4",command =lambda:but1(4),bg="grey" ,fg="black",padx=20)
mybut5 = Button(win, text ="5",command = lambda:but1(5),bg="grey" ,fg="black",padx=20)
mybut6 = Button(win, text ="6",command = lambda:but1(6),bg="grey" ,fg="black",padx=20)
mybut7 = Button(win, text ="1",command = lambda:but1(1),bg="grey" ,fg="black",padx=20)
mybut8 = Button(win, text ="2",command = lambda:but1(2),bg="grey" ,fg="black",padx=20)
mybut9 = Button(win, text ="3",command = lambda:but1(3),bg="grey" ,fg="black",padx=20)
mybut0 = Button(win, text ="0",command = lambda:but1(0),bg="grey" ,fg="black",padx=20)
mybut_equals = Button(win, text ="=",command =but_equals,bg="grey" ,fg="red",padx=20)
mybut_add = Button(win, text ="+",command =add,bg="grey" ,fg="black",padx=20)
mybut_clear =  Button(win, text ="C",command=but_clear,bg="grey" ,fg="black",padx=20)
mybut_prod = Button(win, text ="*",command =product,bg="grey" ,fg="black",padx=20)
mybut_div = Button(win, text ="/",command =quotient,bg="grey" ,fg="black",padx=20)
mybut_sub = Button(win, text ="-",command =subtract,bg="grey" ,fg="black",padx=20)
mybut_sq = Button(win, text ="sqrt",command =square,bg="grey" ,fg="black",padx=10)
#button arrangement
mybut1.grid(row=1,column=0)
mybut2.grid(row=1,column=1)
mybut3.grid(row=1,column=2)
mybut4.grid(row=2,column=0)
mybut5.grid(row=2,column=1)
mybut6.grid(row=2,column=2)
mybut7.grid(row=3,column=0)
mybut8.grid(row=3,column=1)
mybut9.grid(row=3,column=2)
mybut0.grid(row=4,column=0)
mybut_equals.grid(row=3,column=3)
mybut_add.grid(row=1,column=3)
mybut_clear.grid(row=4,column=1)
mybut_prod.grid(row=2,column=3)
mybut_div.grid(row=4,column=2)
mybut_sub.grid(row=4,column=3)
mybut_sq.grid(row=5,column=3)

win.mainloop()


















