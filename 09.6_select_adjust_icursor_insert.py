from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Methods of the Entry widgets. 
Here e corresponds to Entry widget just for explanation


1. icursor():           1. e.icursor(position)
                        2. Change or set the cursor position of the Entry_widget.
                        3. e.icursor(5) will place the cursor before 5th character of the entry widget.


2. select_adjust()    1. e.select_adjust(index)
                      2. Same as selection_adjust()
                      3. It select all the characters from the 0 index position to the index position you have set.

3. insert():          1. e.insert(index, string)
                      2. It inserts the string at particular index in Entry widget.                        


'''


# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes


# e.icursor(), e.select_adjust(), e.insert()
def printer():
    e.select_adjust(2)
    e.icursor(5)
    e.insert(7,"ram")

    label = Label(root,
                  text=f"ram is inserted at 7th position\n cursor is set at 5th position\n text selected to 2nd position", fg="black").pack(pady=10)


label = Label(root, text="Write anything and click button to see magic\n write anything of atleast 8 words", bg="pink",
              fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command=printer).pack(pady=10)

e = Entry(root, width=25, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4",
          selectforeground="yellow")
e.pack(ipady=30, ipadx=14, padx=13)


root.mainloop()