from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Methods of the Entry widgets. 
Here e corresponds to Entry widget just for explanation

1. config:              1. e.config()
                        2. Use to update or add new option in Entry widget.
                        
2. get():               1. e.get()
                        2. returns the entry current text as string.
                        
3. delete():            1. e.delete(first, last)
                        2. Use to delete elements from the Entry_widget. 
            
4. icursor():           1. e.icursor(position)
                        2. Change or set the cursor position of the Entry_widget.
                        3. e.icursor(5) will place the cursor before 5th character of the entry widget.

5. index():             1. e.index(index)
                        2. It gives the index position of corresponding index, it is just like asking what 
                           is the position of 5th character of the text in entry widget and answer is 5 which is useless
                           beacuase if someone knows the position then why would he ask.
                           BUT it is useful in these cases.
                        
                        3. (A) e.index(INSERT): returns the index position of the cursor.
                           (B) e.index(END): returns the position of last character of the text in Entry widget.
                           (C) e.index(Anchor): returns the position of first selected character from left in the Entry widget.


6. insert():          1. e.insert(index, string)
                      2. It inserts the string at particular index in Entry widget.                        

7. select_adjust()    1. e.select_adjust(index)
                      2. Same as selection_adjust()
                      3. It select all the characters from the 0 index position to the index position you have set.

8. select_range()     1. e.select_adjust(start,end)
                      2. Same as selection_range()
                      3. It select all the characters in the given range.
                      
9. select_present()   1. e.select_present()
                      2. Same as selection_present()
                      3. It just prints true if there is any selection in the entry widget.
                      
10. select_clear()    1. e.select_clear()
                      2. Same as selection_clear()
                      3. Clears all the selection, if there is any.

11. select_from and select_to  1. e.select_from(index) and e.select_to(index)
                               2. same as selection_from() and selection_to()
                               3. It starts selecting from index of select_from to index of select_to()

12. xview():            1. e.xview(index)
                        2. It make sure particular index element always appears in the entry widget, what happen 
                           sometimes is that you have a entrywidget which can show 10 characters only and remaining
                           just hides so when you use e.xview(12), then 12 character just appears on the screen at the 
                           0 position and all the character before 12th position letter hides..

13. xview_scroll()      1. e.xview_scroll(number, what)
                        
                        2. Consider a horizontal scroll bar, it is used to scroll horizontally by a give amount,
                           if you use positive for number, then it scrolls all the text in entrywidget from left 
                           to right and if you use negative value for number then it scrolls text in entrywidget 
                           from right to left
                           
                        3. Here what can be UNITS or PAGES, units for scrolling on the basis of character width and pages
                           for scrolling on the basis of entry box size.
'''

# Here we have created a label, button and entry widget, write anything on entrywidget and click button to see changes



# e.delete() and e.index(INSERT)
def printer():
    e.delete(0,3)
    label = Label(root, text=f"3 character from index position 0\n to index position 3 is deleted \n and indes position of cursor is {e.index(INSERT)}", fg="red").pack(pady=10)


label = Label(root, text="Write anything and click button to see magic\n write anything of atleast 8 words", bg="pink", fg="blue", width="50", height="5").pack(pady=19)

button = Button(root, text='clickme', command=printer).pack(pady=10)

e = Entry(root, width=2, font=("Arial", 20), bg="red", fg="yellow", selectbackground="green", selectborderwidth="4", selectforeground="yellow")
e.pack(ipady=30, ipadx=14, padx=13)

# e.config()
e.config(width=25)

root.mainloop()