import tkinter as tk
from tkinter import messagebox

# Function to add a task
def add_task():
    task = task_entry.get()
    if task != "":
        tasks_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
    else:
        messagebox.showwarning("Warning", "You must enter a task.")

# Function to delete a selected task
def delete_task():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        tasks_listbox.delete(selected_task_index)
    except:
        messagebox.showwarning("Warning", "You must select a task to delete.")

# Function to mark a selected task as completed
def mark_task_completed():
    try:
        selected_task_index = tasks_listbox.curselection()[0]
        task = tasks_listbox.get(selected_task_index)
        tasks_listbox.delete(selected_task_index)
        tasks_listbox.insert(tk.END, task + " (completed)")
    except:
        messagebox.showwarning("Warning", "You must select a task to mark as completed.")

# Create the main window
root = tk.Tk()
root.title("Fashionable To-Do List")
root.geometry("400x500")
root.configure(bg='#333333')

# Create a frame for the gradient background
canvas = tk.Canvas(root, width=400, height=500)
canvas.grid(row=0, column=0)
gradient = canvas.create_rectangle(0, 0, 400, 500, fill="white", outline="")

# Define the gradient colors
colors = ["#ffcccc", "#ff99cc", "#ff66cc", "#ff33cc", "#ff00cc", "#cc00cc"]
for i, color in enumerate(colors):
    canvas.create_rectangle(0, i*500//len(colors), 400, (i+1)*500//len(colors), fill=color, outline="")

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='#333333')
frame.place(relwidth=0.95, relheight=0.9, relx=0.025, rely=0.025)

# Create an entry widget for adding tasks
task_entry = tk.Entry(frame, width=30, font=('Helvetica', 14), borderwidth=2, relief='solid')
task_entry.pack(padx=20, pady=10)

# Create buttons for adding, deleting, and marking tasks
add_task_button = tk.Button(frame, text="Add Task", command=add_task, bg='#ff9999', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
add_task_button.pack(pady=5)

delete_task_button = tk.Button(frame, text="Delete Task", command=delete_task, bg='#ff6666', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
delete_task_button.pack(pady=5)

mark_task_completed_button = tk.Button(frame, text="Mark Completed", command=mark_task_completed, bg='#66cc66', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
mark_task_completed_button.pack(pady=5)

# Create a listbox to display tasks
tasks_listbox = tk.Listbox(frame, width=50, height=10, font=('Helvetica', 14), bg='#ffffff', fg='#333333', selectbackground='#ff9999', selectforeground='#ffffff', borderwidth=2, relief='solid')
tasks_listbox.pack(pady=20)

# Create a label for the copyright notice
copyright_label = tk.Label(root, text="© 2024 Manoj Paloi", font=('Helvetica', 10), bg='#333333', fg='#ffffff')
copyright_label.place(relx=0.5, rely=0.96, anchor='center')

# Run the application
root.mainloop()
