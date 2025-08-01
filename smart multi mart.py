import tkinter as tk
from tkinter import ttk, messagebox
import qrcode
from PIL import Image, ImageTk
import io

# Sample data for six shops, each with 14 items
shops = {
    "Zudio": [
        {"product": "Shirt", "price": 250},
        {"product": "Pants", "price": 350},
        {"product": "T-shirt", "price": 300},
        {"product": "Jeans", "price": 800},
        {"product": "Sweater", "price": 600},
        {"product": "Jacket", "price": 1200},
        {"product": "Shorts", "price": 450},
        {"product": "Belt", "price": 150},
        {"product": "Cap", "price": 200},
        {"product": "Scarf", "price": 100},
        {"product": "Shoes", "price": 900},
        {"product": "Socks", "price": 50},
        {"product": "Gloves", "price": 80},
        {"product": "Sunglasses", "price": 500}
    ],
    "Reliance Digital": [
        {"product": "Mobile Phone", "price": 15000},
        {"product": "Laptop", "price": 50000},
        {"product": "Headphones", "price": 2000},
        {"product": "Smartwatch", "price": 7000},
        {"product": "Camera", "price": 30000},
        {"product": "Speakers", "price": 3500},
        {"product": "Router", "price": 1500},
        {"product": "Tablet", "price": 25000},
        {"product": "TV", "price": 40000},
        {"product": "Printer", "price": 8000},
        {"product": "Keyboard", "price": 1000},
        {"product": "Mouse", "price": 500},
        {"product": "Charger", "price": 1500},
        {"product": "USB Cable", "price": 300}
    ],
    "Food Court": [
        {"product": "Pizza", "price": 400},
        {"product": "Cola", "price": 50},
        {"product": "Pasta", "price": 350},
        {"product": "Ice Cream", "price": 150},
        {"product": "Sandwich", "price": 200},
        {"product": "Salad", "price": 250},
        {"product": "Coffee", "price": 100},
        {"product": "Burger", "price": 300},
        {"product": "Fries", "price": 100},
        {"product": "Donut", "price": 80},
        {"product": "Juice", "price": 60},
        {"product": "Sushi", "price": 500},
        {"product": "Noodles", "price": 400},
        {"product": "Wrap", "price": 150}
    ],
    "H&M": [
        {"product": "Shirt", "price": 300},
        {"product": "Trousers", "price": 600},
        {"product": "Dress", "price": 900},
        {"product": "Skirt", "price": 500},
        {"product": "Shoes", "price": 1200},
        {"product": "Hat", "price": 200},
        {"product": "Scarf", "price": 150},
        {"product": "Gloves", "price": 250},
        {"product": "Coat", "price": 1800},
        {"product": "Jacket", "price": 1500},
        {"product": "Socks", "price": 100},
        {"product": "Tie", "price": 80},
        {"product": "Belt", "price": 100},
        {"product": "Backpack", "price": 700}
    ],
    "Decathlon": [
        {"product": "Sports Shoes", "price": 1200},
        {"product": "Basketball", "price": 500},
        {"product": "Tennis Racket", "price": 1500},
        {"product": "Yoga Mat", "price": 800},
        {"product": "Cycling Helmet", "price": 900},
        {"product": "Running Shorts", "price": 350},
        {"product": "Soccer Ball", "price": 600},
        {"product": "Gym Gloves", "price": 300},
        {"product": "Jersey", "price": 400},
        {"product": "Kettlebell", "price": 900},
        {"product": "Fitness Band", "price": 800},
        {"product": "Swimming Goggles", "price": 250},
        {"product": "Hiking Boots", "price": 1700},
        {"product": "Backpack", "price": 1000}
    ],
    "Nike": [
        {"product": "Running Shoes", "price": 4000},
        {"product": "Training Pants", "price": 1500},
        {"product": "Sweatshirt", "price": 1200},
        {"product": "Cap", "price": 300},
        {"product": "Socks", "price": 200},
        {"product": "Sports Bra", "price": 800},
        {"product": "Tennis Skirt", "price": 700},
        {"product": "Joggers", "price": 1300},
        {"product": "Football Shoes", "price": 2500},
        {"product": "Wristbands", "price": 150},
        {"product": "Ankle Socks", "price": 100},
        {"product": "Headband", "price": 80},
        {"product": "Tracksuit", "price": 1800},
        {"product": "Duffel Bag", "price": 2500}
    ]
}

# To store user-inputted quantities
quantity_vars = {}
selected_shops = []

