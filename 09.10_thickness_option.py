from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")
'''
Thickness options

1. highlightbackground : The color of the focus highlight when the widget does not have focus.


2. highlightcolor : The color of the focus highlight when the widget has the focus.

3. highlightthickness: The thickness of the focus highlight, default is 1, make it sure to suppress it.
'''


label = Label(root, text="focus out and focus in between the entry widgets.", bg="pink", fg="blue", width="50", height="5").pack(pady=19)


e1 = Entry(root, width=20, font=("Arial", 20), bg="red", fg="yellow",highlightbackground="yellow", highlightcolor="green", highlightthickness="20")
e1.pack(ipady=30, ipadx=14, padx=13, pady=20)

e2 = Entry(root, width=20, font=("Arial", 20), bg="red", fg="yellow", border="10", highlightbackground="cyan", highlightcolor="blue", highlightthickness="20")
e2.pack(ipady=30, ipadx=14, padx=13, pady=20)




root.mainloop()