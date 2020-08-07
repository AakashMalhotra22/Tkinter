'''
Underline the whole sentence:
1. You can use underline attribute of label to underline a particular word but when it comes to underline whole sentence,
   then you have two option.
   A. Use the font which has underline option in it by default like Verdana 15 underline
   B. Import font from tkinter.

'''


from tkinter import*
from tkinter import font
root= Tk()
# option-1
label = Label(root, text ="Underline the whole text by option1", font=("Verdana 15 underline")).pack()# here 15 is font size, you can change it.

#Option- 2

label2 = Label(root, text ="Underline the whole text by option-2")
label2.pack(pady=10)
f = font.Font(label2, label2.cget("font"))
f.configure(underline = True)
label2.configure(font = f)


root.mainloop()

