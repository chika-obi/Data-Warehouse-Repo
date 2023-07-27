import tkinter as tk
from tkinter import ttk

def on_selection(event):
    # Print the selected value from the combobox
    selected_value = event.widget.get()
    print(selected_value)

# Create the main application window
root = tk.Tk()
root.title("Four Comboboxes")

# Create and configure the comboboxes
combo_box1 = ttk.Combobox(root, values=["Option 1", "Option 2", "Option 3"])
combo_box2 = ttk.Combobox(root, values=["Item A", "Item B", "Item C"])
combo_box3 = ttk.Combobox(root, values=["Choice X", "Choice Y", "Choice Z"])
combo_box4 = ttk.Combobox(root, values=["Apple", "Banana", "Orange"])

# Add a label for each combobox
label1 = tk.Label(root, text="Select Option:")
label2 = tk.Label(root, text="Select Item:")
label3 = tk.Label(root, text="Select Choice:")
label4 = tk.Label(root, text="Select Fruit:")

# Bind the on_selection function to the comboboxes
combo_box1.bind("<<ComboboxSelected>>", on_selection)
combo_box2.bind("<<ComboboxSelected>>", on_selection)
combo_box3.bind("<<ComboboxSelected>>", on_selection)
combo_box4.bind("<<ComboboxSelected>>", on_selection)

# Pack the comboboxes and labels into the window
label1.pack()
combo_box1.pack()
label2.pack()
combo_box2.pack()
label3.pack()
combo_box3.pack()
label4.pack()
combo_box4.pack()

# Start the main event loop
root.mainloop()
