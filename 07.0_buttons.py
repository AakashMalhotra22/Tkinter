from tkinter import*

'''
buttons:
1. syntax is
  Button(root, options)
2. You can use all the options of the label in button such as fg, bg, relief, font, height, width, anchor, justify, underline, border, wraplength, textvariable 

3. Imp option is state:
   a. It has two options: normal and disabled.
   b. If it is set to disabled, then button is not clickable.
   c. If it is set to normal, which is default option, it is clicable.

3. One more main option is command.
'''

root = Tk()
root.title('buttons')
root.geometry('400x600')

my_button = Button(root, text="button 1", fg= "red", bg= "yellow",).pack()

# Using all the options in this
# Here state is normal by default, so button is clickable.
my_button1 = Button(root, text="button 2 ", fg= "blue", bg= "pink", font=("arial",20), height=2, width =10, relief="raised", border="10").pack(pady=10)

# Same options as above button, but state is disabled so not clickable button.
my_button2 = Button(root, text="button 3", fg= "blue", bg= "pink", font=("arial",20), height=2, width =10, relief="raised", border="10", state="disabled").pack(pady=10)


'''
Using command to assign task to the button
'''

#Making clicked fun

def clicked():
    my_label = Label(root, text = "you clicked button 3", bg = "yellow", fg = "red",font =("",20) ).pack(pady=5)

my_button4= Button(root, text=" button4 func", fg= "green", bg = "yellow", relief ="sunken", border ="10", command = clicked ).pack(pady=5)
# Make sure when you assign a function name in command, don't use parenthesis like clicked(), it should be only clicked
# And if you want to pass parameter to the function, use lambda function in command

# Passing argument in the function

def clicker(num):
    my_label = Label(root, text=f"you have asked for {num}", bg="yellow", fg="red", font=("", 20)).pack()

my_button5= Button(root, text=" button5 func", fg= "green", bg = "yellow", relief ="sunken", border ="10", command = lambda: clicker(51) )

root.mainloop()