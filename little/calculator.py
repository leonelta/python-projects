from tkinter import *

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, textvariable=text_Input, font=('arial', 20, bold), bd =30,
                   insertwidth = 4, bg = "powder blue", justify= 'right' )