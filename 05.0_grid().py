from tkinter import*
'''
grid way:
1. It is another way to pack your label on screen.
2.Just consider  master window as a grid paper sheet with each row and column numbered.
3. If you don't write any row and column, then grid system by default selects the 1 column and empty row.
'''

root = Tk()

root.title("grid system")

my_label = Label(root, text="To use grid system\n think of rows and column\n it is row 1 and column0", bg="white", fg="blue")
my_label.grid(row=1, column=0)# It will pack the label on row 1 and column0

my_label1 = Label(root, text="row2 and column=0", bg="white", fg="red")
my_label1.grid(row=2, column=0,)

my_label1 = Label(root, text="row-1 and column-2", bg="white", fg="green")
my_label1.grid(row=1, column=2)

my_label1 = Label(root, text="row-3 and column-5\n as there is no column 3 and column4 so column5 acts as column3", bg="white", fg="pink")
my_label1.grid(row=3, column=5,)

my_label1 = Label(root, text="No row and column is assigned\n so automatically chooses column 1 and  next empty row", bg="white", fg="cyan")
my_label1.grid()


root.mainloop()