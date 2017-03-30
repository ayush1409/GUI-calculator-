# CALCULATOR

from tkinter import *
root = Tk()
root.title("Calculator")

def btnclick(number):
	global operator
	operator = operator + str(number)
	text_input.set(operator)

def btncleardisplay():
	global operator
	operator = ''
	text_input.set("")

def btnequal():
	global operator
	sumup = str(eval(operator))
	text_input.set(sumup)
	operator = ""


text_input = StringVar()
operator = ""
text_display = Entry(root, textvariable = text_input, font = ('arial',20,'bold'),bg = 'powder blue',
						bd = 5, justify = 'right' ).grid(columnspan = 4)

# ***********************************************************************
btn7 = Button(root, text = '7',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(7)).grid(row = 1, column = 0)
btn8 = Button(root, text = '8',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(8)).grid(row = 1, column = 1)
btn9 = Button(root, text = '9',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(9)).grid(row = 1, column = 2)
btnadd = Button(root, text = '+',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick("+")).grid(row = 1, column = 3)

#************************************************************************
btn4 = Button(root, text = '4',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(4)).grid(row = 2, column = 0)
btn5 = Button(root, text = '5',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(5)).grid(row = 2, column = 1)
btn6 = Button(root, text = '6',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(6)).grid(row = 2, column = 2)
btnsub = Button(root, text = '-',padx = 19,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue",command = lambda:btnclick("-")).grid(row = 2, column = 3)

#************************************************************************
btn1 = Button(root, text = '1',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(1)).grid(row = 3, column = 0)
btn2 = Button(root, text = '2',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(2)).grid(row = 3, column = 1)
btn3 = Button(root, text = '3',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(3)).grid(row = 3, column = 2)
btnmul = Button(root, text = '*',padx = 18,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick("*")).grid(row = 3, column = 3)

#************************************************************************
btn0 = Button(root, text = '0',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick(0)).grid(row = 4, column = 0)
btnclear = Button(root, text = 'C',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = btncleardisplay).grid(row = 4, column = 1)
btnequal = Button(root, text = '=',padx = 16,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue",command = btnequal).grid(row = 4, column = 2)
btndiv = Button(root, text = '/',padx = 18,pady = 16, font = ('arial',20,'bold'), bd = 8, 
	fg = 'black', bg = "powder blue", command = lambda:btnclick("/")).grid(row = 4, column = 3)
#root.geometry("300x300")
root.mainloop()	