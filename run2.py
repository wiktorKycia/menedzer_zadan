from tkinter import *
import os
from tkinter import messagebox as msg

root = Tk()
root.geometry("500x200")


# FUNCTIONS
def import_from_file(file_name):
    file = open(file_name, "r")
    global list_of_tasks
    list_of_tasks = []
    for line in file.readlines():
        list_of_tasks.append(line.strip())
    file.close()


def show_tasks():
    import_from_file('tasks.txt')
    listbox.delete(0, END)
    for task in list_of_tasks:
        listbox.insert(END, task)


def check_in_list(name):
    if name not in list_of_tasks:
        msg.showerror("Error", "There is no such task in the list")
    else:
        pass


def find_in_listbox():
    import_from_file('tasks.txt')
    index = 0
    task_name = entry_var.get().strip()

    check_in_list(task_name)

    for i, elem in enumerate(list_of_tasks):
        elem.strip()
        if elem == task_name:
            index = i
    listbox.see(index)


def remove_task():  # wyjątek jeśli nie ma zadania
    import_from_file('tasks.txt')
    task_name = entry_var.get()

    check_in_list(task_name)

    for task in list_of_tasks:
        if task == task_name:
            list_of_tasks.remove(task)

    file = open('tasks.txt', 'w')
    for task in list_of_tasks:
        file.write(task+"\n")
    file.close()

    path = "./files/" + task_name + ".txt"
    try:
        os.remove(path)
    except FileNotFoundError:
        msg.showerror("ERROR", "File: {} does not exists".format(task_name))

    show_tasks()


def add_task():
    file = open('tasks.txt', 'a+')
    new_task = entry_task_name_var.get()
    file.write(new_task+'\n')
    file.close()

    global description
    description = task_description.get(1.0, END)
    file = open('files/{}.txt'.format(new_task), 'a+')
    file.writelines(description)
    file.close()

    show_tasks()
    window.destroy()


def show_adding_window():
    global window
    window = Tk()
    window.title('Add a new task')
    window.geometry('300x200')

    global enter_name_label  # label do task name'a
    enter_name_label = Label(window, text='Enter here task name: ')
    enter_name_label.pack()
    enter_name_label.place(x=10, y=10)

    global entry_task_name_var  # zmienna przechwytująca to co jest w entry
    entry_task_name_var = StringVar(master=window)

    global entry_task_name  # pole do wpisania nazwy zadania
    entry_task_name = Entry(window, textvariable=entry_task_name_var)
    entry_task_name.pack()
    entry_task_name.place(x=10, y=30)

    global task_description_label  # label do pola na opis zadania
    task_description_label = Label(window, text='Enter here task description: ')
    task_description_label.pack()
    task_description_label.place(x=10, y=50)

    global task_description  # pole opisowe zadania
    task_description = Text(window, width=130, height=280,)
    task_description.pack()
    task_description.place(x=10, y=70)

    global plus  # przycisk dodający zadanie
    plus = Button(window, text='add task', command=add_task)
    plus.pack()
    plus.place(x=220, y=10)

    window.mainloop()


def close_confirming():
    window_c.destroy()


def clear_all_tasks():
    open('tasks.txt', 'w').close()

    for file in os.listdir('files'):
        try:
            os.remove(file)
        except FileNotFoundError:
            print("nie odnaleziono pliku")

    show_tasks()
    window_c.destroy()


def show_confirming_window():
    global window_c
    window_c = Tk()
    window_c.geometry("300x100")
    window_c.title('Delete all tasks')

    global info
    info = Label(window_c, text='This operation will delete all the tasks from your list')
    info.pack()
    #info.place(x=10, y=10)

    global cancel_button
    cancel_button = Button(window_c, text='Cancel', command=close_confirming)
    cancel_button.pack()
    cancel_button.place(x=100, y=30)

    global confirm_button
    confirm_button = Button(window_c, text='Confirm', command=clear_all_tasks)
    confirm_button.pack()
    confirm_button.place(x=150, y=30)

    window_c.mainloop()


def confirm_editing():
    task_name = entry_new_task_name_var.get()
    path1 = "./files/" + entry_var.get() + ".txt"
    path2 = "./files/" + task_name + ".txt"
    os.rename(path1, path2)

    global new_description
    new_description = new_task_description.get(1.0, END)

    file = open(path2, "w+")
    file.write(new_description)
    file.close()
    window_e.destroy()


