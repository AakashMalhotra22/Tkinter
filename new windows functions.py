# First way to create a window
from tkinter import*

root = Tk()
root.geometry('500x500')

#Create second
def newwindow():
    y = Toplevel()
    y.title("Second Window")


    label = Label(y, text="Look at my new window!!!").pack()
    # Destroy new window

    destroy_button = Button(y, text="quit", command=y.destroy).pack()

    # Maximize and Minimize button for main window

    minimize_button = Button(y, text="Minimize new window", command= root.iconify).pack(pady=10)
    maximize_button = Button(y, text="Maximize new window", command= root.deiconify).pack(pady=10)

    # Withdraw new window:
    withdraw_button = Button(y, text="withdraw new window", command=root.withdraw).pack(pady=10)
    rewithdraw_button = Button(y, text="rewithdraw new window", command=root.deiconify).pack(pady=10)

    # Destroy new window

    destroy = Button(y, text = "destroy main window", command =root.destroy).pack(pady=10)

    y.mainloop()



but = Button(root, text="click me", command = newwindow)
but.pack()
root. mainloop()