# First way to create a window
from tkinter import*

root = Tk()
root.geometry('500x500')

#Create second
def newwindow():
    y = Toplevel()
    y.title("Second Window")
    y.geometry("300x200")

    label = Label(y, text="Look at my new window!!!").pack()
    y.mainloop()


but = Button(root, text="click me", command = newwindow)
but.pack()
root. mainloop()