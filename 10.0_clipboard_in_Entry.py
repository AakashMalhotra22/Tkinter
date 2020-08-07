from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("500x600")

'''
Methods of the Entry widgets. 

1. e.clipboard_get(): It just prints out whatever is copied last time and from where it was copied either from pycharm
                      entry widget or anywhere.
                      
2. e.clipboard_clear(): It clear whatever is in the clipboard.
3. e.clipboard_append(): It appends a string to the clipboard which you assign.

'''


# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes.
# Here we also use grid.pack_forget system.

label =Label(root)

# e.delete() and e.index(INSERT)
def clipboard_get():
    global label
    label.grid_forget()
    # if there is nothing in clipboard, then it may give error.
    try:
        label = Label(root, text=f"{e.clipboard_get()} is in the clipboard", fg="red")
        label.grid(row=6, column=1, pady=20, padx=30)
    except:
        pass

def clipboard_clear():
    global label
    label.grid_forget()
    e.clipboard_clear()
    label = Label(root,text=f"clipboard is emptty, try it by using clipboard_get_button", fg="red")
    label.grid(row=6, column=1, pady=20, padx=30)

# it just add to clipboard whatever is in the entry box
def clipboard_append():
        global label
        label.grid_forget()
        e.clipboard_append(e.get())
        label = Label(root,text=f"{e.get()} is added to clipboard, check it by use of clipboard_get button", fg="red")
        label.grid(row=6, column=1, pady=20, padx=30)



label1 = Label(root, text="Write anything and click button to see magic\n write anything of atleast 8 words", bg="pink",
              fg="blue", width="50", height="5").grid(row=1, column=1, pady=10, padx=30)

button1 = Button(root, text='clipboard_get', command=clipboard_get).grid(row=2, column=1, pady=10, padx=30)

button2 = Button(root, text='clickboard_clear', command=clipboard_clear).grid(row=3, column=1, pady=10, padx=30)

button3 = Button(root, text='clickboard_append', command=clipboard_append).grid(row=4, column=1, pady=10, padx=30)

e = Entry(root, width=2, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4",
          selectforeground="yellow")
e.grid(row=5, column=1,ipady=30, ipadx=14, padx=30)


# e.config()
e.config(width=25)

root.mainloop()