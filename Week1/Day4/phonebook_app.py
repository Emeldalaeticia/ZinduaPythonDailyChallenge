phonebook = {}

def add_contact(phonebook):
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    if name in phonebook:
        print("Contact already exists.")
    else:
        phonebook[name] = phone
        print("Contact added successfully.")


def delete_contact(phonebook):
    name = input("Enter contact name: ")
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted successfully.")
    else:
        print("Contact not found.")


def search_contact(phonebook):
    name = input("Enter contact name: ")
    if name in phonebook:
        print(f"{name}: {phonebook[name]}")
    else:
        print("Contact not found.")


def print_contacts(phonebook):
    if phonebook:
        print("Contacts:")
        for name, phone in phonebook.items():
            print(f"{name}: {phone}")
    else:
        print("No contacts found.")


while True:
    print("\nPhonebook App")
    print("1. Add a contact")
    print("2. Delete a contact")
    print("3. Search for a contact")
    print("4. Print all contacts")
    print("5. Exit")
    
    choice = input("Enter your choice (1-5): ")
    if choice == "1":
        add_contact(phonebook)
    elif choice == "2":
        delete_contact(phonebook)
    elif choice == "3":
        search_contact(phonebook)
    elif choice == "4":
        print_contacts(phonebook)
    elif choice == "5":
        break
    else:
        print("Invalid choice. Please try again.")