def edit_task():
    task_name = entry_var.get()
    if task_name not in list_of_tasks:
        msg.showerror("Error", "There is no such task in the list")
    else:
        global window_e
        window_e = Tk()
        window_e.geometry('300x200')

        global enter_new_name_label
        enter_new_name_label = Label(window_e, text='Enter here new task name: ')
        enter_new_name_label.pack()
        enter_new_name_label.place(x=10, y=10)

        global entry_new_task_name_var
        entry_new_task_name_var = StringVar(master=window_e)

        global entry_new_task_name
        entry_new_task_name = Entry(window_e, textvariable=entry_new_task_name_var)
        entry_new_task_name.pack()
        entry_new_task_name.place(x=10, y=30)

        global new_task_description_label
        new_task_description_label = Label(window_e, text='Enter here task description: ')
        new_task_description_label.pack()
        new_task_description_label.place(x=10, y=50)

        global new_task_description
        new_task_description = Text(window_e, width=130, height=280)
        new_task_description.pack()
        new_task_description.place(x=10, y=70)

        global edit_e
        edit_e = Button(window_e, text='edit task', command=confirm_editing)
        edit_e.pack()
        edit_e.place(x=220, y=10)

        entry_new_task_name_var.set(task_name)

        file_path = "./files/" + task_name + ".txt"
        file = open(file_path, "r")
        for line in file.readlines():
            new_task_description.insert(END, line)

        file.close()

        window_e.mainloop()


def listbox_select(index):
    entry_var.set(listbox.get(listbox.curselection()))


# WIDGETS
# Entry
label_var = StringVar(root, 'Find in the list or type here: ')
label = Label(root, textvariable=label_var)
label.pack()
label.place(x=10, y=10)

entry_var = StringVar(root)
entry_var.set('type task name...')
edit = Entry(root, textvariable=entry_var)
edit.pack()
edit.place(x=10, y=30, width=150)

# Listbox
list_label = Label(root, text='Here is your list of tasks')
list_label.pack()
list_label.place(x=10, y=60)

listbox = Listbox(root, width=50, height=6)
listbox.pack()
listbox.place(x=10, y=80)

# MENUS
mainmenu = Menu()
root.config(menu=mainmenu)

opt_menu = Menu(mainmenu)
mainmenu.add_cascade(label='Options', menu=opt_menu)

settings_menu = Menu(mainmenu)
mainmenu.add_cascade(label='Settings', menu=settings_menu)

opt_menu.add_command(label='Add task', command=show_adding_window)
opt_menu.add_command(label='Remove task', command=remove_task)
opt_menu.add_command(label='Edit task', command=edit_task)
opt_menu.add_separator()
opt_menu.add_command(label='Show tasks in text window')
opt_menu.add_separator()
opt_menu.add_command(label='clear all tasks', command=show_confirming_window)


# Opis zadań, pole textowe przy dodawaniu zadań
'''
Tutorial(menu) jak korzystać z menagera,
messagebox zaimportować
obsługa wyjątków
(przy entry, jeśli nie ma takiego zadania w liście, lub pliku)
'''

listbox.bind('<<ListboxSelect>>', listbox_select)

# BUTTONS
# Require new, confirming window
add_task_button = Button(root, text='new task', command=show_adding_window)
clear_all_tasks_button = Button(root, text='clear tasks list', command=show_confirming_window)  # okno potwierdzające

# Choose from the list
find_button = Button(root, text='find', command=find_in_listbox)
remove_task_button = Button(root, text='remove task', command=remove_task)
edit_task_button = Button(root, text='edit task', command=edit_task)  # okno z polem tekstowym jak przy dodawaniu zadań

# packing
add_task_button.pack()
remove_task_button.pack()
edit_task_button.pack()
clear_all_tasks_button.pack()
find_button.pack()

# placing
add_task_button.place(x=325, y=10)
remove_task_button.place(x=325, y=40)
edit_task_button.place(x=325, y=70)
clear_all_tasks_button.place(x=325, y=100)
find_button.place(x=165, y=25)

show_tasks()

root.mainloop()
