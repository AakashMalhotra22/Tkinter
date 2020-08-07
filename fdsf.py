from tkinter import *

def callback(sv):
    print (sv.get())
    print(sv.index())


root = Tk()
sv = StringVar(name="ram")
sv.set(['a','b'])
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
e = Entry(root, textvariable=sv)
e.pack()
root.mainloop()