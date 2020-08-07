from tkinter import *


root = Tk()
#root.geometry('300x300')


def yk():
    y3.grid(row=1, column =0, columnspan = 2, padx=20, pady=20)


def y1k():
    y3.grid_forget()




y = Button(root, text="show", command = yk, bg = "blue", fg="red", border = 12, relief ="sunken" )
y2 = Button(root, text="hide", command = y1k, bg = "blue", fg="red", border = 12, relief ="sunken" )
y.grid(row=0,column=0)
y2.grid(row=0,column=1)

y3 = Frame(root, bg="yellow", width=100, height=100, relief ="sunken", bd =10)
y3.grid(row=1, column =0, columnspan = 2, padx=20, pady=20)

my_frame = Label(y3, text="Aakash", bg ="green", fg="white", font=("Arial",32))
my_frame.pack()

root.mainloop()