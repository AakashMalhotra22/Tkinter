from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("600x800")
'''
place_forget():
1. It is just used to remove a label from the screen
2. It's syntax is label.place_forget()
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
    label1.destroy()# or you can use label1.place_forget()
    label1 = Label(root, text=f"Hello {e.get()}")
    label1.place(x=100, y=500, height=50, width=250)

#label
label = Label(root, text="Enter your name...", bg ="pink", fg="blue",font=("",14)).place(x=100, y=0, height=50, width=250)

#button
button1 = Button(root, text='clickme',font=("",14), command =func).place(x=100, y=80, height=50, width=100)

e = Entry(root, width=20,font=("Arial",14), bg="cyan",fg="white", cursor="dot")
e.place(x=100, y=180, height=50, width=250)

#remove: It just removes the label from the screen.
def remove():
    label1.place_forget()


#delete: It just completely destroythe label from the screen.
def delete():
    label1.destroy()


# show: This function is used to again pack the label on screen, if it is been removed by use of place_forget() but
#       if it is removed by use of destroy(), then it can't be back and that why try and except is used because whenever
#       you try to get that label back which is completely destroyed, so this would give an error that label1 is not
#       defined.
def show():
    try:
        label1.place(x=100, y=500, height=50, width=250)
    except:
        pass

button2 = Button(root, text='remove',font=("",10),bg="red", command =remove).place(x=100, y=250, height=50, width=100)

button3 = Button(root, text='delete',font=("",10),bg="blue", command =delete).place(x=100, y=330, height=50, width=100)

button4 = Button(root, text='show',font=("",10),bg="green", command =show).place(x=100, y=400, height=50, width=100)


root.mainloop()