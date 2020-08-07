from tkinter import*
root = Tk()
root.title("Tkinter variables...")


# Using with labels.

v = StringVar(root, value="hi")
label = Label(root,textvariable=v, border="5", relief="sunken", bg="red").pack(fill=X,pady=5)


# Using with Button..
v1 = DoubleVar(root, value=5.0)
button = Button(root, textvariable=v1, relief="sunken", bg="green").pack(fill=X,pady=5)


# Using with Entry..
v2 = DoubleVar(root, value=5.0)
# This shows the 5.0 value already written in Entry widget.
entry = Entry(root, textvariable=v2, relief="sunken", bg="blue",fg ="white", justify="center").pack(fill=X,pady=5)


# Can be used with checkboxes and other things, will discussed later.

root.mainloop()
