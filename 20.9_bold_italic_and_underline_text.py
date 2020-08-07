from tkinter import *
from tkinter import font
root = Tk()
root.geometry("900x500")

'''There is no such method, just an application'''

def bold_text():

    text_font= font.Font(y, y.cget("font"))
    text_font.configure(weight='bold')
    y.tag_config("bolder", font=text_font)

    if y.tag_ranges("sel"): # This is to check, whether a text is selected or not
        current_tag=(y.tag_names("sel.first",))# it gives the name of tag associated with the selected text first position
        if "bolder" in current_tag:
            y.tag_remove("bolder", "sel.first", "sel.last") # sel.first represents the first selected position and same for sel.last, for this make sure there is a selected text.
        else:
            y.tag_add("bolder", "sel.first", "sel.last")
    else:
        pass

def italic_text():

    italize_font = font.Font(y, y.cget("font"))
    italize_font.configure(slant="italic")
    y.tag_config("italizer", font=italize_font)

    if y.tag_ranges("sel"): # This is to check, whether a text is selected or not
        current_tag=(y.tag_names("sel.first",))# it gives the name of tag associated with the selected text first position
        if "italizer" in current_tag:
            y.tag_remove("italizer", "sel.first", "sel.last") # sel.first represents the first selected position and same for sel.last, for this make sure there is a selected text.
        else:
            y.tag_add("italizer", "sel.first", "sel.last")
    else:
        pass



def underline_text():
    underline_font= font.Font(y, y.cget("font"))
    underline_font.configure(underline=True)
    y.tag_config("underline", font=underline_font)


    if y.tag_ranges("sel"): # This is to check, whether a text is selected or not
        current_tag=(y.tag_names("sel.first",))# it gives the name of tag associated with the selected text first position
        if "underline" in current_tag:
            y.tag_remove("underline", "sel.first", "sel.last") # sel.first represents the first selected position and same for sel.last, for this make sure there is a selected text.
        else:
            y.tag_add("underline", "sel.first", "sel.last")
    else:
        pass


y = Text(root, bg="white", fg="black", height="6", width="40", cursor="dot", border="1",selectbackground="cyan",selectforeground="black" )
y.pack(pady=10)

y2 = Text(root, height=2, width="13").pack(pady=10)

b1 = Button(root, text="BOLD", border="10", command=bold_text)
root.bind('<Control-b>', lambda event,b=b1:b.invoke())
root.bind('<Control-B>', lambda event,b=b1:b.invoke())
b1.pack(pady=10)

b2 = Button(root, text="ITALIC", border="10", command=italic_text)
root.bind('<Control-q>', lambda event,b=b2:b.invoke())# we cant choose, ctrl+i, because it already defined.
root.bind('<Control-Q>', lambda event,b=b2:b.invoke())
b2.pack(pady=10)

b3 = Button(root, text="UNDERLINE", border="10", command=underline_text)
root.bind('<Control-u>', lambda event,b=b3:b.invoke())
root.bind('<Control-U>', lambda event,b=b3:b.invoke())
b3.pack(pady=10)

root.mainloop()