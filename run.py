from tkinter import *

root = Tk()

# SIZES
main_frame_width = 300
main_frame_height = 300
nav_width = 150
nav_height = 200
main_height = main_frame_height
main_width = main_frame_width + nav_width
root.geometry(str(main_width)+"x"+str(main_height))

# LISTS
frames_list = []


# PANELS
panedwindow = PanedWindow(root, orient=HORIZONTAL)
panedwindow.pack(fill=BOTH, expand=True)

# FRAMES
main_frame = Frame(panedwindow, width=main_frame_width, height=main_frame_height, relief=SUNKEN, borderwidth=5)
nav = Frame(panedwindow, width=nav_width, height=nav_height, relief=SUNKEN, borderwidth=5)
panedwindow.add(main_frame)
panedwindow.add(nav)


# FUNCTIONS
def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = file.readlines()
    file.close()


def show_tasks():
    import_from_file("tasks.txt")
    global frame
    for i, task in enumerate(list_of_tasks):
        frame = Frame(main_frame, height=50, width=250, relief=RAISED, borderwidth=5)
        frame.pack()
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
    entry = Entry(nav, textvariable=task_name)
    entry.grid(row=0, column=0)

    global plus
    plus = Button(nav, text="+", command=add_task)
    plus.grid(row=0, column=1)


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
