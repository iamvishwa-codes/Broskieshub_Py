import json
import os

# File to store contacts
CONTACT_FILE = "contacts.json"

# Load existing contacts (if any)
def load_contacts():
    if os.path.exists(CONTACT_FILE):
        with open(CONTACT_FILE, "r") as file:
            return json.load(file)
    return []

# Save contacts to file
def save_contacts(contacts):
    with open(CONTACT_FILE, "w") as file:
        json.dump(contacts, file, indent=4)

# Add a new contact
def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email: ")
    contact = {"name": name, "phone": phone, "email": email}
    contacts.append(contact)
    save_contacts(contacts)
    print(f"✅ Contact '{name}' added successfully!\n")

# View all contacts
def view_contacts(contacts):
    if not contacts:
        print("No contacts found.\n")
        return
    print("\n--- Contact List ---")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} - {contact['phone']} - {contact['email']}")
    print()

# Search contact by name
def search_contact(contacts):
    search_name = input("Enter name to search: ").lower()
    found = [c for c in contacts if search_name in c["name"].lower()]
    if found:
        print("\n--- Search Results ---")
        for c in found:
            print(f"{c['name']} - {c['phone']} - {c['email']}")
    else:
        print("No contact found with that name.\n")
    print()

# Delete contact by name
def delete_contact(contacts):
    del_name = input("Enter name to delete: ").lower()
    new_contacts = [c for c in contacts if c["name"].lower() != del_name]
    if len(new_contacts) < len(contacts):
        save_contacts(new_contacts)
        print(f"🗑️ Contact '{del_name}' deleted successfully!\n")
    else:
        print("No contact found with that name.\n")
    return new_contacts

# Main menu
def main():
    contacts = load_contacts()
    while True:
        print("📒 CONTACT BOOK")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contact(contacts)
        elif choice == "4":
            contacts = delete_contact(contacts)
        elif choice == "5":
            print("Goodbye! 👋")
            break
        else:
            print("Invalid choice! Try again.\n")

# Run the program
if __name__ == "__main__":
    main()
