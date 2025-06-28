import tkinter as tk
from tkinter import messagebox
import random

class NumberGuessingGame:
    def __init__(self, master):
        self.master = master
        master.title("Number Guessing Game")

        self.secret_number = random.randint(1, 100)
        self.attempts = 0

        self.label = tk.Label(master, text="Guess a number between 1 and 100:")
        self.label.pack(pady=10)

        self.entry = tk.Entry(master)
        self.entry.pack(pady=5)

        self.guess_button = tk.Button(master, text="Guess", command=self.check_guess)
        self.guess_button.pack(pady=5)

        self.feedback_label = tk.Label(master, text="")
        self.feedback_label.pack(pady=10)

    def check_guess(self):
        try:
            guess = int(self.entry.get())
            self.attempts += 1

            if guess < self.secret_number:
                self.feedback_label.config(text="Too low! Try again.")
            elif guess > self.secret_number:
                self.feedback_label.config(text="Too high! Try again.")
            else:
                messagebox.showinfo("Correct!", f"Congratulations! You guessed it in {self.attempts} attempts.")
                self.reset_game()
        except ValueError:
            self.feedback_label.config(text="Please enter a valid number.")

    def reset_game(self):
        self.secret_number = random.randint(1, 100)
        self.attempts = 0
        self.entry.delete(0, tk.END)
        self.feedback_label.config(text="Guess a number between 1 and 100:")

# Run the game
if __name__ == "__main__":
    root = tk.Tk()
    game = NumberGuessingGame(root)
    root.mainloop()