from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("900x500")

'''

Index Method

1. index:   A. syntax is text_widget_name.index(index position).


Indexes:
1. These are used to point to positions within the text handled by the text widget.
2. There are following index types:

   A. line/column(line.column):  A. 1.3 means first line and 3rd character.
                                 B. 2.0 means second line with no element.
    
   B. line end  (line.end)       A. "1.end" means first line last character.
                                 B. a line does not end unless you press ENTER.
   
   C. INSERT                     A. The  position at which cursor is placed.
   
   D. CURRENT                    A. The position which is near to mouse pointer.
   
   E. END                        A. The position after the last line and last character of the text widget.
   
   F. user_defined_marks:        A. INSERT, CURRENT, END are all examples of marks but this are already defined marks.
                                 B. In the same way you can create your own mark.
                                    Ex: i created my own mark named "lol" which indicates the index position 1.2
                                    
                                 C.  Discuss in detail later.
                                 
    G. user_defined_tabs:        A. Discuss it  later
    
    H. Selection                 A. type of tag which covers the selection text. 
   
'''


# Example:


def indexer():
    r1 = y.index(INSERT)
    r2 = y.index(CURRENT)
    r3 = y.index(END)
    r4 = y.index('1.end')


    l1 = Label(root, text =f"cursor is at {r1} \n the position near to mouse pointer is {r2}\n"
                           f"the end position is {r3} \nthe end position of first line is {r4}"
                           ,bg ="black", fg="white").pack(pady=10)


y = Text(root, width=40, height=9)
y.pack(pady=10)

b1 = Button(root, text="click me after writing something", command=indexer)
b1.pack(pady=10)



root.mainloop()