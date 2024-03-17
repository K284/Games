from tkinter import *
cal = Tk()
cal.title("Calculator")
t = StringVar()
o = ""

def btn(num):
    global o
    o+=str(num)
    t.set(o)

def clearC():
    global o
    o = ""
    t.set(o)

def final():
    global o
    f = str(eval(o))
    t.set(f)
    o = ""    


#1 ST ROW
textdisplay = Entry(cal, font =("arial",20,"bold"),textvariable = t, bd = 30, insertwidth = 4, bg = "powder blue", justify = "right").grid(columnspan = 4)
b7 = Button(cal,text = "7",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(7)).grid(row = 1, column = 0)
b8 = Button(cal,text = "8",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(8)).grid(row = 1, column = 1)
b9 = Button(cal,text = "9",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(9)).grid(row = 1, column =2)
add =  Button(cal,text = "+",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn('+')).grid(row = 1, column = 3)

#2 ND ROW
b4 = Button(cal,text = "4",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(4)).grid(row = 2, column = 0)
b5 = Button(cal,text = "5",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(5)).grid(row = 2, column = 1)
b6 = Button(cal,text = "6",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(6)).grid(row = 2, column =2)
sub =  Button(cal,text = "-",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn('-')).grid(row = 2, column = 3)

#3 RD ROW
b1 = Button(cal,text = "1",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(1)).grid(row = 3, column = 0)
b2 = Button(cal,text = "2",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(2)).grid(row = 3, column = 1)
b3 = Button(cal,text = "3",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(3)).grid(row = 3, column =2)
mul =  Button(cal,text = "*",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn('*')).grid(row = 3, column = 3)

#4 TH ROW
b0 = Button(cal,text = "0",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn(0)).grid(row = 4, column = 0)
bC = Button(cal,text = "C",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: clearC()).grid(row = 4, column = 1)
equal =  Button(cal,text = "=",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: final()).grid(row = 4, column = 2)
div = Button(cal,text = "/",bd = 8, fg = "black", bg = "powder blue", padx = 16, pady = 16, font = ("arial", 20, "bold"), command = lambda: btn('/')).grid(row = 4, column = 3)

