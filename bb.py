from tkinter import*
from time import sleep

root = Tk()
root.geometry("600x400")
7
def clicked():
    if y.get() == "ram":
        for i in range(108):

            Label(root, text = f"ram ram ram ram {i+1}", bg ="pink", fg = "green", font= ("calibri", 20)).pack()
            sleep(0.3)
    else:
        Label(root, text=f"Hello {y.get()} sir", bg="pink", fg="green",
              font=("calibri", 20)).pack()


label1 = Label(root, text = "Enter your name...", fg= "black", font=("Arial", 25))
label1.pack()

y = Entry(root, bg = "yellow",fg= "red", font=("Arial",20))
y.pack(pady = 20)

y1 = Button(root, text = "click here", command=clicked, bg = "yellow",fg= "red", font=("Arial",20))
y1.pack(pady=20)











root.mainloop()