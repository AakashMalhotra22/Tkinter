from tkinter import*

'''
1. focus_set()
   a) This is used to set the focus on particular button.
   b) You can set focus at one particular button.
   c) The color of the focus is same as color of th fg.

2. focus_get()
   a) This is used to get which button has focus. 
   b) These option is not limited to button, you can use it on labels, check boxes, everywhere.

'''

root = Tk()
root.title("focus_set()")
root.geometry('400x400')


button1 = Button(root, text="set_focus button", bg="red", fg="yellow")

button1.focus_set()
button1.pack()
'''You  have to apply focus_set() before packing the button on screen as above.'''


button2 = Button(root, text ="not set_focus button").pack(pady=10)

# focus_set()

y = root.focus_set()
print(y)

print(f"The focus set button is {y}")

root.mainloop()