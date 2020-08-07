from tkinter import*


root = Tk()
root.title("checkboxes!!!")
root.geometry("500x500")
#check boxes
v = StringVar()
y = Checkbutton(root, text="cheeze", variable=v, onvalue="1", offvalue="2")
y.deselect()
y.pack()

def func1():
    if v.get()=="1":
        my_label = Label(root,text="You wannt cheeze....")

    else:
        my_label = Label(root, text="You dont wannt cheeze....")
    my_label.pack(pady=10)

my_button = Button(root, text = "Select Toppings", command = func1).pack()


root.mainloop()