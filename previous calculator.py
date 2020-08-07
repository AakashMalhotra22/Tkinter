from tkinter import*
from PIL import *
from PIL import ImageTk, Image
root = Tk()
root.geometry("300x525")
root.title("Calculator")
root.resizable(0,0)
root.iconbitmap(r'C:\Users\india\Desktop\Python Files\tkinter\y.ico')

#Restricting entries of alphabats in Entry box function.

def change(inp):
    global Entry_box1
    y =(list(inp))
    i = Entry_box1.index(INSERT)

    if len(y)>25:
        return False

    else:

        try:
                if y[-1].isdigit()or y[-1] in"++-*,%,/.":
                    for i in range(len(y)):
                        if y[i] in r"abcdefghijklmnopqrstvwxyz=\\:?><,`~|_={};:'":
                             return False


                    else:
                        return True
                elif inp is"":
                    return True

                else:
                    return False
        except:
              return True




# Row-1

Frame_box1 = Frame(root, bg = "light yellow",highlightbackground="orange", border=10, relief ="raised")
Frame_box1.place(x=0,y=0, width=300, height=150)

def callback(sv):
    operation()



sv = StringVar()
sv.trace("w", lambda name, index, mode, sv=sv: callback(sv))
Entry_box1 = Entry(Frame_box1, bg = "light yellow", fg="black",border = None, font = ("", 32), justify = "right", textvariable=sv, borderwidth = 0 )
Entry_box1.place(x=-0,y=0, width=280, height=100)

reg = root.register(change)
Entry_box1.config(validate = "all", validatecommand = (reg,'%P'))


def entry_font_resize():
    y = Entry_box1.get()

    if len(y)>0:
        clear()
        Entry_box1.config(font=("",32))
        for i in range(len(y)):
            Entry_box1.insert(i,y[i])


        if len(y)>11:
            clear()
            Entry_box1.config(font=("",24))
            for i in range(len(y)):
                Entry_box1.insert(i,y[i])
            if len(y) > 15:
                clear()
                Entry_box1.config(font=("", 18))
                for i in range(len(y)):
                    Entry_box1.insert(i, y[i])
                    if len(y) > 22:
                        clear()
                        Entry_box1.config(font=("", 14))
                        for i in range(len(y)):
                            Entry_box1.insert(i, y[i])


out = str(Entry_box1.get())

def f(a):
    global Entry_box1
    global i
    i = Entry_box1.index(INSERT)
    # Creating variable k which converts every int number or operation in the form of string.
    k = str(a)
    if i==0:
        if k in "+,/,*":
             pass
        else:
            # Inserting value k at index position i.
            Entry_box1.insert(i, k)


    elif 25>i>0:
        var =0
        #Code to stop repetition of operations in Entry box one after other.
        y = list(Entry_box1.get())
        i = Entry_box1.index(INSERT)
        try:
         if y[i] in "+,-,/,*,." and k in "+,-,/,*,.":
             var=1
        except:
            pass
        try:
            if k in "+,-,/,*,."and y[i-1] in "+,-,/,*,.":
             var = 1
             pass
        except:
            pass
        if var!=1:
            # Inserting value k at index position i.
            Entry_box1.insert(i, k)

    elif i>25:
        pass

def operation():
    global i
    i = Entry_box1.index(INSERT)
    global label1
    # Mathematical Calculations.
    # Creating global out variable for output
    global out
    out = str(Entry_box1.get())
    y = str(Entry_box1.get())

    if i==0:
        try:
            if y[0]in"+-*/%*":
              out = "Err"
        except:
            pass


    if i>0:
            try:
                q =eval(y)
                out =q
            except SyntaxError:
                try:
                    print(i)
                    out =eval(y[0:i-1])

                except:
                    for i in range(1, len(y)):
                        for j in range(i - 1, i):
                            if y[i] in "+-*,%,/." and y[j] in '+-*,%,/.':
                                out = "Err"



            except :
                p = 'Err'
                out = p
            else:
                try:
                    if int(y)== q or float(y)==q:
                            out = ""
                except:
                    pass


    global label1

    label1 = Label(root,text = out, fg = "gray",bg="light yellow", font=("",18), anchor = "e")
    label1.place(x=10,y=100,width=280, height=30)
    entry_font_resize()












def cut():
    global i
    Entry_box1.delete(i-1,i)


def isequalsto():
    q = str(out)
    y = Entry_box1.get()
    p = len(y)
    for i in y:
        if i not in"+-/**%":
            pass
        else:
            Entry_box1.delete(0,p)
            for i in range(len(q)):
                Entry_box1.insert(i,q[i])
                label1.destroy()






