import tkinter as tk
from tkinter import messagebox

TASKS_FILE = "tasks.txt"

def load_tasks():
    try:
        with open(TASKS_FILE, "r") as f:
            return f.read().splitlines()
    except FileNotFoundError:
        return []

def save_tasks(tasks):
    with open(TASKS_FILE, "w") as f:
        for task in tasks:
            f.write(task + "\n")

def add_task():
    task = entry.get()
    if task:
        listbox.insert(tk.END, task)
        entry.delete(0, tk.END)
        save_tasks(listbox.get(0, tk.END))

def delete_task():
    selected = listbox.curselection()
    if selected:
        listbox.delete(selected)
        save_tasks(listbox.get(0, tk.END))
    else:
        messagebox.showwarning("Warning", "Select a task to delete.")

# GUI setup
root = tk.Tk()
root.title("To-Do List")

entry = tk.Entry(root, width=30)
entry.pack(pady=10)

add_btn = tk.Button(root, text="Add Task", command=add_task)
add_btn.pack()

listbox = tk.Listbox(root, width=45, height=10)
listbox.pack()

delete_btn = tk.Button(root, text="Delete Task", command=delete_task)
delete_btn.pack(pady=5)

# Load existing tasks
for task in load_tasks():
    listbox.insert(tk.END, task)

root.mainloop()
