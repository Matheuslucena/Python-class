import Tkinter
from time import strftime

def timer():
  box = Tkinter.Tk()
  clock = Tkinter.Label()
  clock['text'] = strftime('%H:%M:%S')
  clock['font'] = "Helvetica 120 bold"
  clock.pack()
  box.mainloop()
  now = strftime('%H:%M:%S')
  if clock['text'] != now:
    clock['text'] = strftime('%H:%M:%S')
  box.after(100, timer)
   
timer()
