# Initialize an empty contact dictionary
contacts = {}

# Function to add a new contact
def add_contact():
    name = input("Enter contact name: ")
    phone = input("Enter contact phone number: ")
    email = input("Enter contact email: ")
    contacts[name] = {"Phone": phone, "Email": email}
    print(f"Contact {name} added successfully!")

# Function to view all contacts
def view_contacts():
    if contacts:
        print("Contacts:")
        for name, info in contacts.items():
            print(f"Name: {name}")
            print(f"Phone: {info['Phone']}")
            print(f"Email: {info['Email']}")
            print("-------------------")
    else:
        print("No contacts found.")

# Function to search for a contact
def search_contact():
    name = input("Enter contact name to search: ")
    if name in contacts:
        info = contacts[name]
        print(f"Name: {name}")
        print(f"Phone: {info['Phone']}")
        print(f"Email: {info['Email']}")
    else:
        print(f"Contact {name} not found.")

# Function to update a contact
def update_contact():
    name = input("Enter contact name to update: ")
    if name in contacts:
        phone = input("Enter new phone number: ")
        email = input("Enter new email: ")
        contacts[name]["Phone"] = phone
        contacts[name]["Email"] = email
        print(f"Contact {name} updated successfully!")
    else:
        print(f"Contact {name} not found.")

# Function to delete a contact
def delete_contact():
    name = input("Enter contact name to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact {name} deleted successfully!")
    else:
        print(f"Contact {name} not found.")

# User interface
while True:
    print("\nContact Book Menu:")
    print("1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    
    choice = input("Enter your choice (1/2/3/4/5/6): ")
    
    if choice == '1':
        add_contact()
    elif choice == '2':
        view_contacts()
    elif choice == '3':
        search_contact()
    elif choice == '4':
        update_contact()
    elif choice == '5':
        delete_contact()
    elif choice == '6':
        break
    else:
        print("Invalid choice. Please try again.")
