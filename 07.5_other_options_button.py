from tkinter import*
root = Tk()
root.title("other options button")
root.geometry('400x400')

'''

Button options
1. padx and pady:
  a) It provides internal padding.
  b) padx- Additional padding from left to right of the text.
  c) pady- Addition padding from top to bottom of the text.


2. config option:
 a) It is used to modify any of the option of the button.
 b) syntax is config(**options)

'''

# Using padx and pady
b1 = Button(root, text="click me",padx=100, pady=50, bg='blue',border=10)

#using config to change the options or add new.
b1.config(bg="red", fg="yellow")
b1.pack()



root.mainloop()