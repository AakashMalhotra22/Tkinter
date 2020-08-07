from tkinter import *
from tkinter import font
root = Tk()
root.geometry("900x500")


def bold_text():
    print("Hi")

b1 = Button(root, text="BOLD", border="10", command=bold_text)
b1.bind('<Control-b>', lambda event,b=b1: b.invoke())# When calling a callback function, always remember, you have to always specify event attribute.
b1.pack(pady=10)


root.mainloop()