# Function to display selected shop's products
def display_shop_products(shop_name, var):
    if var.get():  # If the checkbox is ticked
        if shop_name not in selected_shops:
            selected_shops.append(shop_name)
    else:  # If the checkbox is unticked
        if shop_name in selected_shops:
            selected_shops.remove(shop_name)

    # Clear product_frame and dynamically show selected shops
    for widget in product_frame.winfo_children():
        widget.destroy()
    
    # Display products for all selected shops
    for i, shop in enumerate(selected_shops):
        shop_container = tk.Frame(product_frame, bg="lightgray", bd=2, relief="solid", padx=10, pady=10)
        shop_container.grid(row=0, column=i, padx=10, pady=10, sticky="nsew")
        
        tk.Label(shop_container, text=f"Products in {shop}", font=("Arial", 12, "bold")).grid(row=0, column=0, columnspan=3)
        
        # Header Row
        tk.Label(shop_container, text="Product", font=("Arial", 10, "bold")).grid(row=1, column=0, padx=5, pady=5)
        tk.Label(shop_container, text="Quantity", font=("Arial", 10, "bold")).grid(row=1, column=1, padx=5, pady=5)
        tk.Label(shop_container, text="Price", font=("Arial", 10, "bold")).grid(row=1, column=2, padx=5, pady=5)
        
        for idx, item in enumerate(shops[shop], start=2):
            product_label = tk.Label(shop_container, text=f"{item['product']}", font=("Arial", 10))
            product_label.grid(row=idx, column=0, padx=5, pady=5)
            
            quantity_var = tk.IntVar(value=0)
            quantity_entry = tk.Entry(shop_container, textvariable=quantity_var, width=5)
            quantity_entry.grid(row=idx, column=1, padx=5, pady=5)
            
            price_label = tk.Label(shop_container, text=f"Rs. {item['price']}", font=("Arial", 10))
            price_label.grid(row=idx, column=2, padx=5, pady=5)
            
            # Store the quantity variable for each shop's product
            quantity_vars[(shop, item['product'])] = quantity_var

# Function to simulate sending notifications to shops
def send_notifications(bill_details):
    for shop, items in bill_details.items():
        total_amount = sum(int(item.split("=")[1].strip().split(" ")[-1]) for item in items)
        messagebox.showinfo(f"Notification for {shop}", f"The amount of Rs. {total_amount} has been credited to {shop}.")

# Function to generate QR code for the bill amount
def generate_qr_code(amount):
    qr = qrcode.make(f"Pay Rs. {amount}")
    buf = io.BytesIO()
    qr.save(buf)
    buf.seek(0)
    return Image.open(buf)

# Function to generate bill
def generate_bill():
    total_amount = 0
    bill_details = {}

    for shop in selected_shops:
        items = []
        for item in shops[shop]:
            quantity = quantity_vars[(shop, item['product'])].get()
            if quantity > 0:
                item_total = quantity * item['price']
                total_amount += item_total
                items.append(f"{item['product']} = {quantity} x Rs. {item['price']} = Rs. {item_total}")

        if items:
            bill_details[shop] = items  # Only include shops with purchased items

    if not bill_details:  # If no items were selected, show an error
        messagebox.showerror("Error", "No items selected for billing.")
        return

    bill_window = tk.Toplevel(root)
    bill_window.title("Bill Summary")
    bill_window.geometry("400x500")
    
    # Display bill content in the center
    bill_frame = tk.Frame(bill_window)
    bill_frame.pack(pady=20)

    tk.Label(bill_frame, text="Bill Summary", font=("Arial", 14, "bold")).pack(pady=10)

    for shop, items in bill_details.items():
        tk.Label(bill_frame, text=f"--- {shop} ---", font=("Arial", 12, "bold")).pack()
        for item in items:
            tk.Label(bill_frame, text=item).pack()
    
    tk.Label(bill_frame, text=f"\nTotal Amount: Rs. {total_amount}", font=("Arial", 12, "bold")).pack()

    # Generate and display QR code
    qr_code_image = generate_qr_code(total_amount)
    qr_code_image = qr_code_image.resize((150, 150))  # Resize QR code
    qr_code_photo = ImageTk.PhotoImage(qr_code_image)
    qr_code_label = tk.Label(bill_frame, image=qr_code_photo)
    qr_code_label.image = qr_code_photo  # Keep a reference to avoid garbage collection
    qr_code_label.pack(pady=10)

    # Button to confirm payment
    payment_button = tk.Button(bill_frame, text="Pay Bill", command=lambda: [send_notifications(bill_details), bill_window.destroy()])
    payment_button.pack(pady=10)

# Main window setup
root = tk.Tk()
root.title("Smart MultiMart Billing System")
root.geometry("800x600")

# Title label for Smart MultiMart
tk.Label(root, text="Smart MultiMart", font=("Arial", 16, "bold")).pack(pady=10)

# Checkbox frame for shops
checkbox_frame = tk.Frame(root)
checkbox_frame.pack(pady=20)

for shop in shops.keys():
    var = tk.IntVar()
    checkbox = tk.Checkbutton(checkbox_frame, text=shop, variable=var, command=lambda s=shop, v=var: display_shop_products(s, v))
    checkbox.pack(side='left', padx=10)

# Frame to display products
product_frame = tk.Frame(root)
product_frame.pack(pady=10)

# Button to generate bill
generate_bill_button = tk.Button(root, text="Generate Bill", command=generate_bill)
generate_bill_button.pack(pady=20)

root.mainloop()
