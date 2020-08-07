from tkinter import*
'''
default():
1. The default option in tkinter tells the button is the default button in the GUI, for example, the one that is invoked
   automatically when you press Enter or some other keys.
   
2. There is no such option, you need to create it manually.

'''

root = Tk()
root.title("setting default button")
root.geometry('400x400')

# Created the command function of button b1
def ramji():
    print("jai shri ram")

# Created the command function of button b2
def shivji():
    print("omm namhay shivaay")


# Created callback function for the binding.
def callback(*args):
    b1.invoke()

# creating the button
b1 = Button(root, text="click me", command =ramji)

# Here we bind Enter key with whole window, so whenever anyone press, it call the callback function and callback function press the button using invoke option.
root.bind("<Return>", callback)
b1.pack()

'''Another Way by using lambda'''

b2 = Button(root, text ="click me 2", command = shivji)
"Here we are binding key a to button b2, so to use it first take focus on b2, or you can use focus_set() method."
'It will only work if focus is on button 2'

b2.focus_set()
b2.bind('<a>', lambda e, b=b2: b.invoke())

b2.pack()


root.mainloop()
