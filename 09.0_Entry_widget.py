from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("400x600")
'''
Entry widget:
1. These are the widgets which are used to assign single line widget from the users.
2. for more than one line of code, use text widget.
3. The syntax is Entry(master, option...)
4. master represents the parent windows.
'''




def printer():

    label2= Label(root, text=f"Hello {e.get()}").pack(pady=10)
    '''e.get() is used to get what is written in the entry widget.'''


label1 = Label(root, text='This is basic example of entry widget,\n  just write anything and press button', bg="pink", fg="blue", width ="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command =printer).pack(pady=10)

e = Entry(root, width=20,font=("Arial",20), bg="red",fg= "yellow",border=5, relief= "sunken" )
e.pack(ipady=30, ipadx=14, padx=13)


root.mainloop()