def clear():
    q = str(out)
    y = Entry_box1.get()
    p = len(y)
    Entry_box1.delete(0, p)


#Lower Portion of calculator, Buttons:


# Row-1
e5 = Button(root, text="C", fg ="black", bg = "#d32323", font = ("",16), command =clear, relief="raised", border =10)
e5.place(x=0,y=150, width=75, height=75)

#Adding Division Image
divide_image = ImageTk.PhotoImage(Image.open("divide2.png"))

e6 = Button(root, text ="/", bg = "#d32323", font = ("",16),command =lambda: f("/"),relief="raised", border =10)
e6.place(x=75,y=150, width=75, height=75)

#Adding Multiply Image
multiply_image = ImageTk.PhotoImage(Image.open("multiply.png"))


e7 = Button(root, text = "X", bg = "#d32323", font = ("",16),command =lambda: f("*"),relief="raised", border =10)
e7.place(x=150,y=150, width=75, height=75)

#Adding Cut Image
cut_image = ImageTk.PhotoImage(Image.open("cut7.png"))


e8 = Button(root, image=cut_image, bg = "#d32323", font = ("",16), command = cut,relief="raised", border =10)
e8.place(x=225,y=150, width=75, height=75)

# Row-2

e9 = Button(root, text="7", fg ="black", bg = "orange", font = ("",16), command =lambda: f(7),relief="raised", border =10)
e9.place(x=0,y=225, width=75, height=75)

e10 = Button(root, text="8", fg ="black", bg = "orange", font = ("",16),command =lambda: f(8),relief="raised", border =10)
e10.place(x=75,y=225, width=75, height=75)

e11 = Button(root, text="9", fg ="black", bg = "orange", font = ("",16),command =lambda: f(9),relief="raised", border =10)
e11.place(x=150,y=225, width=75, height=75)

#Adding Subtraction Image
subtraction_image = ImageTk.PhotoImage(Image.open("Subttaction3.png"))


e12 = Button(root, image = subtraction_image, bg = "#d32323", font = ("",16),command =lambda: f("-"),relief="raised", border =10)
e12.place(x=225,y=225, width=75, height=75,)

# Row-3

e13 = Button(root, text="4", fg ="black", bg = "orange", font = ("",16),command =lambda: f("4"),relief="raised", border =10)
e13.place(x=0,y=300, width=75, height=75, )

e14 = Button(root, text="5", fg ="black", bg = "orange", font = ("",16),command =lambda: f("5"),relief="raised", border =10)
e14.place(x=75,y=300, width=75, height=75)

e15 = Button(root, text="6", fg ="black", bg = "orange", font = ("",16),command =lambda: f("6"),relief="raised", border =10)
e15.place(x=150,y=300, width=75, height=75)

#Adding Addition Image
addition_image = ImageTk.PhotoImage(Image.open("Addition5.png"))

e16 = Button(root, text = "+", bg = "#d32323", font = ("",16),command =lambda: f("+"),relief="raised", border=10)
e16.place(x=225,y=300, width=75, height=75)

# Row-4


e17 = Button(root, text="1", fg ="black", bg = "orange", font = ("",16),command =lambda: f("1"),relief="raised", border =10)
e17.place(x=0,y=375, width=75, height=75)

e18 = Button(root, text="2", fg ="black", bg = "orange", font = ("",16),command =lambda: f("2"),relief="raised", border =10)
e18.place(x=75,y=375, width=75, height=75)

e19 = Button(root, text="3", fg ="black", bg = "orange", font = ("",16),command =lambda: f("3"),relief="raised", border =10)
e19.place(x=150,y=375, width=75, height=75)

e20 = Button(root, text="=", fg ="white", bg = "blue", font = ("",16), command =isequalsto,relief="raised", border =10)
e20.place(x=225,y=375, width=75, height=150)

# Row-5
e21 = Button(root, text="%", fg ="black", bg = "#d32323", font = ("",16),command =lambda: f("%"),relief="raised", border =10)
e21.place(x=0,y=450, width=75, height=75)

e22 = Button(root, text="0", fg ="black", bg = "orange", font = ("",16),command =lambda: f("0"),relief="raised", border =10)
e22.place(x=75,y=450, width=75, height=75)

e23 = Button(root, text=".", fg ="black", bg = "#d32323", font = ("",16),command =lambda: f("."),relief="raised", border =10)
e23.place(x=150,y=450, width=75, height=75)



root.mainloop()