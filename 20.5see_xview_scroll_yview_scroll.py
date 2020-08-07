from tkinter import*
root = Tk()
root.geometry("900x500")

'''
Methods of view:

1. see(index)                 A. It makes sure particular index appears on the screen.
2. xview_scroll(number,what)        A. The amount of shift horizontally, what can be in UNITS.
3. yview_scroll(number,what)        A. The amount of shift vertically, what can be in UNITS.

4. xscrollcommand and yscrollcommand  A. These are used to create horizontal and vertical scroll bar.
                                      B. Discuss later.

'''

def func1():
    #This would make sure index 1.1 appears on the screen.
    y.see(1.1)

def func2():
    # This would do horizontal movement from left to right
     y.xview_scroll(10, UNITS)

def func3():
    # This would do vertical movement from downwards to upwards.
     y.yview_scroll(-10, UNITS)



y = Text(root,bg="pink", fg="blue", height="6", width="40" , cursor="dot",border="1")
y.pack(pady=10)



b1 = Button(root, text="see button",border="10", command=func1).pack(pady=10)

b2 = Button(root, text="xview_scroll",border="10", command=func2).pack(pady=10)

b3 = Button(root, text="yview_scroll button",border="10", command=func3).pack(pady=10)

root.mainloop()