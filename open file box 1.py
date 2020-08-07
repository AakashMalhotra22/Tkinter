from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open it")
root.geometry("400x400")


#Open dialog Box

root.filename = filedialog.askopenfilename(initialdir=r'C:\Users\india\Desktop\Python Files\tkinter', title="Open an image file", filetypes=(("JPG Files", "*.jpg"),("All files","*.*")))

root.mainloop()