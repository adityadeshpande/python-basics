class ContactBook:
    def __init__(self):
        self.contacts = {}

    def add_contact(self, name, phone, email):
        self.contacts[name] = {"Phone": phone, "Email": email}
        print(f"Contact '{name}' added successfully.")

    def view_contacts(self):
        if not self.contacts:
            print("No contacts found.")
        else:
            print("\nContact List:")
            for name, details in self.contacts.items():
                print(f"{name} - Phone: {details['Phone']}, Email: {details['Email']}")

    def search_contact(self, name):
        if name in self.contacts:
            print(f"\n{name} - Phone: {self.contacts[name]['Phone']}, Email: {self.contacts[name]['Email']}")
        else:
            print("Contact not found.")

    def delete_contact(self, name):
        if name in self.contacts:
            del self.contacts[name]
            print(f"Contact '{name}' deleted.")
        else:
            print("Contact not found.")

if __name__ == "__main__":
    book = ContactBook()

    while True:
        print("\nOptions: 1) Add Contact  2) View Contacts  3) Search  4) Delete  5) Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            book.add_contact(name, phone, email)
        elif choice == "2":
            book.view_contacts()
        elif choice == "3":
            name = input("Enter name to search: ")
            book.search_contact(name)
        elif choice == "4":
            name = input("Enter name to delete: ")
            book.delete_contact(name)
        elif choice == "5":
            print("Exiting Contact Book...")
            break
        else:
            print("Invalid choice. Try again.")
