from tkinter import*
root = Tk()

'''
bitmap(Basic level):

1. You can add certain symbols in your tkinter button or labels instead of text which is called bitmaps.
   For example an error symbols.

2. These symbols are called bitmaps.

3. bitmap can be used in button and labels.

4. These are the following bitmaps available.
   A. "error"  B. "gray75"  C. "gray50" D."gray25" E."gray12"
   F."hourglass" G."info" H."questhead" I."question" J."warning"


5. If you write both text and bitmap, then bitmap would be given preference and text would not appear

'''

# Example

# Here only bitmap appears,  not the text.
b1 = Button(root, text="hello", bitmap="error",fg="blue", bg="pink").pack(pady=5, ipady=10, ipadx=10)

# Here only bitmap appears, not the text, no need to write the text
l1 = Label(root, text="info", bitmap="info",fg="green", bg="pink").pack(pady=5)


'''Above codes can simply be written as...'''
#b1 = Button(root, bitmap="error",fg="blue", bg="pink").pack(pady=5, ipady=10, ipadx=10)
#l1 = Label(root,  bitmap="info",fg="green", bg="pink").pack(pady=5)



root.mainloop()