class Animal:
    def __init__(self, name):
        self.name = name

    def sound(self):
        print(f"{self.name} makes a sound.")


class Dog(Animal):
    def sound(self):
        print(f"{self.name} barks.")


class Cat(Animal):
    def sound(self):
        print(f"{self.name} meows.")


if __name__ == "__main__":
    while True:
        print("1. Create a Dog")
        print("2. Create a Cat")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter the dog's name: ")
            dog = Dog(name)
            dog.sound()
        elif choice == '2':
            name = input("Enter the cat's name: ")
            cat = Cat(name)
            cat.sound()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
