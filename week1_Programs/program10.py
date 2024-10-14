def write_to_file(filename, text):
    with open(filename, 'w') as file:
        file.write(text)


def read_file(filename):
    with open(filename, 'r') as file:
        text = file.read()
        words = text.split()
        return len(words)


while True:
    print("1. write")
    print("2. read")
    print("3. Exit")
    choice = input("Enter your choice: ")

    if choice == '1':
        filename = input("Enter the filename: ")
        text = input("Enter the text to write: ")
        write_to_file(filename, text)
    elif choice == '2':
        filename = input("Enter the filename: ")
        words = read_file(filename)
        print("Number of words in the file:", words)
    elif choice == '3':
        break
    else:
        print("Invalid choice. Please try again.")
