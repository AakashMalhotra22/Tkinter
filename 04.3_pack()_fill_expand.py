#4 fill:Y and expand
from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(fill=Y) # fills along y-axis.
label2 = Label(root, text="red", fg ="white", bg="red", font=("",25))
label2.pack( fill=Y, expand=True) # Here expand will use all the y-axis size.


root.mainloop()
