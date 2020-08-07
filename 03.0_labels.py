'''
Everything is a widget in tkinter and label is also one of them.

Label widget
1. The widget implements a display box where you can place text or images.
2. The text displayed by this widget can be updated at any time you want.
3. It also has many parameters.
4. Simple syntax:
   w = label(root, options,...)
   root- It represents the parent window.
   options- You can add many features to label widget.
'''

from tkinter import*

root =Tk()
root.title("Label widget")
root.geometry("900x900")

my_label =Label(root, text="We are doing labels", bg ="red", fg = "yellow", font=("Arial",20))
my_label.pack()

'''
There are many ways to represent your label on the screen.
1. pack()
2. place()
3. grid()
'''

my_label1 = Label(root,text="Everything is a widget in tkinter, label is also a widget.")
my_label1.pack()



#Label Options
'''
1. fg:      It means foreground, you can change the color of text by use of this, you can either write the name of color or color code.
2. bg:      It means background, you can change the color of background of text, you can either write the name of the color or the color code.
3. font:    1. It is used to change font size and font color of the text.
            2. Command font=("font_name",font_size) 


4. height:   Changes the height of the text or if you have already assigned the font size of text, then it changes the height of background of text.
5. width :   Changes the width of the text or if you have already assigned the font size of text, then it changes the width of the background.  
6. anchor:   1. It places the text on the given direction, it has following options:
             2.  e,n,s,w,ne,nw,se,sw, CENTRE-It is default.
7. justify   1. It is used to tell, how to align text, if there are many lines in label.
             2. It has three options, right,left, centre.

8.state:     1. It just used with button, to change their state, whether click able or not but you can use it with labels also.
             2. Two options either normal and disabled.



9. relief:    1. Just use to change the appearance of the text.
              2. It has five options: sunken, raised, groove,flat, ridge.
10. border:   1. Used to change the border width.
              2. It is same as borderwidth.
                 


11.wraplength: 1. It is used to break the lines in label, but the problem is that it takes parameter as pixels not as character. 
               2. If you write wraplength equals to 100, then it each line will have only 8 characters.
               3. It is better to use /n to break lines.

12. underline: 1. It is used to underline the nth character of the label text.
               2. If you want to underline 7th character,write underline =7
               3. The problem with this option is that you can underline only single character, not the whole text.
               4. To underline, whole text you have to change font.

13. cursor:    1. If you set this option to a cursor name (arrow, dot etc.), the mouse cursor will change to that pattern 
                    when it is over the checkbutton.


14. textvariable: 1. It is used when you want to change the text in the labels.

'''

#Using anchor, justify, width, height.
my_label2 = Label(root,text="We are using here: \n1. height \n2. width \n3. anchor \n4. justify ", fg ="green",bg ="orange", anchor="s", height ="7", width="20", justify="left")
my_label2.pack(pady =10)

# using state
my_label3 = Label(root, state ="disabled", font =("",12) ,text =" Using state:\n It just changes the text color to light and dull so that it looks like it is disabled\n This color is actually black but appears to be grey")
my_label3.pack(pady=10)

# using relief and border
my_label4 = Label(root, text ="Using relief and border", relief ="raised", border ="10")
my_label4.pack(pady =10)

# using wraplength and underline
my_label5 = Label(root, text ="using wraplength and underline", underline = "4", wraplength ="150", font =("",20))
my_label5.pack()

# using cursor
my_label6 = Label(root, text="cursor- dot and arrow, but changes seen in checkboxes", cursor ="dot")
my_label6.pack(pady =10)


root.mainloop()
