from tkinter import*

'''
There are two types of span
1. rowspan: It is used to span multiple rows at a time, default is 1.

2. columnspan:  It is used to span multiple column at a time, default is 1. 
'''

root = Tk()
root.geometry('400x400')
# Spanning two column
label1 = Label(root, text="spanning two column")
label1.grid(row=1, column=1, columnspan=2)

label2 = Label(root, text="column 1")
label2.grid(row=2, column=1)

label3 = Label(root, text="column 2")
label3.grid(row=2, column=2)

# Spanning two row
label1 = Label(root, text="spanning two row")
label1.grid(row=3, column=1, rowspan=2)

label2 = Label(root, text="row 1")
label2.grid(row=3, column=2)

label3 = Label(root, text="row  2")
label3.grid(row=4, column=2)


# using both column span and row span

label10 = Label(root, text="spanning two rows\n and two column")
label10.grid(row=5, column=1, columnspan=2, rowspan=2)

root.mainloop()