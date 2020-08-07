from tkinter import*

root = Tk()
root.title("Jai Shri Ram...")
root.geometry("400x400")

my_label = Label(root, text ="Jai Shri Ram...",fg="black", bg= "red", font=("TimesNewRoman",18), height = 2, width= 24, relief="ridge",state ="disabled" )
my_label.grid(row = 0, column = 0, columnspan= 2)

ram1 = Label(root, text="favourable", fg="blue", bg ="yellow", font=("TimesNewRoman", 12), relief = "groove")
ram1.grid(row = 1, column =0,)


ram3 = Label(root, text = "bolo jai shri ram...", fg ="Pink", bg ="blue", font=("Arial, 12"))
ram3.grid(row=2, column=1)







root.mainloop()
