import json
import os

CONTACTS_FILE = "contacts.json"

def load_contacts():
    if os.path.exists(CONTACTS_FILE):
        with open(CONTACTS_FILE, "r") as f:
            return json.load(f)
    return []

def save_contacts(contacts):
    with open(CONTACTS_FILE, "w") as f:
        json.dump(contacts, f, indent=4)

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")
    address = input("Enter address: ")
    contacts.append({"name": name, "phone": phone, "email": email, "address": address})
    print("✅ Contact added.")

def view_contacts(contacts):
    if not contacts:
        print("No contacts to show.")
        return
    print("\n📇 Contact List:")
    for i, contact in enumerate(contacts, 1):
        print(f"{i}. {contact['name']} – {contact['phone']}")

def search_contacts(contacts):
    query = input("Enter name or phone to search: ").lower()
    found = [c for c in contacts if query in c['name'].lower() or query in c['phone']]
    if found:
        for c in found:
            print(f"\n🔍 Found:\nName: {c['name']}\nPhone: {c['phone']}\nEmail: {c['email']}\nAddress: {c['address']}")
    else:
        print("No matching contact found.")

def update_contact(contacts):
    name = input("Enter the name of the contact to update: ").lower()
    for c in contacts:
        if c['name'].lower() == name:
            c['phone'] = input("New phone number: ")
            c['email'] = input("New email address: ")
            c['address'] = input("New address: ")
            print("🔄 Contact updated.")
            return
    print("❌ Contact not found.")

def delete_contact(contacts):
    name = input("Enter the name of the contact to delete: ").lower()
    for i, c in enumerate(contacts):
        if c['name'].lower() == name:
            del contacts[i]
            print("🗑️ Contact deleted.")
            return
    print("❌ Contact not found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n📌 CONTACT MANAGER MENU")
        print("1. Add Contact\n2. View Contacts\n3. Search Contact\n4. Update Contact\n5. Delete Contact\n6. Exit")
        choice = input("Choose an option: ")

        if choice == "1":
            add_contact(contacts)
        elif choice == "2":
            view_contacts(contacts)
        elif choice == "3":
            search_contacts(contacts)
        elif choice == "4":
            update_contact(contacts)
        elif choice == "5":
            delete_contact(contacts)
        elif choice == "6":
            save_contacts(contacts)
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Try again.")

if __name__ == "__main__":
    main()