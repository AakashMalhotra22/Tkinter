from tkinter import*

'''
Grid options:

1. Sticky: 1. The widgets are centered in their cells by default, to change it use n,s,e,w,ne,nw,se,sw.
           2. It is  same as anchor. 
           3. w+e means that the widget will be stretched horizontally to fill the whole cell.
           4. w+e+n+s measn that widget will be stretched to fill whole space
           
'''

root = Tk()
root.geometry('500x500')

my_label1 = Label(root, text="Sticky: changing the position", font=("",20) )
my_label1.grid( row=0, column=1)


my_label1 = Label(root, text="centering towards the west",bg = "red" )
my_label1.grid(sticky="w", row=1, column=1)

my_label2 = Label(root, text="centering towards the east",bg = "green" )
my_label2.grid(sticky="e", row=2, column=1)

my_label3 = Label(root, text="centering towards the north",bg = "cyan" )
my_label3.grid(sticky="n", row=3, column=1)

my_label3 = Label(root, text="centering towards the south",bg = "blue" )

my_label3.grid(sticky="s", row=4, column=1)

root.mainloop()