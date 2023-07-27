import tkinter as tk

# Create the main window
window = tk.Tk()
window.title("Restaurant Management System")

# Set the window size
window.geometry("600x700")
window.resizable(False,False)

# Add widgets and functionality here
# Create a list to store menu items
menu_items = []

# Function to add menu items
def add_menu_item():
    item = item_entry.get()
    price = price_entry.get()
    menu_items.append((item, price))
    item_entry.delete(0, tk.END)
    price_entry.delete(0, tk.END)

# Create label and entry for item
item_label = tk.Label(window, text="Item:")
item_label.pack()
item_entry = tk.Entry(window)
item_entry.pack()

# Create label and entry for price
price_label = tk.Label(window, text="Price:")
price_label.pack()
price_entry = tk.Entry(window)
price_entry.pack()

# Create button to add menu item
add_button = tk.Button(window, text="Add Item", command=add_menu_item)
add_button.pack()

# Create a label to display menu items
menu_label = tk.Label(window, text="Menu Items")
menu_label.pack()

# Create a text widget to display menu items
menu_text = tk.Text(window, height=10, width=40)
menu_text.pack()

# Function to update the menu display
def update_menu_display():
    menu_text.delete(1.0, tk.END)  # Clear the text widget
    for item, price in menu_items:
        menu_text.insert(tk.END, f"{item}: ${price}\n")

# Create a button to update the menu display
update_button = tk.Button(window, text="Update Menu", command=update_menu_display)
update_button.pack()

# Create a list to store the orders
orders = []

# Function to place an order
def place_order():
    item = order_item_entry.get()
    quantity = int(order_quantity_entry.get())
    for menu_item, price in menu_items:
        if menu_item == item:
            orders.append((item, price, quantity))
            break
    order_item_entry.delete(0, tk.END)
    order_quantity_entry.delete(0, tk.END)

# Create label and entry for order item
order_item_label = tk.Label(window, text="Item:")
order_item_label.pack()
order_item_entry = tk.Entry(window)
order_item_entry.pack()

# Create label and entry for order quantity
order_quantity_label = tk.Label(window, text="Quantity:")
order_quantity_label.pack()
order_quantity_entry = tk.Entry(window)
order_quantity_entry.pack()

# Create button to place an order
order_button = tk.Button(window, text="Place Order", command=place_order)
order_button.pack()

# Create a label to display the total bill
total_label = tk.Label(window, text="Total Bill: $0.00")
total_label.pack()

# Function to update the total bill
def update_total_bill():
    total = 0
    for item, price, quantity in orders:
        total += float(price) * quantity
    total_label.config(text=f"Total Bill: ${total:.2f}")

# Create a button to update the total bill
calculate_button = tk.Button(window, text="Calculate Bill", command=update_total_bill)
calculate_button.pack()



# Start the main event loop
window.mainloop()
