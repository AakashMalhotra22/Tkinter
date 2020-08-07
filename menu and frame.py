from tkinter import*


root = Tk()

root.title("Practise")

yf = Frame(root, bg = "green", border="17", height=200, width=300, relief="sunken" )
yf.pack(pady=4)


y = Label(yf, text="Let's do something", fg= "pink", bg="blue", font=("",32), relief="sunken")
y.pack(pady=20)

y1 = Label(yf, text="Enter your name...", fg= "pink", bg="blue", font=("",20), relief="sunken")
y1.pack(pady=20)

y2 = Entry(yf, bg="yellow", fg="red", border=4, font=("arial",18))
y2.pack(pady=10)

# command

def func1():
        y4= Label(yf, text=f"Hi {y2.get()}",fg="red", border=4, font=("arial",18))
        y4.pack(pady=4)


def func2():
#    y4 = Label(yf, text=f"chlo kuck krte hn", fg="white",bg="black", border= 1, font=("arial", 18))
#   y4.pack(pady=4)
    framer.pack(pady=20, padx=20)

def func3():
    framer2.pack(pady=20, padx=20)



y3 = Button(yf, text="click here", border=10, command=func1)
y3.pack(pady=5)

#menu
menur = Menu(root)
root.config(menu=menur)

ym1 = Menu(menur)
menur.add_cascade(label="File", menu=ym1)
ym1.add_command(label ="intro",command= func2 )
ym1.add_separator()

ym1.add_command(label ="exit", command= root.quit)


my_menu2= Menu(menur)
menur.add_cascade(label="View", menu=my_menu2)
my_menu2.add_command(label="ask", command=func3)
my_menu2.add_command(label ="exit", command= root.quit)


framer = Label(yf,text="aakash naam to suna hoga", fg="red", bg="yellow", relief="groove", font=("Times New Roman", 16))

framer2 = Label(yf, text = "Edit krte hn", fg="red", bg="yellow", relief="groove", font=("Times New Roman", 16))


root.mainloop()