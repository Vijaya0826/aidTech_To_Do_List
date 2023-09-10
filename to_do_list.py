from tkinter import *
from tkinter import messagebox
import pickle

def add_task():
    task = entry_task.get()
    if task != "":
        listbox_tasks.insert(END, task)
        entry_task.delete(0,END)
    else:
        messagebox.showwarning(title="warning!", message="you must enter a task")

def delete_task():
    try:
        task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(task_index)
    except:
        messagebox.showwarning(title="warning!", message="you must select a task")
    
def load_tasks():
    try:
        tasks = pickle.load(open("tasks.dat","rb"))
        listbox_tasks.delete(0, END)
        for task in tasks:
            listbox_tasks.insert(END, task)
    except:
        messagebox.showwarning(title="warning!", message="cannot find tasks.dat")
     
def save_tasks():
    tasks = listbox_tasks.get(0, listbox_tasks.size())
    pickle.dump(tasks, open("tasks.dat","wb"))


root = Tk()
root.title("To_do_list")
root.geometry("500x350")


frame_tasks = Frame(root)
frame_tasks.pack()

listbox_tasks = Listbox(frame_tasks, height=10, width=50)
listbox_tasks.pack(side=LEFT)

scrollbar_tasks = Scrollbar(frame_tasks)
scrollbar_tasks.pack(side=RIGHT, fill=Y)

listbox_tasks.config(yscrollcommand=scrollbar_tasks.set)
scrollbar_tasks.config(command=listbox_tasks.yview)

entry_task = Entry(root, width=50)
entry_task.pack()

btn_add_task = Button(root, text="Add task", command=add_task)
btn_add_task.pack()

btn_delete_task = Button(root, text="delete task", command=delete_task)
btn_delete_task.pack()

btn_load_tasks = Button(root, text="load tasks", command=load_tasks)
btn_load_tasks.pack()

btn_save_tasks = Button(root, text="save tasks", command=save_tasks)
btn_save_tasks.pack()

root.mainloop()
