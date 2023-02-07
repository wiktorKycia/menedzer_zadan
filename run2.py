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
mainmenu.add_cascade(label='Setttings', menu=settings_menu)

opt_menu.add_command(label='Add task')
opt_menu.add_command(label='Remove task')
opt_menu.add_separator()
opt_menu.add_command(label='Show tasks in text window')


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


def show_adding_window():
    global window
    window = Tk()
    window.title('Add a new task')
    window.geometry('200x200')
    global enter_name_label  # label do task name'a
    enter_name_label = Label(window, text='Enter here task name: ')

    global entry_task_name_var  # zmienna przechwytująca to co jest w entry
    entry_task_name_var = StringVar()

    global entry_task_name  # pole do wpisania nazwy zadania
    entry_task_name = Entry(window, textvariable=entry_task_name_var)

    global task_description_label  # label do pola na opis zadania
    task_description_label = Label(window, text='Enter here task description: ')

    global task_description  # pole opisowe zadania
    task_description - Text(window)

    global plus
    plus = Button(window, text='add task', command=add_task)

    window.mainloop()


def clear_all_tasks():
    os.remove('tasks.txt')
    file = open('tasks.txt', 'a+')
    file.close()
    show_tasks()


def listbox_select(index):
    entry_var.set(listbox.get(listbox.curselection()))


# Opis zadań, pole textowe przy dodawaniu zadań
'''
Tutorial(menu) jak korzystać z menagera,
messagebox zaimportować
obsługa wyjątków
(przy entry, jeśli nie ma takiego zadania w liście, lub pliku)
'''

listbox.bind('<<ListboxSelect>>', listbox_select)

# BUTTONS
# Require new window
add_task_button = Button(root, text='new task')
''' 
tworzy nowe okno, w którym użytkownik nadaje nazwę zadaniu i daje mu któtki opis, 
label: 'enter task name:', 
entry: ~nazwa zadania~, StringVar - przechwycony przez Button
label: 'enter here description', 
pole text: ~opis zadania~, - utworzyć oddzielny plik w folderze o nazwie ze StringVara i treści z opisu
button: add task, - komenda add_task(), - zmodyfikować
'''

# Choose from the list
remove_task_button = Button(root, text='remove task', command=remove_task)  # obsłużyć wyjątek, jeżeli nie ma takiego zadania w liście - error
read_description_button = Button(root, text='read description')  # okno z labelami
edit_task_button = Button(root, text='edit task')  # okno z polem tekstowym jak przy dodawaniu zadań
clear_all_tasks_button = Button(root, text='clear tasks list')  # okno potwierdzające

show_tasks()

root.mainloop()
