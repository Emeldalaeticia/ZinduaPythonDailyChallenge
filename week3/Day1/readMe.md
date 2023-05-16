Inventory Management System

This code implements an inventory management system using the InventoryManagementSystem class and the InventoryItem class. It allows users to add, remove, update, display, and save items in the inventory.

The InventoryItem class represents an item in the inventory and has attributes such as name, quantity, and price. It is currently commented out.

The InventoryManagementSystem class manages the overall inventory. It has a list of items and provides methods to add, remove, update, display, load, and save items.

The add_item method creates a new InventoryItem object and adds it to the items list.

The remove_item method iterates over the items list and removes the item with the matching name, returning True if successful, and False if the item is not found.

The update_item method finds the item with the matching name and updates its quantity and/or price if the corresponding arguments are provided. It returns True if successful and False if the item is not found.

The display_inventory method iterates over the items list and prints each item.

The load_inventory method reads item information from a CSV file and adds the items to the inventory using the add_item method.

The save_inventory method writes the item information from the items list to a CSV file.

The main function creates an instance of the InventoryManagementSystem class, loads the inventory from a CSV file, and presents a menu to interact with the inventory system.

In the menu loop, users can choose options to add an item, remove an item, update an item, display the inventory, save the inventory to a file, or exit the program.

User input is collected and processed accordingly, utilizing the respective methods of the InventoryManagementSystem class.

This code provides a basic inventory management system, allowing users to perform various operations on the inventory and save/load data from a CSV file