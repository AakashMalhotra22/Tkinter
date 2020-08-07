import tkinter as tk


def callback(event, tag):
    print(event.widget.get('%s.first'%tag, '%s.last'%tag))

root = tk.Tk()

text = tk.Text(root)
text.pack()

text.tag_config("tag1", foreground="blue")
text.tag_bind("tag1", "<Button-1>", lambda e:callback(e, "tag1"))
text.insert('end', "first link", "tag1")

text.insert("end", " other text ")

text.tag_config("tag2", foreground="blue")
text.tag_bind("tag2", "<Button-1>", lambda e:callback(e, "tag2"))
text.insert("end", "second link", "tag2")

root.mainloop()