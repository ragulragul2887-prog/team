import json
import os

# File to store grocery data
FILE_NAME = "grocery_store.json"

# Load items from file
def load_items():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as f:
        return json.load(f)

# Save items to file
def save_items(items):
    with open(FILE_NAME, "w") as f:
        json.dump(items, f, indent=4)

# Add new item
def add_item(items):
    code = input("Enter item code: ")
    if code in items:
        print("Item already exists!")
        return
    name = input("Enter item name: ")
    price = float(input("Enter item price: "))
    stock = int(input("Enter stock quantity: "))
    items[code] = {"name": name, "price": price, "stock": stock}
    add_item(items)
    print("✅ Item added successfully!")

# View all items
def view_items(items):
    if not items:
        print("No items available.")
        return
    print("\n--- Grocery Store Items ---")
    for code, details in items.items():
        print(f"Code: {code}, Name: {details['name']}, Price: {details['price']}, Stock: {details['stock']}")

# Update item
def update_item(items):
    code = input("Enter item code to update: ")
    if code not in items:
        print("❌ Item not found.")
        return
    print("Leave blank if no change.")
    name = input(f"Enter new name ({items[code]['name']}): ") or items[code]['name']
    price = input(f"Enter new price ({items[code]['price']}): ")
    stock = input(f"Enter new stock ({items[code]['stock']}): ")

    items[code]['name'] = name
    if price: 
        items[code]['price'] = float(price)
    if stock: 
        items[code]['stock'] = int(stock)

    save_items(items)
    print("✅ Item updated successfully!")

# Delete item
def delete_item(items):
    code = input("Enter item code to delete: ")
    if code not in items:
        print("❌ Item not found.")
        return
    del items[code]
    save_items(items)
    print("🗑️ Item deleted successfully!")

# Billing system
def billing(items):
    cart = []
    total = 0
    while True:
        code = input("Enter item code to buy (or 'done' to finish): ")
        if code.lower() == "done":
            break
        if code not in items:
            print("❌ Item not found.")
            continue
        quantity = int(input("Enter quantity: "))
        if quantity > items[code]['stock']:
            print("❌ Not enough stock.")
            continue
        cost = items[code]['price'] * quantity
        cart.append((items[code]['name'], quantity, items[code]['price'], cost))
        total += cost
        items[code]['stock'] -= quantity

    save_items(items)
    print("\n--- Bill ---")
    for name, qty, price, cost in cart:
        print(f"{name} x {qty} @ {price} = {cost}")
    print(f"Total: {total}")
    print("✅ Purchase successful!")

# Main Menu
def main():
    items = load_items()
    while True:
        print("\n--- Grocery Store Management ---")
        print("1. Add Item")
        print("2. View Items")
        print("3. Update Item")
        print("4. Delete Item")
        print("5. Billing System")
        print("6. Exit")
        choice = input("Enter choice: ")
        if choice == "1":
            add_item(items)
        elif choice == "2":
            view_items(items)
        elif choice == "3":
            update_item(items)
        elif choice == "4":
            delete_item(items)
        elif choice == "5":
            billing(items)
        elif choice == "6":
            print("👋 Exiting... Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()
