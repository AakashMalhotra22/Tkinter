#5 fill: BOTH and expand

from tkinter import*


root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(fill=BOTH, expand=False)
label2 = Label(root, text="red", fg ="white", bg="red", font=("",25))
label2.pack( fill=BOTH, expand=True) # Here expand will help use all the remaining space.


root.mainloop()
