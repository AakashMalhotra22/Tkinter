from tkinter import*
root = Tk()
root.title("**kwargs")

#Making userid and password

def making(parent, text, width=None,**options):
    my_label = Label(parent,text=text, width=width).pack()
    my_entry = Entry(parent, **options)
    if width == None:
       pass
    else:
        my_entry.config(width =width)
    my_entry.pack( )


y1= making(root,text="Username:", bg="pink", border=5)
y2= making(root,text="Password",width=20,bg="pink", show="*", border=5)



root.mainloop()