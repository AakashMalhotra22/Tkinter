from tkinter import *

root = Tk()
root.title("Input Entry box")
root.geometry("400x600")

'''
Attributes or options of the Entry widgets.

1. width and height: 1. width is used to change the width of the Entry widget.
                     2. There is no such option of height and if you want to change it, use internal padding - ipady.

2. cursor: 1. When your cursor is over the Entry widget, then you can change the appearance of the cursor.
           2. It has two options: cursor=dot and cursor=arrow and may be many more.

3. cursor color and width   A. insertbackground : color of the cursor.
                            B. insertwidth: width of the cursor.


4. anchor and justify: 1. There is no option of anchor in it
                       2. Justify is used to change the alignment of the text in Entry widget.
                       3. if justify=right, then text will start from the right position.
                       4. if justify = left, then text will start from the left position, it is default option.
                       5. if justify = Centre, then text will start from the centre position of the Entry widget.
5. selection text color:   A. selectbackgrond: The background color of the selected text.
                           B. selectforeground: The foregound color of the selected text.
                           C. selectborderwidth: The width of the border of the selected text.


6. insertofftime and inserontime:  A. insertontime is used to set the time for which cursor shows on the screen.
                                    B. inserofftime is used to set the time for which cursor is not on the screen.
                                    If you set insertontime =5000 and insertofftime=6000, then cursor shows on the
                                    screen  for 5 sec and then disappear for 6 sec and then again appear for 5 sec
                                    and this process goes on.                       
'''

# cursor, insertbackground and insertwidth, justify and width

label1 = Label(root, text="cursor, insertbackground, insertwidth, justify\n and width in entry box", bg="yellow",
               fg="blue", width="50", height="3").pack(pady=5)

e1 = Entry(root, width=80, cursor="dot", insertbackground="red", insertwidth='5', justify='center')
e1.pack(ipady=20, pady=5)

# insertontime and insertofftime, selectbackground, selectborderwidth, selectforeground
label2 = Label(root, text="Notice, the cursor blinking\n try selecting the text in below entry box", bg="cyan",fg="blue", width="50", height="3").pack(pady=18)

e2 = Entry(root, width=80, cursor="arrow", insertontime="10", insertofftime="20", selectbackground="green", selectforeground="yellow", selectborderwidth="5")
e2.pack(ipady=20, pady=5)

root.mainloop()