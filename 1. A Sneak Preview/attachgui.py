from tkinter import *
from tkinter102 import MyGui

main_win = Tk()
Label(main_win, text=__name__).pack()

# popup window
pop_up = Toplevel()
Label(pop_up, text='Attach').pack(side=LEFT)
MyGui(pop_up).pack(side=RIGHT)
main_win.mainloop()
