from tkinter import *
import os

root = Tk()
root.geometry("500x200")

# WIDGETS
# Entry
label_var = StringVar(root, 'Find in the list or type here: ')
label = Label(root, textvariable=label_var)
label.pack()
label.place(x=10, y=10)

entry_var = StringVar(root)
entry_var.set('type task name')
edit = Entry(root, textvariable=entry_var)
edit.pack()
edit.place(x=10, y=30, width=150)

# Listbox
list_label = Label(root, text='Here is your list of tasks')
list_label.pack()
list_label.place(x=10, y=60)

listbox = Listbox(root, width=50, height=4)
listbox.pack()
listbox.place(x=10, y=80)


# FUNCTIONS
def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = file.readlines()
    file.close()


def show_tasks():
    import_from_file('tasks.txt')
    for task in list_of_tasks:
        listbox.insert(END, task)


def remove_task():
    import_from_file('tasks.txt')
    task_name = str(entry_var)
    for task in list_of_tasks:
        if task == task_name:
            list_of_tasks.remove(task)
    os.remove('tasks.txt')
    file = open('tasks.txt', 'a+')
    for task in list_of_tasks:
        file.write(task)
    show_tasks()


def add_task():
    import_from_file('tasks.txt')
    new_task = str(entry_var)
    list_of_tasks.append(new_task)
    file = open('tasks.txt', 'a+')
    file.write(new_task+"\n")
    file.close()
    show_tasks()
'''
def clear_tasks():
    file = open('tasks.txt', 'a+')
    file.
'''

# buttony: edit_task, 

show_tasks()

root.mainloop()
