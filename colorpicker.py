from tkinter import *
from tkinter import colorchooser

root = Tk()
root.title("color_chooser")
root.geometry('600x500')
def color():
    my_color= colorchooser.askcolor()[1]
    my_label = Label(root, text=my_color).pack(pady=10)

    my_label2= Label(root, text = "You have chosen a color!!!", font = ("",32), fg=my_color).pack()


my_button = Button(root, text="Pick a color", command=color).pack()
root.mainloop()