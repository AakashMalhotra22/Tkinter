from tkinter import*
from tkinter import messagebox

root =  Tk()
root. geometry('500x500')
#Types of pop up boxes
#1. showinfo 2. showwarning 3. showerror 4. askquestions  5. askokcanel   6. askyesno


def popupfunction():
    response = messagebox.showerror("Pop up", "Look at  this issue!!!")
    my_label = Label(root, text=response).pack()




y = Button(root, text="pop button", bg = "red", fg = "yellow", font=("",16), relief = "sunken", command=popupfunction)
y.pack(pady=10)



root.mainloop()