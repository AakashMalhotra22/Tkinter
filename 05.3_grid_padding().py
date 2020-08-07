from tkinter import*
'''
Padding:
There are four padding options:

1. ipadx: It increases the width of the background.
2. ipady: It increases the height of the background.
3. pady: 1. It creates the gaps of x units below and above of the label.
         2. If you apply pady to one label of a row, then it will apply to all the labels present in the row.
         
         
4. padx: 1. It creates the gaps of x units left and right of the label.
         2. if you apply padx to one label of a oolumn, it will apply to all the labels of the column.

'''



root = Tk()
root.geometry('400x400')

my_label1 = Label(root, text = "label1", bg = "red")
my_label1.grid(row=1, column=1, pady=10, padx=10, ipady=10, ipadx=10)

my_label1 = Label(root, text = "label2", bg = "green")
my_label1.grid(row=1, column=2,)

my_label1 = Label(root, text = "label3", bg = "cyan")
my_label1.grid(row=2, column=1)

my_label1 = Label(root, text = "label4", bg = "yellow")
my_label1.grid(row=2, column=2)

root.mainloop()