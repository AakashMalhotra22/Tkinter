from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Methods of the Entry widgets. 
1. select_from and select_to  1. e.select_from(index) and e.select_to(index)
                               2. same as selection_from() and selection_to()
                               3. It starts selecting from index of select_from to index of select_to()

2. selection_get: It just gives what is selected.

'''


# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes
#selection_get
def printer():
    e.select_from(3)
    e.select_to(5)
    label = Label(root,text="text is selected from index position 3 to index position 5", fg="red").pack(pady=10)
    # It prints out what is been selected.
    label = Label(root, text=e.selection_get()).pack()


label = Label(root, text="Write anything and click button to see magic\n write anything of atleast 8 words", bg="pink",
              fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command=printer).pack(pady=10)

e = Entry(root, width=25, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4",
          selectforeground="yellow")
e.pack(ipady=30, ipadx=14, padx=13)


root.mainloop()