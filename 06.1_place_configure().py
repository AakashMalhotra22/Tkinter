#5 place_configure()
'''
1. This is used to update any of the options of the place.
2. It's syntax is label.place_configure()
'''

from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",10))
label1.place(x=100, y =100, height=200, width=200)
label1.place_configure(height=50, width=50)

root.mainloop()
