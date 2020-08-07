from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")
'''
text variable and state....

1. state: 1. There are three states
          A. state=normal: It is default state, when it's on the window then the widget is said to be on normal state.
          B. state=disabled: This state makes the widget unresponsive and not editable.
          c. Active: When the cursor is over the Entry widget then that state is called active state.


2. textvariable: 1. It is used to retreive text from the entry widget, it can be used in place of e.get
                 2. first create
                    var = StringVAr()
                    then use textvariable=var
                    then var.get()

'''

# textvariable: 1. Another way of retrieving what is written in entry widget.
 #              2. By use of this, you can set default text in entry box which appears everytime you run it

var = StringVar()
var.set("ram ji")

def printer():
    label2 = Label(root, text=f"Hello {var.get()}").pack(pady=10)
    # Instead of e.get, we have used var.get()


label = Label(root, text="Enter your name...", bg="pink", fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command=printer).pack(pady=10)

e1 = Entry(root, width=20, font=("Arial", 20), bg="red", fg="yellow", textvariable=var)
e1.pack(ipady=30, ipadx=14, padx=13)


# state:

label2 = Label(root, text="Here is a entry widget which is disabled...", bg="pink", fg="blue", width="50", height="2").pack(pady=40)

e2 = Entry(root, width=20, font=("Arial", 20), bg="red", fg="yellow", state="disabled")
e2.pack(ipady=30, ipadx=14, pady=5)



root.mainloop()