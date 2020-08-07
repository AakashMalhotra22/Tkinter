from tkinter import*
root = Tk()
root.title("Invoke")
root.geometry("400x300")
'''
Invoke():
1. Calling this function is same as clicking the button.
2. It just calls out the command attribute of the button and if there is no command attribute used in the button,
   it returns the empty string.

3. This will not work if button state is disabled.
'''
def ramji():
    print("jai shri ram")

b1 = Button(root, text="click me", command=ramji)
"Now as soon as you run this python file, it would automatically click the button b1"
b1.invoke()
b1.pack()

# Creating button 2 which calls button1 by use of invoke
b2 = Button(text = "click to call button 1", command= lambda b=b1:b.invoke())
b2.pack()

'''Note: If you not use the command =ramji in button, then output is empty string means nothing.'''




root.mainloop()
