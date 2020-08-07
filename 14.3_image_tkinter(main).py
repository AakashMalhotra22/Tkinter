from tkinter import*
from PIL import Image,ImageTk
root = Tk()
root.title("image")
root.geometry('600x600')


'''
Image in tkinter.
1. you can add image in any widget, button, labels, but not in entry box, 
# steps to add image
step1: Create the instance of an image.
step2: use image option of any widget to link the image instance with that widget.

2. The size of image appears on the screen, depends on the image size only, it cant be change from here.

'''
# Example 1:
'''Adding an image to a label'''

# STEP1: Creating image instance
my_image = ImageTk.PhotoImage(Image.open('aak.jpg'))# here we have used image only not the address, because this image and file is saved in same directory.

# Step2: Adding to label
l1 = Label(root, text="hello", image=my_image,bg="green",fg="white").pack(pady=10, fill=X)
# There is a problem, only image appears and not the text and this is because your image is over the text.
# To show both text and image on screen, use compound attributes.
'''
compound attributes:
It has following option.
1. none: it is default option, which means image over text.
2. top: it means image shows above text.
3. bottom: it means image shows below text.
4. left: it means image shows left to text,
5. right: it means image shows right to text.
6.. center: It means text appears in the center of image.
'''
# Using compound
l2 = Label(root, text="hello", image=my_image,compound="top", bg="red", foreground="black").pack(pady=10,fill=X)


# Adding image to a button
b1 = Button(root, text ="click_me", image=my_image, border="10",compound="center",bg="blue",fg="yellow",font=("",16)
            ,relief="raised").pack(pady=10, fill=X)



root.mainloop()