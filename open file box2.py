from tkinter import*
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title("Open it")
root.geometry("400x400")


#Open dialog Box


def func():
  root.filename = filedialog.askopenfilename(initialdir=r'C:\Users\india\Desktop\Python Files\tkinter', title="Open an image file", filetypes=(("JPG Files", "*.jpg"),("All files","*.*")))
  my_label = Label(root,text=root.filename).pack(pady=10)# This will print out the location of the opened file.

  # Open picture and paste on screen:

  global my_img
  my_img = ImageTk.PhotoImage(Image.open(root.filename))
  img_label = Label(root, image=my_img)
  img_label.pack(pady=10)

but = Button(root, text = "open", command = func).pack(pady=10)

root.mainloop()