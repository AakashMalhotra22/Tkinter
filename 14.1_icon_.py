from tkinter import*
root= Tk()

'''
For adding icon.
1. First you have to have icon file which is of form .ico form.
2. Address of icon file where it is saved.
3. syntax is root.iconbitmap(r'address\filename.ico')
   # One more thing, if your icon file is saved in the same directory as your python file, then there is no need of
     address, you just need to write the name of file only.
     
     
4. This would appear on the top left corner of the application.

'''

root.title("icon")
root.iconbitmap(r"C:\Users\india\Desktop\Python Files\tkinter\y.ico")# here r is rawstring which is used to avoid other meaning of slash.
#Here there is no need to write address of icon file, because our icon file and python file are saved in same directory.
# We can easily write root.iconbitmap('y.ico')

#Creating a label

l = Label(root, text="Notice the icon on the left most corner of this application", bg="red", fg="white").pack(pady=5, fill=X)

root.mainloop()