from tkinter import*
'''
repeatdelay and repeatinterval:

Normally, a button fires only once when the user releases the mouse button. If you want the button to fire at regular
intervals as long as the mouse button  is held down, set repeatinterval option to a number of milliseconds to be used between repeats
,and set the repeatdelay to the number of milliseconds to wait before starting to repeat.
For example, if you specify “repeatdelay=5000, repeatinterval=1000” the button will fire after 5 second, and every one 
second thereafter , until the user releases the mouse button. If the user does not hold the mouse button down at least 
repeatdelay milliseconds, the button will fire normally.

'''

'''How a button works

To use button, you hover the cursor over it and press left key of the mouse and then release that key, then the button clicks.
In case of repeatdelay and repeatinterval, you have to press the key and not to release it.

'''


root = Tk()
root.title('repeatdelay and repeatinterval')
root.geometry('400x400')


def click(a):
    if a ==1:
        label = Label(root, text="you clicked button 1").pack(pady=3)
    elif a ==2:
        label = Label(root, text="you clicked button 2").pack(pady=3)

b1 = Button(root, text="button1", repeatdelay=2000, repeatinterval=1000, command= lambda: click(1)).pack()
#Here if you hold the left key of mouse on the button, then after 5 sec it starts clicking button and then follow interval of 1 sec.

b2 = Button(root, text = "button 2", command =lambda:click(2)).pack(pady=10)

root.mainloop()