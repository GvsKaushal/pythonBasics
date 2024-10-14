def factorial(n):
    if n == 0:
        return 1
    else:
        return n * factorial(n - 1)


while True:
    try:
        num = int(input("Enter a number: "))
        result = factorial(num)
        print("Factorial of", num, "is", result)

    except:
        print("only numbers")

    choice = input("Do you want to check another number? (y/n): ")
    if choice.lower() == "n":
        break
