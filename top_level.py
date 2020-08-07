from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.geometry("900x500")


def func(*args):
   # label = Label(root, text=f"{y.get([1.21],[1.39])}").pack(pady=10)
    y.delete([1.0],['1.end'])
   # print(y.index(CURRENT))
    #(y.insert(1.1,"aakash"))
    #y.see(1.1)
    print(y.mark_set("lol",1.2))
    y.mark_gravity("lol",RIGHT)
    y.insert("lol", "ram")
    print(y.get('lol', INSERT))
    y.insert("lol", "sita")
    print(y.get('lol', INSERT))
    y.tag_add("tag1", 1.21, 1.31)
    y.tag_config("tag1",background="yellow")
    y.tag_config(SEL, background="cyan",foreground="white")
    y.yview_scroll(-10,UNITS)
    print(y.tag_names())


my_image = ImageTk.PhotoImage(Image.open('aak.jpg'))

y = Text(root,bg="pink", fg="blue", height="6", width="40" , cursor="dot",border="1",
         highlightbackground="yellow", highlightcolor="green", highlightthickness="10", # border
         insertbackground="blue", insertwidth="5",   # cursor
         insertofftime="1", insertontime="1", # cursor blinking
         selectbackground="yellow", selectborderwidth="50", selectforeground="purple", # selection colors
          spacing1=10,spacing2=1, spacing3=10, # spacing
         tabs="50", wrap="char")


y.image_create(image=my_image,index=1.0,pady="10",padx="30",align=TOP,)
y.pack(pady=10)



b1 = Button(root, text="hello",border="10", command=func)
root.bind('<b>',lambda b=b1:b1.invoke())
b1.pack(pady=10)

e1 = Entry(root, border="10",highlightbackground="yellow", highlightcolor="green", highlightthickness="10")
e1.pack(pady=10)

root.mainloop()