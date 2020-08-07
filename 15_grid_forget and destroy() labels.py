from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("400x600")
'''
grid_forget():
1. It is just used to remove a label from the screen
2. It's syntax is label.grid_forget()
3. It's same as pack_forget().

destroy():
1. It is used to delete a label from the screen completely, means one's destroyed, cant be retreived.
2. It's syntax is label.destroy()
'''
label1 = Label(root)

def func():
    # There is a problem because in grid system, label packs at the same place as it was earlier, for example, first you write
    # ram in entry box, then it would print hello ram, then you write aakash, then it would print hello aakash over hello ram
    # at the same place, so it just overlaps it and it looks clumsy, so what we did, before packing hello aakash after hello ram
    # first we remove hello ram from screen, then packs hello aakash over it.
    global label1
    label1.grid_forget()# or you can use label1.destroy()
    label1 = Label(root, text=f"Hello {e.get()}")
    label1.grid(row=7, column=1)

#label
label = Label(root, text="Enter your name...", bg ="pink", fg="blue",font=("",14)).grid(row=1, column=1,padx=10)

#button
button1 = Button(root, text='clickme',font=("",14), command =func).grid(row=2, column=1,padx=10)

e = Entry(root, width=20,font=("Arial",14), bg="cyan",fg="white", cursor="dot")
e.grid(row=3, column=1, ipady=5)

#remove: It just removes the label from the screen.
def remove():
    label1.grid_forget()


#delete: It just completely destroythe label from the screen.
def delete():
    label1.destroy()


# show: This function is used to again pack the label on screen, if it is been removed by use of grid_forget() but
#       if it is removed by use of destroy(), then it can't be back and that why try and except is used because whenever
#       you try to get that label back which is completely destroyed, so this would give an error that label1 is not
#       defined.
def show():
    try:
        label1.grid(row=7, column=1)
    except:
        pass

button2 = Button(root, text='remove',font=("",10),bg="red", command =remove).grid(row=4, column=1)

button3 = Button(root, text='delete',font=("",14),bg="blue", command =delete).grid(row=5, column=1)

button4 = Button(root, text='show',font=("",14),bg="green", command =show).grid(row=6, column=1)


root.mainloop()