phonebook = {}


def addContact(name, phoneNumber):
    phonebook[name] = phoneNumber


def findContact(name):
    if name in phonebook:
        print(name, ":", phonebook[name])
    else:
        print("Contact not found.")


def deleteContact(name):
    if name in phonebook:
        del phonebook[name]
        print("Contact deleted.")
    else:
        print("Contact not found.")


while True:
    print("1. Add contact")
    print("2. Find contact")
    print("3. Delete contact")
    print("4. Exit")

    try:
        choice = int(input("Enter your choice: "))

        if choice == 1:
            name = input("Enter name: ")
            phoneNumber = input("Enter phone number: ")
            addContact(name, phoneNumber)
        elif choice == 2:
            name = input("Enter name: ")
            findContact(name)
        elif choice == 3:
            name = input("Enter name: ")
            deleteContact(name)
        elif choice == 4:
            break
        else:
            print("Invalid choice.")
    except:
        print(" check options")
