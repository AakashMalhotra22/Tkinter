from tkinter import*

'''
So far
1 .pack_forget()- just forgets - works with pack
2 .destroy() - Completely cancels out - 
3 .iconify()- Minimize
4 .deiconify() - Maximize or regenerate
5 .withdraw() - Cancel out
'''
root = Tk()
root.title("lets complete it")
root.geometry("500x500")


#
def submit():
    global hello_label

    hello_label = Label(root, text="Hello "+e.get())
    hello_label.grid(row=3, column=0)

def clear():
    #hello_label.grid_forget()
    #You can also use the destroy here also
    hello_label.destroy()


my_label = Label(root, text = "Enter your name: ").grid(row=0, column=0)

e = Entry(root)
e.grid(row=1, column=0)

my_button = Button(root, text = "click here", command= submit).grid(row=2, column=0)



#clear button
clear_button = Button(root, text ="Clear", command= clear).grid(row=2, column=1)


root.mainloop()
