from tkinter import*
root = Tk()
root.title("Tkinter variables...")

'''
Tkinter variables:
1. tkinter supports some variables which are used to manipulate the value in tkinter.
2. There are total four variables:
    
    a. BooleanVar(): For boolean values, 0,1, True, False
    b. StringVAr(): For strings
    c. IntVar(): For Integers.
    d. DoubleVar(): For floating values, 1.0, 0.2

3. These methods supports the following methods.
   A. set(): To set the value of the variable.
   B. get(): To retrieve the value of the variable.
   C. setvar(): Another way to set the value of the variable.
   D. getvar(): Another way to get the value of the variable.
   
4. Common syntax is: 
  var(you can use any other name also) = Variable_name(StringVar,IntVar,..)(main_window, value= any_value, name =)
  Ex:
  var = StringVar(root, value="aakash", name="strings")# here this name is used in setvar() and getvar()
  or you can avoid parameters
  var = StringVar()
  
5. Difference between:
   var= StringVar()# here by default, this var would link to main top level window
   var = StringVAr(root) # here this var would link to only root window.
   
'''


#Example1:

var = StringVar()
var.set("HI")
print(var.get())

# Example:2
var1 = IntVar()
var1.set(5)
print(var1.get())


# Example:3
var2 = BooleanVar()
var2.set(1)
print(var2.get())


# Example:4
var3 = DoubleVar()
var3.set(1)
print(var3.get())


# Example-5
# No need of set function
var4 = StringVar(root,value="aakash")# Here you have linked it with root window.
var5 = IntVar(value="50")# Here there is no root used, means  top level window is used.

print(var4.get())
print(var5.get())
print(" ")


#Example-6
'''getvar() and setvar() method '''

var6 = StringVar(root,name="string")
var7  = IntVar(root,name="integer")

root.setvar(name="string", value="jai shri ram")
print(root.getvar(name="string"))

root.setvar(name="integer", value=1000)
print(root.getvar(name="integer"))


root.mainloop()
