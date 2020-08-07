from tkinter import *


root = Tk()
text = Text(root, height=5, width=50)
text.pack()


text.insert(INSERT, "Hello.....")
text.insert(END, "Bye Bye.....")


text.tag_add("tag1", "1.0", "1.4")
text.tag_add("tag2", "1.8", "1.13")
text.tag_config("tag1", background="yellow", foreground="blue")
text.tag_config("tag2", background="black", foreground="green")
root.mainloop()