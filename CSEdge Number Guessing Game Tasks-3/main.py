import tkinter as tk
import random

# Function to start/restart the game
def start_game():
    global secret_number, attempts_left
    secret_number = random.randint(1, 100)
    attempts_left = 10
    feedback_label.config(text="Guess a number between 1 and 100")
    attempts_label.config(text=f"Attempts left: {attempts_left}")
    guess_entry.delete(0, tk.END)
    guess_entry.config(state=tk.NORMAL)
    guess_button.config(state=tk.NORMAL)
    restart_button.config(state=tk.DISABLED)

# Function to check the player's guess
def check_guess():
    global attempts_left
    try:
        guess = int(guess_entry.get())
        if guess < 1 or guess > 100:
            feedback_label.config(text="Please enter a number between 1 and 100")
        elif guess < secret_number:
            attempts_left -= 1
            feedback_label.config(text="Too low!")
        elif guess > secret_number:
            attempts_left -= 1
            feedback_label.config(text="Too high!")
        else:
            feedback_label.config(text="Congratulations! You guessed it!")
            guess_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            restart_button.config(state=tk.NORMAL)
        attempts_label.config(text=f"Attempts left: {attempts_left}")
        if attempts_left <= 0:
            feedback_label.config(text=f"You've run out of attempts! The number was {secret_number}.")
            guess_entry.config(state=tk.DISABLED)
            guess_button.config(state=tk.DISABLED)
            restart_button.config(state=tk.NORMAL)
    except ValueError:
        feedback_label.config(text="Please enter a valid number")
    guess_entry.delete(0, tk.END)

# Create the main window
root = tk.Tk()
root.title("Number Guessing Game")
root.geometry("400x300")
root.configure(bg='#333333')

# Title label
title_label = tk.Label(root, text="Number Guessing Game", font=('Helvetica', 18, 'bold'), bg='#333333', fg='#ffffff')
title_label.pack(pady=10)

# Feedback label
feedback_label = tk.Label(root, text="Guess a number between 1 and 100", font=('Helvetica', 14), bg='#333333', fg='#ffcccc')
feedback_label.pack(pady=10)

# Attempts label
attempts_label = tk.Label(root, text="Attempts left: 10", font=('Helvetica', 14), bg='#333333', fg='#ffcccc')
attempts_label.pack(pady=5)

# Entry for guessing
guess_entry = tk.Entry(root, font=('Helvetica', 14), borderwidth=2, relief='solid')
guess_entry.pack(pady=10)

# Button to submit the guess
guess_button = tk.Button(root, text="Submit Guess", command=check_guess, bg='#ff9999', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised')
guess_button.pack(pady=5)

# Button to restart the game
restart_button = tk.Button(root, text="Restart Game", command=start_game, bg='#66cc66', fg='#ffffff', font=('Helvetica', 14, 'bold'), borderwidth=2, relief='raised', state=tk.DISABLED)
restart_button.pack(pady=5)

# Start the game initially
start_game()

# Run the application
root.mainloop()
