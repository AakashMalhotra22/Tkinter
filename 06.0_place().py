from tkinter import*
'''
place:
1. To use place consider the window as coordinate axis.
2. It has basic four options:
   1. x- Tells the x point
   2. y- Tells the y point
   3. width = Set the width of the label
   4. height = Set the height of the label 
   
   From above, atleast you need to write either x value or y value, otherwise nothing appears on the screen.
   If you write only x value, then it will consider y value as zero and vice versa.
'''

root = Tk()
root.title("place")
root.geometry("400x500")
# Label1
l1 = Label(root, text="one", border=5, relief="sunken",bg="red")
l1.place(x=0,y=0, width=100, height=125)

# Label 2
l2 = Label(root, text="two", border=5, relief="sunken",bg="blue")
l2.place(x=110,y=300, width=100, height=125)


'''place option:
1. Anchor:
   a. It has following option: n,w,e,s,nw,sw,ne,se.
   b. Default is CENTER.
    
'''

root.mainloop()
