from tkinter import *

root = Tk()
main_height = 800
main_width = 500
root.geometry(str(main_width)+"x"+str(main_height))
frames_list = []


def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = file.readlines()
    file.close()


def show_tasks():
    import_from_file("tasks.txt")
    global frame
    for i, task in enumerate(list_of_tasks):
        frame = Frame(root, height=50, width=250, relief=RAISED, borderwidth=5)
        frame.pack(side=LEFT)
        frames_list.append(frame)

        global label1
        label1 = Label(frame, text=str(i+1)+": ", padx=10)
        label1.place(in_=frame, x=10, y=0)

        global label2
        label2 = Label(frame, text=task)
        label2.place(in_=frame, x=30, y=0)

        global delete_button
        delete_button = Button(frame, text="delete")
        delete_button.place(in_=frame, x=120, y=0)



def show_adding():
    global task_name
    task_name = StringVar()

    global entry
    entry = Entry(root, textvariable=task_name)
    entry.pack()

    global plus
    plus = Button(root, text="+", command=add_task)
    plus.pack(after=entry)


def clear_frames():
    for i in frames_list:
        i.destroy()


def clear_adding():
    entry.destroy()
    plus.destroy()


def add_task():
    file = open("tasks.txt", "a+")
    new_task = str(task_name)
    file.write(new_task+"\n")
    file.close()
    clear_frames()
    clear_adding()
    show_tasks()
    show_adding()


show_tasks()
show_adding()

root.mainloop()
