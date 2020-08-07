#5 pack_configure()
'''
1. This is used to update any of the options of the pack.
2. It's syntax is label.pack_configure()
'''

from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(pady=10)
label1.pack_configure(ipady=10, ipadx=19, fill=X, pady=50)

root.mainloop()
