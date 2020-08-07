from tkinter import*
root = Tk()
root.title("bind keys")
root.geometry('400x800')



#Example:
'''widget is label, event is enter key'''


def callback(event):
    label = Label(root, text=f"mouse cursor is at {event.x}, {event.y}\n and this is label", bg="red", fg="white").pack(pady=10)


l1 = Label(root, text="Take the mouse over me", fg = "blue", relief ="raised", border="5")
l1.bind('<Enter>',callback)
l1.pack(pady=10)


# Example-2

# widget is parent window which is root, event is alphabet r
def callback1(event):
    label = Label(root, text=f"This is parent window", bg="green", fg="white").pack(pady=10)

root.bind('<r>',callback1)



root.mainloop()
