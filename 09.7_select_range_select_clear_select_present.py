from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Methods of the Entry widgets. 
Here e corresponds to Entry widget just for explanation

1. select_range()     1. e.select_adjust(start,end)
                      2. Same as selection_range()
                      3. It select all the characters in the given range.

2. select_present()   1. e.select_present()
                      2. Same as selection_present()
                      3. It just prints true if there is any selection in the entry widget.

3. select_clear()    1. e.select_clear()
                      2. Same as selection_clear()
                      3. Clears all the selection, if there is any.

'''


# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes


def select_func():
    e.select_range(3,7)
    label = Label(root,text=f"text is selected in range(3,7)\n it is {e.select_present()} that text is selected", fg="red").pack(pady=10)


def clear_func():
    e.select_clear()
    label = Label(root,text="The selected text gets cleared..", fg="red").pack(pady=10)

label = Label(root, text="write a word of 8 words and then\n cick select button followed by clear button.", bg="pink",
              fg="blue", width="50", height="5").pack(pady=19)

button1 = Button(root, text='select', command=select_func).pack(pady=10)
button2 = Button(root, text='clear', command=clear_func).pack(pady=10)


e = Entry(root, width=25, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4",
          selectforeground="yellow")
e.pack(ipady=30, ipadx=14, padx=13)


root.mainloop()