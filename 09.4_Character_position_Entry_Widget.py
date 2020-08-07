from tkinter import*
root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
There are many ways to specify character position in Entry widgets, you can use this, when you are selecting or deleting
any items from the list so you can use them.                      


1. Numerical Indexes: Same as in python like range(0,2) means index position 0 and index position 1.
                      For example:
                      When you want to delete first 5 letter of the entrywidget, so you can use entrywidget.delete(0,5)


2. END:  1. It corresponds to last character in the Entry widget but not including last character.
         2. The range (0, END or"end") includes to all characters in the Entry widget.  
         3. when you want to delete all the elements in the entrywidget you can use entrywidget.delete(0,END) or you want
            to insert cursor at end position of the entrywidget, you can use it enntrwidget.icursor(END)
            
3. mouse coordinates:  1. Use of mouse coordinate, not known much

4. ANCHOR:             1. It corresponds to the first character of the selected text in Entry widget.
                       For example:
                       If you have text of 8 characters and you have selected text from 3 character to 5 character, then 
                       anchor corresponds to 3.

5. INSERT:             1. It corresponds to the current position of the text cursor.
                       2. By use of this, you can easily get the position of the cursor.
                       3. if your cursor is at 5 position, it would print 5.
'''




root.mainloop()