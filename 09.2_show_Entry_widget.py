from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
show: 1. It is used to change the appearance of the character typed by the user in entry box, imagine you are entering
            your password, then at that moment they dont show your password, instead show an asterisk sign.
         2. show="*" This would replace each character by asterisk sign, but when you use e.get() you would get the
            actual text.
'''



def printer():
    label = Label(root, text=f"{e.get()}").pack(pady=10)


label = Label(root, text="Enter your name...", bg="pink", fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='click here to know what you have written...', command=printer).pack(pady=10)

# Here show changes the appearance of the text which you write in Entry widget.
e = Entry(root, width=20, font=("Arial", 20), bg="red", fg="yellow", show="*")
e.pack(ipady=30, ipadx=14, padx=13)

root.mainloop()