'''
Console Based programs:

1. When you run a program in console, what happens it goes through each line of code and executes the code.
2. You can stop the code, either by clicking on cross, or do some keyboard interaction.
3. Once, all the lines of code are finished being executed, it ends the execution process and gives out the result and
   now if you want to use it you have to again run it again.
4. It generates the output once.

'''
'''
Graphical Interface programs.
1. When you run a program in gui, what happens,it first run all the events in your codes and execute them to show on the graphical window.
2. After when all the execution is finished of what you have writen in the code, it does not close the graphical window.
3. Instead it waits, unless an event occur, event can be anything, like you pressed some button of it, you pressed keyboard key, you used mouse cursor.
4. It is like a infinite mainloop running, it just prints out the code, then wait for further direction and doesn't end the program unless you yourself stops it.

5. This all happens because of your root.mainloop command.
   root.mainloop is something like this:
   
   while True:
   event = wait_for_event
   event.process()
   if main_window_has_been_destroyed():
         break
         
   What it does, it is just like an infinite mainloop, initially waits for an event to occur, and whenever an event comes,
   it processes that event, for ex: if you press any keyboard key, then corresponding to this key whatever function i bind,
   that function would be executed, and whenever i destroy main window means i click on cross button, then only the mainloop
   stops working.
   
   This is what mainloop does.

6. Your graphical program would not execute without mainloop, and if it is running in some text editor like IDLE, that means
   in those editor, mainloop is already defined.

'''

