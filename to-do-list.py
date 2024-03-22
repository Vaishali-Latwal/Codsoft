import tkinter as tk
from tkinter import messagebox
class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.frame_tasks = tk.Frame(root)
        self.frame_tasks.pack()

        self.listbox_tasks = tk.Listbox(self.frame_tasks, height=10, width=50)
        self.listbox_tasks.pack(side=tk.LEFT)

        self.scrollbar_tasks = tk.Scrollbar(self.frame_tasks)
        self.scrollbar_tasks.pack(side=tk.RIGHT, fill=tk.Y)

        self.listbox_tasks.config(yscrollcommand=self.scrollbar_tasks.set)
        self.scrollbar_tasks.config(command=self.listbox_tasks.yview)

        self.entry_task = tk.Entry(root, width=70)
        self.entry_task.pack()

        add_task_button = tk.Button(root, text="Add task", width=40, command=self.add_task)
        add_task_button.pack()

        delete_task_button = tk.Button(root, text="Delete task", width=40, command=self.delete_task)
        delete_task_button.pack()

        update_task_button = tk.Button(root, text="Update task", width=40, command=self.update_task)
        update_task_button.pack()

        save_tasks_button = tk.Button(root, text="Save tasks", width=40, command=self.save_tasks)
        save_tasks_button.pack()

        quit_button = tk.Button(root, text="Quit", width=40, command=root.quit)
        quit_button.pack()

        self.load_tasks()

    def add_task(self):
        task = self.entry_task.get()
        if task:
            self.listbox_tasks.insert(tk.END, task)
            self.entry_task.delete(0, tk.END)
        else:
            messagebox.showwarning("Warning", "Please enter a task.")

    def delete_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            self.listbox_tasks.delete(task_index)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            task_index = self.listbox_tasks.curselection()[0]
            task_text = self.listbox_tasks.get(task_index)

            new_task = simpledialog.askstring("Update task", "Click a task to update:", initialvalue=task_text)
            if new_task:
                self.listbox_tasks.delete(task_index)
                self.listbox_tasks.insert(task_index, new_task)
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def save_tasks(self):
        tasks = self.listbox_tasks.get(0, tk.END)
        with open("tasks.txt", "w") as f:
            for task in tasks:
                f.write(task + "\n")
        messagebox.showinfo("Information", "Tasks saved successfully.")

    def load_tasks(self):
        try:
            with open("tasks.txt", "r") as f:
                for line in f:
                    self.listbox_tasks.insert(tk.END, line.strip())
        except FileNotFoundError:
            pass

if __name__ == "__main__":
    root = tk.Tk()
    todo_app = TodoApp(root)
    root.mainloop()
