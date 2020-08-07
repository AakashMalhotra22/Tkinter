from tkinter import *
from PIL import ImageTk, Image

root = Tk()
root.geometry("900x500")


'''
1. The Image can be added much in the same as in Entry box.
2. Here is a separate method to add image that is 
   text_box_name.image_create(index, image,align, padx, pady)# These are the common options.

3. align means position of image wrt to text.
   1. baseline, bottom, center, top 

'''

#func image adder:
def imager():
    global my_image # This is neccessary, otherwise image would not show up.
    my_image = ImageTk.PhotoImage(Image.open('aak.jpg'))

    y.image_create( image=my_image, index=INSERT,padx=10,pady=10, align="baseline")


# Creating a text box
y = Text(root, bg="pink", fg="blue", height="20", width="40", border="1")
y.pack(pady=10)

# Creating a button to add image
b1 = Button(root, text="Add image \n at the cursor position", command=imager)
b1.pack(pady=10)

root.mainloop()