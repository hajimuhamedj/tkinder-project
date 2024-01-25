import tkinter as tk
from tkinter import messagebox

def add_task():
    task = entry_task.get()
    if task:
        listbox_tasks.insert(tk.END, task)
        entry_task.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "you not enter a task.")

def delete_task():
    try:
        selected_task_index = listbox_tasks.curselection()[0]
        listbox_tasks.delete(selected_task_index)
    except IndexError:
        messagebox.showwarning("Warning", "you not select a task to delete.")

def main():
    global entry_task, listbox_tasks

    app = tk.Tk()
    app.title("To-Do List")

    # Entry for new tasks
    entry_task = tk.Entry(app)
    entry_task.pack(pady=10)

    # Button to add tasks
    btn_add = tk.Button(app, text="Add Task", command=add_task)
    btn_add.pack(pady=5)

    # Listbox to display tasks
    listbox_tasks = tk.Listbox(app)
    listbox_tasks.pack(pady=10)

    # Button to delete tasks
    btn_delete = tk.Button(app, text="Delete Task", command=delete_task)
    btn_delete.pack(pady=5)

    app.mainloop()

if __name__ == "__main__":
    main()
