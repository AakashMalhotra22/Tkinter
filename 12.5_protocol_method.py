from tkinter import *
from tkinter import messagebox
root = Tk()

'''
Protocol handlers:
1. tkinter also supports protocol handlers
2. Protocol refers to the interaction between the application and window manager.
   For example:
   closing tkinter app by use of task manager, so if you have not used any protocol , then your tkinter application
   will be closed and your all data which is in tkinter is lost.
   To avoid this, we use protocol 
   
3. The most common used protocol is WM_DELETE_WINDOW
   It is used to define what happens when user explicitly closes  window using the window manager.
   Here you can use protocol handlers, means when any protocol is called then a callback function is triggered.
   so whenever anyone try to close window by use of window manager, a callback function can be created using 
   protocol handlers.
   
'''

# Example

# The handler which is to be triggered at the time of protocol.
def callback():
    if messagebox.askokcancel("Quit", "Do you really wish to quit?"):
        root.destroy()

# So here whenever anyone tries to close the window, callback function is triggered.
root.protocol("WM_DELETE_WINDOW", callback)

root.mainloop()