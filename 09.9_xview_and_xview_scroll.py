from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Methods of the Entry widgets. 
Here e corresponds to Entry widget just for explanation


1. xview():            1. e.xview(index)
                        2. It make sure particular index element always appears in the entry widget, what happen 
                           sometimes is that you have a entrywidget which can show 10 characters only and remaining
                           just hides so when you use e.xview(12), then 12 character just appears on the screen at the 
                           0 position and all the character before 12th position letter hides..

2. xview_scroll()      1. e.xview_scroll(number, what)

                        2. Consider a horizontal scroll bar, it is used to scroll horizontally by a give amount,
                           if you use positive for number, then it scrolls all the text in entrywidget from left 
                           to right and if you use negative value for number then it scrolls text in entrywidget 
                           from right to left

                        3. Here what can be UNITS or PAGES, units for scrolling on the basis of character width and pages
                           for scrolling on the basis of entry box size.
'''


# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes


# e.xview() func
def xviewer():
    e.xview(5)
    e.icursor(5)
    label = Label(root,text="The 5th index letter appears at the 0th index position", fg="black").pack(pady=10)


# e.xview_scroll() func
def xviewer_scroll():
    e.xview_scroll(-100,UNITS) # it shifts character 100 units from right to left.

    label = Label(root,text="The entry box is scrolled 100 units from right to left", fg="green").pack(pady=10)


label = Label(root, text="Write anything and click button to see magic\n write anything of atleast 20 words", bg="pink",
              fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='xview', command=xviewer).pack(pady=10)

button1 = Button(root, text='xview_scroll', command=xviewer_scroll).pack(pady=10)


e = Entry(root, width=10, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4",
          selectforeground="yellow")
e.pack(ipady=30, ipadx=14, padx=13)

# e.config()


root.mainloop()