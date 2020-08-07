from tkinter import*
root = Tk()

entry = Entry(root).pack()
text = Text(root)
text.insert(INSERT,"ram")
text.insert(INSERT,"ram")
text.delete('1.4', END)
text.insert(INSERT,"ji")

text.pack()

root.mainloop()