import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")
        self.root.geometry("400x300") 

        
        self.tasks = []

        
        self.create_widgets()

    def create_widgets(self):
        
        self.task_entry = tk.Entry(self.root, width=30, font=('Arial', 12))
        self.task_entry.grid(row=0, column=0, padx=10, pady=10)

        
        add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#4CAF50", fg="white", font=('Arial', 12))
        add_button.grid(row=0, column=1, padx=10, pady=10)

        
        self.task_listbox = tk.Listbox(self.root, width=40, height=10, font=('Arial', 12))
        self.task_listbox.grid(row=1, column=0, columnspan=2, padx=10, pady=10)

        
        display_button = tk.Button(self.root, text="Display Tasks", command=self.display_tasks, bg="#3498db", fg="white", font=('Arial', 12))
        display_button.grid(row=2, column=0, padx=10, pady=10)

        
        complete_button = tk.Button(self.root, text="Mark as Completed", command=self.complete_task, bg="#e74c3c", fg="white", font=('Arial', 12))
        complete_button.grid(row=2, column=1, padx=10, pady=10)

        
        update_button = tk.Button(self.root, text="Update Task", command=self.update_task, bg="#2ecc71", fg="white", font=('Arial', 12))
        update_button.grid(row=3, column=0, padx=10, pady=10)

        
        remove_button = tk.Button(self.root, text="Remove Task", command=self.remove_task, bg="#e67e22", fg="white", font=('Arial', 12))
        remove_button.grid(row=3, column=1, padx=10, pady=10)

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def display_tasks(self):
        if not self.tasks:
            messagebox.showinfo("Task List", "No tasks available.")
        else:
            task_str = "\n".join(self.tasks)
            messagebox.showinfo("Task List", task_str)

    def complete_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            completed_task = self.task_listbox.get(selected_index)
            self.tasks.remove(completed_task)
            self.task_listbox.delete(selected_index)

    def update_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            updated_task = self.task_entry.get()
            if updated_task:
                self.tasks[selected_index[0]] = updated_task
                self.task_listbox.delete(selected_index)
                self.task_listbox.insert(selected_index, updated_task)
                self.task_entry.delete(0, tk.END)
            else:
                messagebox.showwarning("Warning", "Please enter an updated task.")

    def remove_task(self):
        selected_index = self.task_listbox.curselection()
        if selected_index:
            removed_task = self.task_listbox.get(selected_index)
            self.tasks.remove(removed_task)
            self.task_listbox.delete(selected_index)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
