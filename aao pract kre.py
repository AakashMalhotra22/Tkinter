from tkinter import*
import time

visual = Tk()
sample = Label(visual, text="Hello python!")
sample.pack()
#visual.update()
time.sleep(2)
sample.pack_forget()
# visual.update()



visual.mainloop()