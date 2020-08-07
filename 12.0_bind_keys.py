from tkinter import *

root = Tk()
root.title("Binding keys")
root.geometry("400x700")
'''
Bind keys:
1. for each widget bind method is used to bind any event(means keypress, mouse movement, mousepress, etc) to function
   and methods, widget can be a button, label, or even the frame or parent window.
   for example: if you press key -a, then that button is invoked or any function is triggered.

2.  syntax is widget.bind(event, handler)


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

10. <a>:  keyboard key, same for each character,
          #Note: Here caplock matters, so difference in A and a
          
11. 1:    keyboard numbers, no need to use angle braces.

12. <F1>:   keyboard F keys same for others. 
13. <space>: space key

14. <Left> : for arrow keys, same are Right, Down, Up
14. search remaining keys online if you need.
'''


# Example

# This is callback function
def callback1(event):  # As an argument, you can pass either *args or event which is neccesary
    label = Label(root, text="You have pressed Enter key", bg="green").pack(pady=10)


# This is button
b1 = Button(root, text="clickme", )

# This is bind method which acts over widget b1, using <Return> event means enter of keyboard and call function callback1
b1.bind('<Return>', callback1)
b1.pack(pady=10)


# Make sure always pack the button after binding.
# One more thing focus should be on the button when you are pressing Enter key.


# Example-2

def callback2(*args):  # Last time in case of callback1 we used events, so we are using *args here
    label = Label(root, text="You have pressed alphabet a", bg="red").pack(pady=10)


# Here the widget is root, means whole parent window means the main window, so you can press alphabet a from anywhere in
# parent window this would work.
root.bind('<a>', callback2)

root.mainloop()