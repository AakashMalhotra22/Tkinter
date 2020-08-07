#3 fill= X and expand

from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(fill=X) # fills along x-axis.
label2 = Label(root, text="red", fg ="white", bg="red", font=("",25))
label2.pack( fill=X) # fills along x-axis
label3 = Label(root, text="green", fg ="white", bg="green", font=("",25))
label3.pack(fill=X, expand=True) # Here expands act as pady.


root.mainloop()
