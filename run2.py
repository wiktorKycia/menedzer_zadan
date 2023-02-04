from tkinter import *

root = Tk()
root.geometry("500x200")

label_var = StringVar(root, 'Find in the list or type here: ')
label = Label(root, textvariable=label_var)
label.pack()
label.place(x=10, y=10)

entry_var = StringVar(root)
entry_var.set('type task name')
edit = Entry(root, textvariable=entry_var)
edit.pack()
edit.place(x=10, y=30, width=150)

list_label = Label(root, text='Here is your list of tasks')
list_label.pack()
list_label.place(x=10, y=60)

listbox = Listbox(root, width=50, height=4)
listbox.pack()
listbox.place(x=10, y=80)


def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = file.readlines()
    file.close()


def show_tasks():
    import_from_file('tasks.txt')
    for task in list_of_tasks:
        listbox.insert(END, task)

# zrobić funkcje pokaż, która wypisuje zadania z list_od_tasks w listboxie
# buttony: edit_task, add_task, remove_task

show_tasks()

root.mainloop()
