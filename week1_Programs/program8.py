class Engine:
    def __init__(self):
        self.is_running = False

    def start(self):
        if not self.is_running:
            print("Engine started.")
            self.is_running = True

    def stop(self):
        if self.is_running:
            print("Engine stopped.")
            self.is_running = False


class Car:
    def __init__(self, model, year):
        self.model = model
        self.year = year
        self.engine = Engine()

    def start_engine(self):
        self.engine.start()

    def stop_engine(self):
        self.engine.stop()


if __name__ == "__main__":
    model = input("Enter the car model: ")
    year = int(input("Enter the car year: "))

    car = Car(model, year)

    while True:
        print("1. Start Engine")
        print("2. Stop Engine")
        print("3. Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            car.start_engine()
        elif choice == '2':
            car.stop_engine()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please try again.")
