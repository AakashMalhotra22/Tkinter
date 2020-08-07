from tkinter import*
root = Tk()
root.geometry("900x500")

'''
 user_defined_marks:             A. INSERT, CURRENT, END are all examples of marks but this are already defined marks.
                                 B. In the same way you can create your own mark.
                                    Ex: i created my own mark named "lol" which indicates the index position 1.2
                                    
Methods:
1. mark_set(mark,index):   1. It is used to create mark, here mark represents the name of mark and index represents
                              the position you want to set the mark.

2. mark_unset(mark):       1.  Remove the given mark from the text widget.

3. mark_names():           1.  returns all the marks name from the text widget.

4. index(mark):            1. prints out the index position of hte mark.

5. mark_gravity(mark, gravity)  1. When you insert a text at the mark, then mark can be shifted to the right or the left.
                                   Ex:
                                   we have a mark "lol" at index 1.2, now you have inserted "ram" at the mark position,
                                   then the position of new mark is before r or "ram" or after m of "ram", depends upon
                                   this option.
                                   if you set gravity =right(default), then mark is at shifts right.
                                   if you set gravity =left, then mark is at shifts left.   
'''



def func(*args):
    y.mark_set("lol",1.2) # The mark "lol" is created which represents index position.
    y.mark_gravity("lol",RIGHT) #The gravity of mark "lol" is set to right.
    print(y.mark_names()) # it prints out the name of all marks.
    y.insert("lol", "ram") # It inserts ram at mark 'lol' which means at index 1.2
    print(y.get('lol', INSERT)) # it returns out text from mark "lol" means at index 1.2 to the index where cursor is placed.

    y.mark_unset("lol") # it unsets the mark lol
    print(y.mark_names())



y = Text(root,bg="pink", fg="blue", height="6", width="40" , cursor="dot",border="1")
y.pack(pady=10)

b1 = Button(root, text="hello",border="10", command=func)
b1.pack(pady=10)

root.mainloop()