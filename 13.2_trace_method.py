from tkinter import*
root = Tk()

'''
trace method
1. This method is used to trigger a function, whenever there is a change in variables of tkinter occurs.
   variable can be StringVar(), IntVar(), BooleanVAr(), DoubleVar()
2. syntax:
   var.trace(mode, callback_function_name)
   Here in place of mode you can use "w", "r" and "u", w means write, r means read and u means unset

'''

# Example:
'''Here we are associating StringVar with entry widget, so if there is any changes in entry widget, it would automatically calls a function'''

def callback(*args):
    y = Label(root, text="jai shri ram")
    y.pack(pady=10)

var = StringVar()

'''Use either of the two way.'''
var.trace("w", callback)#Ist way
#var.trace("w", lambda name, indx, mode, var=var: callback(var)) # 2nd way

e = Entry(root,textvariable=var).pack()





root.mainloop()