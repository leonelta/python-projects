from tkinter import *

cal = Tk()
cal.title("Calculator")
operator = ""
text_Input = StringVar()

txtDisplay = Entry(cal, textvariable=text_Input, font=('arial', 20, 'bold'), bd =30,
                   insertwidth = 4, bg = "powder blue", justify= 'right' ).grid(columnspan = 4)

btn7 = Button(cal, padx=16, fg="black",  font=('arial', 20, 'bold'),
              text = "7").grid(row =1, column =0)
cal.mainloop()