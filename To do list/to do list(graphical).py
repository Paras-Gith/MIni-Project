import tkinter as tk
from tkinter import messagebox, simpledialog

tasks = []

#adding task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks.append(task)
        update_listbox()
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "Task cannot be empty!")

# function to update task
def update_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        new_task = simpledialog.askstring("Update Task", "Enter new task:")
        if new_task:
            tasks[index] = new_task
            update_listbox()
    else:
        messagebox.showwarning("Warning", "Please select a task to update!")

# function to delete task
def delete_task():
    selected_task = tasks_listbox.curselection()
    if selected_task:
        index = selected_task[0]
        task_name = tasks[index]
        del tasks[index]
        update_listbox()
        messagebox.showinfo("Deleted", f"Task '{task_name}' deleted successfully!")
    else:
        messagebox.showwarning("Warning", "Please select a task to delete!")

# function to view tasks
def view_tasks():
    if tasks:
        messagebox.showinfo("All Tasks", "\n".join(tasks))
    else:
        messagebox.showinfo("All Tasks", "No tasks found!")

# function to update the listbox
def update_listbox():
    tasks_listbox.delete(0, tk.END)
    for task in tasks:
        tasks_listbox.insert(tk.END, task)

# function to exit program
def exit_app():
    root.destroy()

# main window
root = tk.Tk()
root.title("To-Do List App")
root.geometry("400x400")

# entry box
task_entry = tk.Entry(root, width=30, font=("Arial", 14))
task_entry.pack(pady=10)

# buttons
add_button = tk.Button(root, text="Add Task", command=add_task, bg="lightgreen")
add_button.pack(pady=5)

update_button = tk.Button(root, text="Update Task", command=update_task)
update_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", command=delete_task)
delete_button.pack(pady=5)

view_button = tk.Button(root, text="View Tasks", command=view_tasks)
view_button.pack(pady=5)

exit_button = tk.Button(root, text="Exit", command=exit_app)
exit_button.pack(pady=5)

# listbox to display tasks
tasks_listbox = tk.Listbox(root, width=40, height=10, font=("Arial", 12))
tasks_listbox.pack(pady=10)

# run the app
root.mainloop()
