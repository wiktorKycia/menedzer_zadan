from tkinter import *

okno = Tk()


def pokaz():
    global window
    window = Tk()

    window.mainloop()
    pokaz()


pokaz()
okno.mainloop()
