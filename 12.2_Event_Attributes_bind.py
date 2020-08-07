from tkinter import *

root = Tk()
root.title("Binding keys")
root.geometry("400x500")
'''
Event_Attributes:
1. when you make a callback function of an event which is handler then you write
   def callback(event) Here this event has  many attributes which you can use.

A. widget: event.widget - This gives the name of the widget which generated it, like if you use button widget.

B. x,y:  event.x or event.y- The gives current mouse position.

C. x_root, y_root: event.x_root or event.y_root: This gives current mouse position with respect to upper left corner.

D. char: event.char: This gives char which you have pressed, like a.

E. keysym: event.keysym: Stand for keysymbol.

F. keycode: event.keycode: Each key has code and it gives that.

G. num:  event.num: It gives which mouse button you have pressed, if leftmost then answer is 1.

H. type: event.type: It gives the type of event such as key_stroke or anything.
'''


# Example

# This is callback function
def callback1(event):  # Here only use events as parameter.
    label = Label(root, text=f" Lets do some anyalysis:"
                             f"\n event.widget means widget is {event.widget} "
                             f"\n event.x is {event.x} and event.y is {event.y}, this is current mouse position"
                             f"\n event.x_root is {event.x_root} and event.y_root is {event.y}"
                             f"\n char you entered is '{event.char}' represented by event.char"
                             f"\n keysymbol is {event.keysym}"
                             f"\n keycode is {event.keycode}"
                             f"\n mouse button num is {event.num}"
                             f"\n event type is {event.type}", bg="pink", justify="left").pack(pady=20)





# This is button
b1 = Button(root, text="clickme", )

# change event here to see different results
b1.bind('<Return>', callback1)
b1.pack(pady=10)


root.mainloop()