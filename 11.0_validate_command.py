from tkinter import*
root = Tk()
root.geometry('200x100')
'''
validate command in Entry widget:
1. It is used to restrict keyboard key entries in the entry box.
2. This process consists of three things.
   A. Create a callback function, it is just a function which checks the text in Entry widget and returns True if the
      text is valid and the text shows on screen and it returns False if text is not valid and text does not show on 
      screen.
      
   B. Registering the callback function, in this we register the callback function by use of register method of parent
      window(root), if you print, it would give a string like 5024221callback,  this character string is used to call
      callback function.
      
   C. After creating a callback function and registering it, now when you call the Entry constructor, use validatecommand 
      and validate option, validatecommand option is used to specify your callback, means as soon as you type anything in
      entry widget, it would call the callback option, and register send the information about callback function to 
      validatecommand.
      
      validate option is used to specify when the callback should be called.
      It has following options:
      1. focus: A. In this validation occurs only when entry widget loses or gets focus, means if you write anything
                   in it nothing happens but if you change the focus, then validation occurs and callback function is called.
                B. written as validate="focus"
                
      2. focusin: A. In this validation occurs only when the entry widget gets focus.
                  B. written as validate ="focusin"
      
      3. focusout: A. In this validation occurs only when the entry widget loses focus.
                   B. written as validate="focusout"
      
      4.key:      A. In this validation occurs only when key stroke is hit.
                  B. written as validate="key"
                  
      5. all:     A. In this validation occurs n all the above cases.
                  B. written as validate="all"
      
      6. none:    A. No validation, default option.

One of the most important things is callback substitution codes to get the details of whatever written in entry widget.
        1. %d = Type of action (1=insert, 0=delete, -1 for others)
        2. %i = index of char string to be inserted/deleted, or -1
        3. %P = value of the entry if the edit is allowed
        4. %s = value of entry prior to editing
        5. %S = the text string being inserted or deleted, if any
        6. %v = the type of validation that is currently set
        7. %V = the type of validation that triggered the callback
             (key, focusin, focusout, forced)
        9. %W = the tk name of the widget

invalidcommand
Entry widgets supports this option also that calls it own callback function whenever validation not occurs.
for example: you have set validate=key, so now if you change the focus, then invalidcomman option triggers its own
callback function.
         
'''
# This is a basic example, in which are restricting the alpahbets from the Entry widget.



# Step1 callback function
def callback(inp,P,d, s,i,v,V,W):
    print(f"inp is {inp}\nd is {d} \ns is {s}\nP is {P}\nv is {V}\nv is {v},W is {W}")
    # This line is written here to understand percentage specifiers.

    if inp.isdigit():
         return True
    elif inp=="None":
        return True
    elif inp in "abcdefghijklmmnopqrstuvwxyz":
        return False
    else:
        return True

# Step-2: Registering the callback function.
reg =root.register(callback)
print(reg)# prints out the character string like 232321callback

# Creating Entry box
e = Entry(root,)

# Step-3 Using validate and validatecommand.
e.config(validate="key", validatecommand=(callback,"%S",'%P','%d', '%s','%i','%v', '%V','%W' ))
e.pack()

root.mainloop()