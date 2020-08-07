# First way to create a window
from tkinter import*

root = Tk()
root.geometry('500x500')

def newwindow():
    y = Tk()


but = Button(root, text="click me", command = newwindow)
but.pack()
root. mainloop()