contacts = []

def add_contact():
    name = input("Enter contact name: ").strip()
    phone = input("Enter phone number: ").strip()
    contact = {"name": name, "phone": phone}
    contacts.append(contact)
    print("Contact added successfully.")

def view_contacts():
    if not contacts:
        print("No contacts to display.")
    else:
        for i, contact in enumerate(contacts, start=1):
            print(f"{i}. Name: {contact['name']}, Phone: {contact['phone']}")

def search_contact():
    query = input("Enter name to search: ").strip().lower()
    found = False
    for contact in contacts:
        if contact['name'].lower() == query:
            print(f"Found - Name: {contact['name']}, Phone: {contact['phone']}")
            found = True
    if not found:
        print("Contact not found.")

def delete_contact():
    query = input("Enter name to delete: ").strip().lower()
    for i, contact in enumerate(contacts):
        if contact['name'].lower() == query:
            del contacts[i]
            print("Contact deleted successfully.")
            return
    print("Contact not found.")

def main():
    while True:
        print("\nContact Book Menu")
        print("1. Add Contact")
        print("2. View All Contacts")
        print("3. Search Contact by Name")
        print("4. Delete Contact")
        print("5. Exit")
        choice = input("Choose an option (1-5): ")
        
        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("Exiting Contact Book. Goodbye!")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
