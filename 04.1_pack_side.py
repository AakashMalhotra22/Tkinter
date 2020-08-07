#2 side

from tkinter import*

root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(side='top')
label2 = Label(root, text="red", fg ="white", bg="red", font=("",25))
label2.pack(side="left")
label3 = Label(root, text="green", fg ="white", bg="green", font=("",25))
label3.pack(side ="right")

label4 = Label(root, text="yellow", fg ="white", bg="yellow", font=("",25))
label4.pack(side ="bottom")


root.mainloop()
