from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.geometry("900x500")

'''
text widget:
1. syntax: Text(root,**options)
2. It is same as entry box but here you can add more than one line and have more options.
'''

# Simple Example of TextWidget
y = Text(root, height=15, width=40)
y.pack()


root.mainloop()