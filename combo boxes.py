from tkinter import *
from tkinter import ttk


root = Tk()
root.geometry("500x500")
options = ["Ram", "Shyam", "Neena"]

my_combo = ttk.Combobox(root, value= options)
my_combo.current(1)
my_combo.pack(pady=10)

def Select():
    my_label=Label(root, text=my_combo.get())
    my_label.pack()

but = Button(root, text="Select", command=Select).pack()

root.mainloop()