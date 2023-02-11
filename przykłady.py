import os

list = os.listdir("./files/")
print(list)
print(os.path.exists("./files/task_name.txt"))
os.remove("./files/task_name.txt")
