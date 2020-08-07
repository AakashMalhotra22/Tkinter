from tkinter import*
root = Tk()
root.title("after option in tkinter")
root.geometry("500x600")


'''
after:
1. syntax
   after(parent,ms,function=None,*args)
   parent-    name of the parent window, in this case it is root.
   ms-        time in milliseconds
   function - function to be called.
   args -     other option 

2. It is used to call a function after a few milliseconds.

'''


Label1 = Label(root, text="This window is going to be closed in 5 seconds", bg ="yellow", fg="red", padx=10,pady=10)
Label1.pack()

root.after(5000,root.destroy)

#function for time
from time import sleep

var = IntVar()
var.set(5)


Label2 = Label(root, textvariable=var, bg ="black", fg="white", padx=100,pady=100,font=('',100))
Label2.pack(pady=30)


root.after(1000, lambda:var.set(4))
Label2.pack()

root.after(2000, lambda:var.set(3))
Label2.pack()

root.after(3000, lambda:var.set(2))
Label2.pack()

root.after(4000, lambda:var.set(1))
Label2.pack()

root.after(4900, lambda:var.set("Go"))
Label2.pack()


root.mainloop()