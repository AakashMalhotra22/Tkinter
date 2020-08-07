from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.geometry("900x500")

'''
Method to get and delete and insert.

A. text_widget_name.get(index1, index2): A. returns the text.
                                         B. you can avoid writing index2, then it would only return character at index1.


B. text_widget_name.selection_get(): returns the selected text.

C. text_widget_name.delete(index1, index2): A. deletes the text
                                            B. you can avoid writing index2, then it would only delete character at index1.

D. text_widget_name.insert(index,str)

Note: A line never ends unless, you press ENTER.

'''



def func(*args):
    r1 = y.get([1.21], [1.39])
    r2 = y.selection_get()

    label = Label(root, text=f"The text from index position 1.21 to 1.39 is'{r1}'\n"
    f"                         The text which is selected is '{r2}'\n"
                         f"The text which is deleted is {y.get([2.0],['2.end'])}").pack(pady=10)

    y.delete([2.0], ['2.end'])
    y.insert(3.1,"jai shri ram")


y = Text(root,bg="pink", fg="blue", height="6", width="40" , cursor="dot",border="1")
y.pack(pady=10)

b1 = Button(root, text="click it after writing something of more than 2lines",border="10", command=func)
b1.pack(pady=10)

root.mainloop()