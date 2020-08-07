from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("400x600")
'''
pack_forget():
1. It is just used to remove a label from the screen
2. It's syntax is label.pack_forget()

destroy():
1. It is used to delete a label from the screen completely, means one's destroyed, cant be retreived.
2. It's syntax is label.destroy()
'''

def func():
    global label1

    label1 = Label(root, text=f"Hello {e.get()}")
    label1.pack()

#label
label = Label(root, text="Enter your name...", bg ="pink", fg="blue",font=("",14)).pack(pady=10)

#button
button1 = Button(root, text='clickme',font=("",14), command =func).pack(pady=10)

e = Entry(root, width=20,font=("Arial",14), bg="cyan",fg="white", cursor="dot")
e.pack(ipady=4)

#remove: It just removes the label from the screen.
def remove():
    label1.pack_forget()


#delete: It just completely destroythe label from the screen.
def delete():
    label1.destroy()


# show: This function is used to again pack the label on screen, if it is been removed by use of pack_forget() but
#       if it is removed by use of destroy(), then it can't be back and that why try and except is used because whenever
#       you try to get that label back which is completely destroyed, so this would give an error that label1 is not
#       defined.
def show():
    try:
        label1.pack()
    except:
        pass

button2 = Button(root, text='remove',font=("",10),bg="red", command =remove).pack(pady=10)

button3 = Button(root, text='delete',font=("",14),bg="blue", command =delete).pack(pady=10)

button4 = Button(root, text='show',font=("",14),bg="green", command =show).pack(pady=10)


root.mainloop()