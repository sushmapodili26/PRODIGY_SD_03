import csv
import os

DATA_FILE = "contacts.csv"
FIELDNAMES = ["name", "phone", "email"]

def load_contacts():
    contacts = []
    if not os.path.exists(DATA_FILE):
        return contacts
    with open(DATA_FILE, newline="", encoding="utf-8") as f:
        reader = csv.DictReader(f, fieldnames=FIELDNAMES)
        for row in reader:
            if any(row.values()):
                contacts.append({k: (v or "").strip() for k, v in row.items()})
    return contacts

def save_contacts(contacts):
    with open(DATA_FILE, "w", newline="", encoding="utf-8") as f:
        writer = csv.DictWriter(f, fieldnames=FIELDNAMES)
        for c in contacts:
            writer.writerow(c)

def show_contacts(contacts):
    if not contacts:
        print("\nNo contacts found.")
        return
    print("\n--- Contacts ---")
    for i, c in enumerate(contacts, start=1):
        print(f"{i}) {c['name']} | {c['phone']} | {c['email']}")

def add_contact(contacts):
    print("\n--- Add Contact ---")
    name = input("Name: ").strip()
    phone = input("Phone: ").strip()
    email = input("Email: ").strip()
    if not name or not phone:
        print("Name and phone cannot be empty!")
        return
    contacts.append({"name": name, "phone": phone, "email": email})
    save_contacts(contacts)
    print("✅ Contact added.")

def edit_contact(contacts):
    show_contacts(contacts)
    if not contacts: return
    idx = int(input("Enter number to edit: ")) - 1
    if 0 <= idx < len(contacts):
        c = contacts[idx]
        name = input(f"New name [{c['name']}]: ").strip() or c['name']
        phone = input(f"New phone [{c['phone']}]: ").strip() or c['phone']
        email = input(f"New email [{c['email']}]: ").strip() or c['email']
        contacts[idx] = {"name": name, "phone": phone, "email": email}
        save_contacts(contacts)
        print("✅ Contact updated.")

def delete_contact(contacts):
    show_contacts(contacts)
    if not contacts: return
    idx = int(input("Enter number to delete: ")) - 1
    if 0 <= idx < len(contacts):
        removed = contacts.pop(idx)
        save_contacts(contacts)
        print(f"🗑️ Deleted contact: {removed['name']}")

def search_contacts(contacts):
    q = input("\nSearch query: ").lower()
    results = [c for c in contacts if q in c['name'].lower() or q in c['phone'] or q in c['email'].lower()]
    if results:
        print("\n--- Search Results ---")
        for i, c in enumerate(results, start=1):
            print(f"{i}) {c['name']} | {c['phone']} | {c['email']}")
    else:
        print("No matches found.")

def main():
    contacts = load_contacts()
    while True:
        print("\n=== Contact Manager ===")
        print("1. View Contacts\n2. Add Contact\n3. Edit Contact\n4. Delete Contact\n5. Search\n6. Exit")
        choice = input("Choose (1-6): ").strip()
        if choice == "1": show_contacts(contacts)
        elif choice == "2": add_contact(contacts)
        elif choice == "3": edit_contact(contacts)
        elif choice == "4": delete_contact(contacts)
        elif choice == "5": search_contacts(contacts)
        elif choice == "6":
            print("Exiting... Contacts saved.")
            save_contacts(contacts)
            break
        else:
            print("Invalid option.")

if __name__ == "__main__":
    main()
