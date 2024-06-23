import tkinter as tk
from tkinter import ttk

# Function to update the expression in the entry box
def click(button):
    current = entry.get()
    entry.delete(0, tk.END)
    entry.insert(0, current + button)

# Function to evaluate the expression and display the result
def evaluate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(0, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(0, "Error")

# Function to clear the entry box
def clear():
    entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Fashionable Calculator")
root.geometry('400x550')
root.configure(bg='#333333')

# Create a frame for the gradient background
canvas = tk.Canvas(root, width=400, height=550)
canvas.grid(row=0, column=0)
gradient = canvas.create_rectangle(0, 0, 400, 550, fill="white", outline="")

# Define the gradient colors
colors = ["#ffcccc", "#ff99cc", "#ff66cc", "#ff33cc", "#ff00cc", "#cc00cc"]
for i, color in enumerate(colors):
    canvas.create_rectangle(0, i*550//len(colors), 400, (i+1)*550//len(colors), fill=color, outline="")

# Create a frame to hold the widgets
frame = tk.Frame(root, bg='#333333')
frame.place(relwidth=0.95, relheight=0.95, relx=0.025, rely=0.025)

# Create an entry widget for displaying the expression
entry = tk.Entry(frame, width=16, font=('Helvetica', 24, 'bold'), borderwidth=2, relief='solid', bg='#ffffff', fg='#333333', justify='right')
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=20)

# Define the buttons with colors
buttons = [
    ('7', '#ff9999'), ('8', '#ff9999'), ('9', '#ff9999'), ('/', '#ffcc99'), 
    ('4', '#99ff99'), ('5', '#99ff99'), ('6', '#99ff99'), ('*', '#ffcc99'), 
    ('1', '#99ccff'), ('2', '#99ccff'), ('3', '#99ccff'), ('-', '#ffcc99'), 
    ('0', '#ff99ff'), ('C', '#ff6699'), ('=', '#6699ff'), ('+', '#ffcc99')
]

# Add buttons to the grid
style = ttk.Style()
style.configure('TButton', font=('Helvetica', 18, 'bold'), borderwidth=1, focusthickness=3, focuscolor='none')
style.map('TButton', background=[('active', '#666666')], foreground=[('active', '#ffffff')])

row_val = 1
col_val = 0

for (button, color) in buttons:
    if button == "=":
        btn = tk.Button(frame, text=button, width=4, height=2, font=('Helvetica', 18, 'bold'), command=evaluate, bg=color, fg='#ffffff', borderwidth=2, relief='raised')
    elif button == "C":
        btn = tk.Button(frame, text=button, width=4, height=2, font=('Helvetica', 18, 'bold'), command=clear, bg=color, fg='#ffffff', borderwidth=2, relief='raised')
    else:
        btn = tk.Button(frame, text=button, width=4, height=2, font=('Helvetica', 18, 'bold'), command=lambda b=button: click(b), bg=color, fg='#ffffff', borderwidth=2, relief='raised')
    btn.grid(row=row_val, column=col_val, padx=5, pady=5)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1



# Create a label for the copyright notice
copyright_label = tk.Label(root, text="© 2024 Manoj", font=('Helvetica', 10), bg='#333333', fg='#ffffff')
copyright_label.place(relx=0.5, rely=0.96, anchor='center')



# Run the application
root.mainloop()
