#5 grid_configure()
'''
1. This is used to update any of the options of the grid.
2. It's syntax is label.grid_configure()
'''

from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.grid(row=1,)
label1.grid_configure(ipady=10, ipadx=19 )

root.mainloop()
