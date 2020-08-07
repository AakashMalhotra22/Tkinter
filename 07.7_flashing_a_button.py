from time import*
from tkinter import*

root = Tk()
root.title("Flashing a button")
root.geometry("500x600")

# Manual Flash

label1 = Label(root, text="Press f key to flash the Manual flash button", bg="cyan", fg="red", padx=5, pady=5).pack(pady=5)

def callback(event):
    button1.config(bg="yellow")
    root.after(100,lambda:button1.config(bg="lightgrey"))
    button1.pack()

button1 = Button(root, text="Manual flash",bg="lightgrey",fg="red")
button1.pack(pady=5)
root.bind("<f>", callback)



# Automatic Flash
from threading import*
from time import*




def automate(end):
    for i in range(end):
        button2.config(bg="red")
        button2.pack()
        sleep(0.1)
        button2.config(bg="blue")
        button2.pack()
        sleep(0.1)


def background(target,args):
    y = Thread(target=target,args=args)
    y.start()


button2 = Button(root, text="Automatic Flash",bg="blue",fg="white", command= lambda:background(automate,(100,)))
button2.pack()


root.mainloop()