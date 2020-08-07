from tkinter import*
from PIL import ImageTk, Image
root = Tk()
root.geometry("900x500")

'''
Attributes of text widgets:
1. Common:                 A. bg, fg, relief, font, border
2. height and width:       A. Height is in line, if height=6 means 6 lines deep.
                           B. Width is in number of characters, if width= 40, means one line has 60 characters.

# cursor related attributes                         
3. cursor:                 A. Same as in entry widget, you can change it to dot, arrow.
4. insertbackground        A. Color of the cursor.
5. insertwidth             A. width of the cursor.
6. insertofftime:          A. for how much milliseconds cursor disappears from the screen at the time of blinking.           
7. insertontime:           A. for how much milliseconds cursor appears oon the screen at the time of blinking.

# Boundary arount text widget 
8. highlightbackground     A. The color of the boundary of the text widget when the text widget does not have focus.
9. highlightcolor          A. The ocolor of the boundary of the text widget when the text widget has focu.
10. highlightthickness:    A. The thickness of the boundary around the text widget.
#Note: Border and boundary are not same, they are different.
#      Border comes before boundary.

# Selection changes:
11. selectbackground:      A. The background color the selected text.
12. selectforeground:      A. The foreground color the selected text.
13. selectborderwidth      A. The borderwidth of the selected text.

# Line spacing.
One things that needs to be understand.
Consider your text widget is of 6 lines and each line can have maximum 40 characters.
Then,
1. If you are writing continuously without pressing enter and filled 3 lines(120 characters) of text box,
   then it is considered as one line in text widget.
   (Unless you press ENTER KEY, new line does not start.)

2. if you have written 3 characters in one line and then pressed enter, then written 4 characters in the line, then 
   pressed enter, then it is considered as two line...
   
   
14. spacing1:             A. It specifies how much vertical space should be put above each line of text.   
15. spacing2:             A. It specifies how much extra vertical space to add between displayed line of text
                             (These means you have filled three lines without pressing ENTER KEY, then how much space
                              among each of them, because these three lines are considered as one.)

15. spacing1:             A. It specifies how much vertical space should be put below each line of text.   


#New one

16. tab:                  A. How many character space should a tab give, tab=50, means if you press tab key it gives
                             50 character space.

17. wrap:                 A. It has two option wrap=WORD or wrap=CHAR, which means how to wrap.
                          B. Sometimes your word is not completed but the line is finished, so you have two options
                             first: break the word, write a few characters of word in first line and rest of the
                                    characters in the second line. This is wrap=CHAR
                             second: write the whole word in next line because it doesnot fit in this line, this is
                                     wrap=WORD

'''

# All are done in one code...

y = Text(root,bg="pink", fg="blue", height="6", width="40",border="1", # Common and height and width
          cursor="dot",insertbackground="red", insertwidth="5",   # cursor
          insertofftime="1", insertontime="1", # cursor blinking
          highlightbackground="yellow", highlightcolor="green", highlightthickness="10", # Boundary
          selectbackground="yellow", selectborderwidth="50", selectforeground="black", # selection colors
          spacing1=10,spacing2=5, spacing3=10, # spacing
          tabs="50", wrap="word") #new

y.pack(pady=10)

# This is another text widget just to show boundary magic, change the focus between them
y2 = Text(root, wrap=CHAR, height="4", width="20",
          highlightbackground="red", highlightcolor="orange", highlightthickness="20")

y2.pack(pady=10)

root.mainloop()