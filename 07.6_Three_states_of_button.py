from tkinter import*
root = Tk()
root.title("flash")
root.geometry("400x300")
'''
There are total three state of the button.
1. normal: a) This is set when you set button state to normal or by default it is normal.
           b) This include the following options - fg,font,border,bg,etc.
           c) Means when the button is shown in the window what should be it's appearance.

2. disabled a) This is set when you set button state to disabled.
            b) This include following options
               1. disabledbackground - color of the background of the button when the button is disabled. 
               2. disabledforeground - color of the foreground of the button when the button is disabled.
               
            c) This option may not work in this version of tkinter.

3. active  a) This comes in to picture when you take your mouse cursor on to the button.
           b) This include the following options.
           1. activebackground - It would change the background of the button as soon as you press the button.
           2. activeforeground - It would change the foreground of the button as soon as you press the button.
           3. overrelief - It would change the relief option of the button as soon as you hover over the button.


'''

# for normal and active state

b1 = Button(root,text ="click me",bg ="yellow",fg="red",activebackground="pink", activeforeground="blue",relief="flat", overrelief="sunken")
b1.config(border="10",padx=50, pady=50)
b1.pack()



root.mainloop()