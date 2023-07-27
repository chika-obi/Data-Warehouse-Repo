
import tkinter as tk

def on_button_click(button_text):
    # Handle button clicks here
    entry.insert(tk.END, button_text)

def clear_entry():
    entry.delete(0, tk.END)

def calculate_result():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        entry.delete(0, tk.END)
        entry.insert(tk.END, "Error")

# Create the main application window
root = tk.Tk()
root.title("Calculator")

# Create the entry widget for displaying the input and output
entry = tk.Entry(root, width=20, font=("Arial", 20), bd=5)
entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

# Define the button labels
button_labels = [
    ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("chr(247)", 1, 3),
    ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
    ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
    ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
    ("C", 5, 0), ("(", 5, 1), (")", 5, 2)
]

# Create the buttons with padding
for button_text, row, col in button_labels:
    button = tk.Button(root, text=button_text, font=("Arial", 15), width=5, height=2,
                       command=lambda text=button_text: on_button_click(text))
    button.grid(row=row, column=col, padx=10, pady=10)

# Create the "Clear" button separately for a wider column span
clear_button = tk.Button(root, text="Clear", font=("Arial", 15), width=20, height=2, command=clear_entry)
clear_button.grid(row=6, column=0, columnspan=4, padx=10, pady=10)

# Create the "=" button separately for a wider column span
equals_button = tk.Button(root, text="=", font=("Arial", 15), width=20, height=2, command=calculate_result)
equals_button.grid(row=7, column=0, columnspan=4, padx=10, pady=10)

root.mainloop()

