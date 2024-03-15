from contact import Contact
import pickle


def load_contacts():
    try:
        with open("contacts.dat", "rb") as file:
            contacts = pickle.load(file)
    except IOError:
        contacts = []

    return contacts

def add_contact(contacts):
    name = input("Enter name: ")
    phone = input("Enter phone: ")
    
    contact = Contact(name, phone)
    if name not in contacts:
        contacts[name] = contact
    else:
        print("Contact already exists")
    
    return contacts


def save_contacts(contacts):
    with open("contacts.dat", "wb") as file:
        # pickle.dump() serializes the object and writes it to the file
        # dump can pass any object (list, dictionary, etc.)
        pickle.dump(contacts, file)


def main():
    myContact1 = Contact("Batman", "555-555-5555")
    myContact2 = Contact("Joker", "444-444-4444")
    myContact3 = Contact("Penguin", "333-333-3333")

    all_contacts = {
        myContact1.get_name(): myContact1,
        myContact2.get_name(): myContact2,
        myContact3.get_name(): myContact3,
    }
    
    print(all_contacts)
    
    save_contacts(all_contacts)
    contacts = load_contacts()
    
    add_contact(contacts)
    save_contacts(contacts)
    
    for contact in contacts.values():
        print(contact)


if __name__ == "__main__":
    main()
