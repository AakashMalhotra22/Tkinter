from tkinter import*

root = Tk()
root.title("Jai Shri Ram...")
root.geometry("400x400")

my_label = Label(root, text ="Ram...",fg="black", bg= "red", font=("TimesNewRoman",18), height = 2, width= 24, relief="ridge",state ="disabled" )
my_label.pack(padx= 5, pady= 100)

ram1 = Label(root, text= "Jai shri ram", fg="blue", bg ="yellow", font=("TimesNewRoman", 18), relief = "groove")
ram1.pack()







root.mainloop()
print("ram")
