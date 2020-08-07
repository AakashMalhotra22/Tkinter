from tkinter import*

root = Tk()
root.title("Radio buttons")

#changing variable

v = IntVar()


#v.set(1) This will already select the option one.


rbutton1 = Radiobutton(root, text ="one", variable=v, value=1)
rbutton2 = Radiobutton(root, text="two", variable=v, value=2)

def func1():
    if v.get()==1:
        my_label = Label(root, text="You clicked radio button one!")
    else:
        my_label = Label(root, text="You clicked radio button two!")
    my_label.pack(pady=5)


rbutton1.pack()
rbutton2.pack(pady=20)

my_button = Button(root, text="click me", command = func1)
my_button.pack(pady=4)

root.mainloop()
