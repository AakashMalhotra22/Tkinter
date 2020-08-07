from tkinter import*
root = Tk() # Instance root of class Tk() which produces object as output
root.title("text variables in label")
root.geometry("500x500")
'''
textvariable:
1. It is used to change text in label.
2. It is used in place of text in labels.
3. You can either choose text or text variable option in label.
4. syntax:
   v1 = StringVar() - Creates text variable
   v1.set("a")- Assign values of v1 to str"a".
   v1.get() - prints out the value of v1.
'''


var = StringVar() # Instance var of class StringVar()

'''Here var is just a text variable, which is just created and has no value, it only accepts string.'''
var.set("ram")
print(var.get())


my_label3 = Label(root, fg ="yellow",bg ="blue", font =("",20),textvariable= var)
'''Here you can either use text or textvariable, and if you use both then the text will be given preference.'''
my_label3.pack()


# Changing value in my_label3
def func():
    global var
    var.set(var.get()+" ji")
    my_label3.pack()


y = Button(root, text="Click to change!", bg = "black", fg ="white", border ="10", relief ='raised', command = func)
y.pack(pady =10)

root.mainloop()