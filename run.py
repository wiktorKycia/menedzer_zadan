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
    for i, task in enumerate(list_of_tasks):
        frame = Frame(root, height=100, relief=RAISED, borderwidth=5)
        frame.pack(fill=X)
        global label1
        label1 = Label(frame, text=str(i+1)+": ", padx=10, height=20)


show_tasks()

root.mainloop()
