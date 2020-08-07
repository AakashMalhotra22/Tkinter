from tkinter import *

root = Tk()
root.geometry('200x800')

#In this we are using both validate and invalidate command.


# Step1 callback function of validate command
def callback(inp, P, d, s, i, v, V, W):

    if inp.isdigit():
        return True
    elif inp == "None":
        return True
    elif inp in "abcdefghijklmmnopqrstuvwxyz":
        return False
    else:
        return True

# callback function for invalidcommand.
def func():
    label =Label(root, text="jai shri ram").pack(pady=6)

# Main Entry widget.
e = Entry(root)

#Step2 Registering the validate callback function
reg = root.register(callback)

#Step2- Registering the invalidate callback function
reg1 = root.register(func)

# Using, validate, invalidatecommand and validatecommand
e.config(validate="key",invalidcommand=reg1, validatecommand=(reg, "%S", '%P', '%d', '%s', '%i', '%v', '%V', '%W'))
e.pack()

# Creating another entry widget
e2 = Entry(root).pack(pady=10)

'''
Here whenever any keystroke is pressed in e entry widget, then validatecommand is triggered and anything else if happened
then invalidcommand is triggered as we have restricted alphabets in the entry widge, so when you try to write alphabets in
entry widget then invalidcommand callback is triggered.
'''

root.mainloop()
