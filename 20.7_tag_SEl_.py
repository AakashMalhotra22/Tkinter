from tkinter import*
root = Tk()
root.geometry("900x500")

'''
tag:

1. Tags are used to associate names to regions of text which makes easy the task of modifying the display settings of 
   specific text areas.
   
2. Tags are also used to bind event callback to specific ranges of text.

3. Any text range have multiple tags.

4. Same tag can be used for multiple ranges.

5. A. SEL or "sel" is a special tag which corresponds to the current selection,
   B. This tag can be added only at the selected text.
   C. There should be atmost one range using selected tag.
   D. sel cant be deleted using tag_delete method, because it is inbuilt.

Methods of tags.
1. tag_add(tag_name,startindex, endindex): creates a tag at this range.
2. tag_remove(tag_name, startindex, endindex): This would remove the tag from that area but not actually deleting the original tag.
3. tag_delete(tag_name): Deletes the tag
4. tag_configure(tag_name, **options) here keep in mind fg is not defined write full foreground same for bg.
5. tag_names(): prints out the name of the tags.
6. tag_ranges(tag_name): it prints out the range of the particular tag.
'''




def func1():
    y.tag_configure("tag1",background="yellow") # Here we have created this tag "tag1" and change some of its options.
    y.tag_add("tag1", 1.1, 1.4 ) # added tag1 in the range(1.1 to 1.4)
    y.tag_add("tag1", 1.8, 1.12) # added tag1 in the range(1.2 to 1.4)

    y.tag_config("sel", background="red", foreground="white") # do changes in the selected tag.
    y.tag_add("sel", 1.19, 1.21)  # When you run this, the text at position 1.19 to 1.21 is already selected.

    print(y.tag_names())
    print(y.tag_ranges('tag1'))

def func2():
    y.tag_remove("tag1", 1.1, 1.4 )
    print(y.tag_names())

def func3():
    y.tag_delete("tag1",)
    print(y.tag_names())


y = Text(root,bg="pink", fg="blue", height="6", width="40" , cursor="dot",border="1")
y.pack(pady=10)



b1 = Button(root, text="tag_add",border="10", command=func1).pack(pady=10)

b2 = Button(root, text="tag_remove",border="10", command=func2).pack(pady=10)


b3 = Button(root, text="tag_delete",border="10", command=func3).pack(pady=10)


root.mainloop()