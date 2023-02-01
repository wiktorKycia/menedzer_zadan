from tkinter import *

root = Tk()
root.geometry("500x500")


def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = file.readlines()


def show_tasks():
    import_from_file("tasks.txt")
    global frame
    frame = Frame(root, height=50, relief=RAISED, borderwidth=5)
    frame.pack(fill=X)
    


root.mainloop()
