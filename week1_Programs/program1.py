while True:

    try:
        num = int(input("Enter a number: "))

        if num > 0:
            print(num, "is positive.")
        elif num < 0:
            print(num, "is negative.")
        else:
            print(num, "is zero.")

    except:
        print("only numbers")

    choice = input("Do you want to check another number? (y/n): ")
    if choice.lower() == "n":
        break
