from tkinter import*
root = Tk()
root.title("bind keys")
root.geometry('400x800')

'''
Levels of bindings:
Binding in tkinter occurs at four level

1. A. widget level which is instance widget like - button, label, enrybox, such that.
   B. syntax is widget(event,handler)

2. A. parent window level or top window level or main window level- This is the first or main windows which appears on the
      screen , here it is root,
   B. syntax is main_window_name(event,handler, here it is root so root(event,handler)
   

3.  A. class level- not known
    B. syntax bind_class(event, handler)
    
4. A. Application level- for whole application, this binding works everywhere in the application in any window.
   B. syntax is bind_all(event, handler)
      For example:
      root.bind_all(<F1>, help_function), now whenever anyone presses the F1 key from anywhere in the application, 
      help function will trigger.
  
'''
#Question:
''' If we create four binding, one for widget, one for main window, one for class level and one for application level
    and event keeps the same that is <Return> and functions are different, then which function will be called.

Ans: All functions are called,
     But order of function triggering is 
     first widget level
     second main window level
     third class level
     fourth application level.    
    
    
    Given below is practical demonstratiion.
'''
def callback1(event):
    label = Label(root, text=f"This is widget level", bg="red", fg="white").pack(pady=10)

def callback2(event):
    label = Label(root, text=f"This is main window level", bg="blue", fg="white").pack(pady=10)

def callback3(event):
    label = Label(root, text=f"This is application level", bg="green", fg="white").pack(pady=10)


b1 = Button(root, text="Press Enter")
b1.focus_set()

'''Here it does not matter which line of code you write first, because always first widget level is triggered followed by
   main window level and then application level'''

root.bind_all('<Return>', callback3)
b1.bind('<Return>', callback1)
root.bind('<Return>', callback2)

b1.pack(pady=10)



root.mainloop()
