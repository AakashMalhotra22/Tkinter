from tkinter import*
root = Tk()
root.geometry("600x400")

# function
def clicked():
    if y.get() == "neena":
        for i in range(20):
            Label(root, text = f"soja {y.get()} soja, kl padai bhi krni hn......", bg ="pink", fg = "green", font= ("calibri", 20)).pack()
    else:
        Label(root, text=f"Hello {y.get()} sir", bg="pink", fg="green",
              font=("calibri", 20)).pack()


#label
label1 = Label(root, text = "Enter your name...", fg= "black", font=("Arial", 25))
label1.pack()

# Entry widget
y = Entry(root, bg = "yellow",fg= "red", font=("Arial",20))
y.pack(pady = 20)

#Button
y1 = Button(root, text = "click here", command=clicked, bg = "yellow",fg= "red", font=("Arial",20))
y1.pack(pady=20)

root.mainloop()