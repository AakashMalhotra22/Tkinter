from tkinter import*


root = Tk()

#Creating command func for y1 button
def func1():
    global yn

    yn =Label(root, text =f'{y.get()} is GOD' )
    yn.pack(pady=20)


# creating hide func for hid button
def hidder():
      yn.pack_forget() # for forget
  #    yn.destroy()


def shower():
    yn.pack()


root.geometry('500x500')
root.iconbitmap(r'C:\Users\india\Desktop\Python Files\tkinter\y.ico')
root.title("My name is Aakash")


label1 = Label(root, text = "Welcome", bg= "pink", fg= "blue", font=("arial",18), relief ="sunken")
label1.pack(padx=20, pady=20)

label2 = Label(root, text = "Write your name here...", bg= "blue", fg= "white", font=("arial",18), relief ="groove")
label2.pack(padx=20, pady=20)

y = Entry(root, text="hello", bg="red", font=("arial",16), justify='right')
y.pack()

y1 = Button(root, text= "click here for fun", bg ="yellow", fg="red", command= func1,font=("arial",15))
y1.pack(pady=20)

#hide_button

hide_button = Button(root, text= "hide", bg ="grey", fg="black", command= hidder,font=("arial",15), relief= "sunken")
hide_button.pack(pady=20)

show_button = Button(root, text= "show", bg ="grey", fg="black", command= shower,font=("arial",15), relief = "sunken")
show_button.pack(pady=20)


#fakeer func

def faker():
    yr = Label(root, text="Power")
    yr.pack()


# menu

my_menu = Menu(root)
root.config(menu= my_menu)

menu_1 = Menu(my_menu)
my_menu.add_cascade(label="aakash", menu=menu_1)
menu_1.add_command(label ="intro", command= faker)
menu_1.add_separator()
menu_1.add_command(label ="exit", command= root.quit)


menu_2 = Menu(my_menu)
my_menu.add_cascade(label="Neena", menu=menu_2)
menu_2.add_command(label ="intra", command= faker)
menu_2.add_separator()
menu_2.add_command(label ="exit", command= root.quit)


root.mainloop()