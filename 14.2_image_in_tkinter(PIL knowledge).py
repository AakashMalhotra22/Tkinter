from tkinter import*
from PIL import Image,ImageTk

'''
Image in tkinter:
1. To set image in tkinter application, we use external library pillow which is written as PIL
2. Here we will discuss, a few options of PIL.

3. We will be using only Image and ImageTK option of PIL and work over it only.
'''

# 1st Image:  Image option is used to open any image wherever it is present in your computer.
'''Let's open a image'''



y1 = Image.open("aak.jpg")# Here we have written only image name and not it's address because this python file and
y1.show()                 # image are saved in same directory, otherwise, we have to write first address then name, as did
                          # in icon.

# Showing image which is not in this directory.

y2 = Image.open(r"C:\Users\india\Dropbox\Screenshots\screen.png")# here first we written the address then \(slash) and then name of image.
y2.show()

'''The above code first show image y1, when you close that image then it shows image y2'''
