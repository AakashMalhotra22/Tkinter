# Here we would use all the Event formats in a widget.

from tkinter import *

root = Tk()
root.title("Binding keys")
root.geometry("400x300")
'''

syntax is widget.bind(event, handler)

Event format: 

1. <Button-1>: Refers to mouse leftmost button. (<Button-3> refers to the rightmost button.)
     so when you press down the leftmost button of mouse over the widget in which you you have bind this, it would 
     automatically invoked the callback function which you have set.
     For example: if you have button widget, then just take mouse over it and press leftmost button of mouse.

2. <B1-Motion>: The mouse is being moved over the widget, with button being held down, same for <B3-Motion>.

3. <ButtonRelease-1>: When the button-1 or leftmost button of mouse is released over the widget. 

4. <Double-Button-1>: Button-1 or leftmost button is clicked twice over the widget.

5. <Enter>: The mouse pointer enters the widget, dont confuse it with keyboard enter key

6. <Leave>: The mouse pointer leaves the widget, 

7. <FocusIn>: The keyboard focus is moved to this widget.

8. <FocusOut>: The keyboard focus is taken from this widget.

9. <Return>: When enter key of keyboard is pressed when this widget has focus.
             # When you use root.bind(<Return>,callback), then there is no need of focus, beacuse root means whole window
             # so it already has focus.

10. <a>:  keyboard key, same for each character.
11. 1:    keyboard numbers, no need to use angle braces.

12. <F1>:   keyboard F keys same for others. 
13. <space>: space key

14. <Left> : for arrow keys, same are Right, Down, Up
14. search remaining keys online if you need.
'''

label = Label(root)
label2 = Label(root)
# Here we have created many function for different events.
def callback1(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have pressed number key\n which is 1", bg="red")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback2(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have pressed alphabet key\n which is a", bg="blue",fg="white")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback3(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have pressed down key", bg="yellow")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback4(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have pressed F keys\n which is F1", bg="pink")
    label.grid(row=4, column=1, padx=30, pady=10)


def callback5(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have pressed space key", bg="green")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback6(event):
    global label2
    label2.grid_forget()
    label2 = Label(root, text="You have taken keyboard focus over this button", bg="black", fg="white")
    label2.grid(row=5, column=1, padx=30, pady=10)

def callback7(event):
    global label2
    label2.grid_forget()
    label2 = Label(root, text="You have taken away keyboard focus\n from this button", bg="red", fg="white")
    label2.grid(row=5, column=1, padx=30, pady=10)

def callback8(event):
    global label
    label.grid_forget()
    label = Label(root, text="You have double clicked the button", bg="blue", fg="white")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback9(event):
    global label
    label.grid_forget()
    label = Label(root, text="Mouse cursor enters the button", bg="pink", fg="black")
    label.grid(row=4, column=1, padx=30, pady=10)

def callback10(event):
    global label
    label.grid_forget()
    label = Label(root, text="Mouse cursor left the button", bg="purple", fg="white")
    label.grid(row=4, column=1, padx=30, pady=10)



b1 = Button(root, text="clickme", )

b1.bind('1', callback1)
b1.bind('<a>', callback2)
b1.bind('<Down>', callback3)
b1.bind('<F1>', callback4)
b1.bind('<space>', callback5)
b1.bind('<FocusIn>', callback6)
b1.bind('<FocusOut>', callback7)
b1.bind('<Double-Button-1>', callback8)
b1.bind('<Enter>', callback9)
b1.bind('<Leave>', callback10)


b1.grid(row=1, column=1, padx=100, pady=10)


b2 = Button(root, text="no use button")
b2.grid(row=2, column=1, padx=100, pady=10)

root.mainloop()