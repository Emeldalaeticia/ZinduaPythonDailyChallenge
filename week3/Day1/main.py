
import csv
class InventoryItem:
    def __init__(self, name, quantity, price):
        self.name = name
        self.quantity = quantity
        self.price = price

    # def __repr__(self):
    #     return (f"{self.name} ({self.quantity}) - ${self.price:.2f}")

class InventoryManagementSystem:
    def __init__(self):
        self.items = []

    def add_item(self, name, quantity, price):
        item = InventoryItem(name, quantity, price)
        self.items.append(item)
        print(self.items)

    def remove_item(self, name):
        for item in self.items:
            if item.name == name:
                self.items.remove(item)
                return True
        return False
    
    def update_item(self, name, quantity=None, price=None):
        for item in self.items:
            if item.name == name:
                if quantity is not None:
                    item.quantity = int(quantity)
                if price is not None:
                    item.price = float(price)
                return True
        return False
    
    def display_inventory(self):
        for item in self.items:
            print(item)

    def load_inventory(self, filename):
        with open(filename, 'r') as csvfile:
            reader = csv.reader(csvfile)
            for row in reader:
                name, quantity, price = row
                quantity = (quantity)
                price = (price)
                self.add_item(name, quantity, price)

    def save_inventory(self, filename):
        with open(filename, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            for item in self.items:
                writer.writerow([item.name, item.quantity, item.price])
                
def main():
    # Create a new instance of the InventoryManagementSystem class
    ims = InventoryManagementSystem()
    # Load the inventory from a CSV file
    ims.load_inventory('inventory.csv')
    # Display a menu and allow the user to interact with the inventory system
    while True:
        print("Menu:")
        print("1. Add item")
        print("2. Remove item")
        print("3. Update item")
        print("4. Display inventory")
        print("5. Save inventory")
        print("6. Exit")
        choice = input("Enter your choice: ")
        if choice == "1":
            name = input("Enter item name: ")
            quantity = int(input("Enter quantity: "))
            price = float(input("Enter price: "))
            ims.add_item(name, quantity, price)
            print("Item added to inventory.")
        elif choice == "2":
            name = input("Enter item name: ")
            if ims.remove_item(name):
                print("Item removed from inventory.")
            else:
                print("Item not found in inventory.")
        elif choice == "3":
            name = input("Enter item name: ")
            quantity = input("Enter new quantity : ")
            price = input("Enter new price : ")
            if quantity == "" and price == "":
                print("No changes made.")
            else:
                if quantity == "":
                    quantity = None
                else:
                    quantity = int(quantity)
                if price == "":
                    price = None
                else:
                    price = float(price)
                if ims.update_item(name, quantity, price):
                    print("Item updated in inventory.")
                else:
                    print("Item not found in inventory.")
        elif choice == "4":
            ims.display_inventory()
        elif choice == "5":
            ims.save_inventory('inventory.csv')
            print("Inventory saved to file.")
        elif choice == "6":
            break
        else:
            print("Invalid choice. Try again.")
        print()



main()









