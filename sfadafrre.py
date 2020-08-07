from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

def printer():


#    e.xview(END)
 #   e.xview_scroll(100, UNITS)
    label = Label(root, text=f"Hello {e.get()}").pack(pady=10)


label = Label(root, text="Enter your name...", bg ="pink", fg="blue", width ="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command =printer).pack(pady=10)

e = Entry(root, width=20,font=("Arial",20), bg="red",fg= "yellow",cursor="dot",border=5, relief= "sunken", justify="right")
e.pack(ipady=30, ipadx=14, padx=13)


root.mainloop()