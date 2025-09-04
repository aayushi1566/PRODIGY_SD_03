# Simple Contact Management System

contacts = {}

def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact '{name}' added successfully!\n")

def view_contacts():
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for name, info in contacts.items():
        print(f"Name: {name}, Phone: {info['Phone']}, Email: {info['Email']}")
    print()

def search_contact():
    name = input("Enter name to search: ")
    if name in contacts:
        print(f"Found: Name: {name}, Phone: {contacts[name]['Phone']}, Email: {contacts[name]['Email']}\n")
    else:
        print("Contact not found.\n")

def update_contact():
    name = input("Enter name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' updated successfully!\n")
    else:
        print("Contact not found.\n")

def delete_contact():
    name = input("Enter name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!
