contacts = []

def add_contact(name, phone, email):
    contacts.append({"name": name, "phone": phone, "email": email})

def remove_contact(name):
    global contacts  # Needed to modify the list
    contacts = [contact for contact in contacts if contact["name"] != name]

def search_contact(name):
    for contact in contacts:
        if contact["name"] == name:
            print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")
            return
    print("Contact not found.")

# Sort contacts by name
def sort_contacts():
    global contacts
    contacts = sorted(contacts, key=lambda x: x["name"])

# Filter contacts by email domain
def filter_contacts(domain):
    filtered = [contact for contact in contacts if domain in contact["email"]]
    for contact in filtered:
        print(f"Name: {contact['name']}, Phone: {contact['phone']}, Email: {contact['email']}")

def main():
    while True:
        action = input("Choose an action - Add (A), Remove (R), Search (S), Sort (O), Filter (F), Quit (Q): ").upper()
        if action == "Q":
            break
        elif action == "A":
            name = input("Enter name: ")
            phone = input("Enter phone: ")
            email = input("Enter email: ")
            add_contact(name, phone, email)
        elif action == "R":
            name = input("Enter name to remove: ")
            remove_contact(name)
        elif action == "S":
            name = input("Enter name to search: ")
            search_contact(name)
        elif action == "O":
            sort_contacts()
        elif action == "F":
            domain = input("Enter email domain to filter: ")
            filter_contacts(domain)

if __name__ == "__main__":
    main()
