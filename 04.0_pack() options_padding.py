'''
Label pading option:
pack()

options:
1. pady: External y-padding, default is zero.
2. padx: External x-padding, default is zero.
3. ipadx: Internal x-padding, default is zero, increases the width of the background
4. ipday: Internal y-padding, default is zero, increases the height of the background.

5. side: 1. It is used to choose the side of packing the widget in the window, it is default at top, that's why whenver you pack anything on screen, it comes at top.
         2. There are four options.
            a. top, b. left c. right d. bottom

6. expand: 1. Specifies whether the widget should be expanded to fill any extra space in the geometry:
           2. It has two options:
               a. False or zero: which is default, no change.
               b. True or non-zero value which just acts as pady.

7. fill 1. It is used to specify whether the widget should occupy all the space provided to it by the master.
        2. It has four options:
         a. NONE: it is default, keep the widget original size.
         b. X: fill horizontally.
         d. BOTH: fill the given space along that direction, if you want to fill full then set expand as non-zero value or True.
         c. Y: fill vertically.

'''
#1. Padding- padx, pady, ipadx, ipady

from tkinter import*

root =Tk()
root.geometry('500x500')

label1 = Label(root, text="black", fg ="white", bg="black", font=("",25))
label1.pack(padx="100", pady=100, ipadx=100, ipady=100)
# Here ipadx has increased the width, ipday has increased the height.
# You can also use height and width instead of ipadx and ipady.

root.mainloop()

