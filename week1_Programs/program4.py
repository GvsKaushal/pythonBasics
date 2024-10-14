def find_largest_smallest(numbers):
    if len(numbers) != 0:
        largest = numbers[0]
        smallest = numbers[0]

        for num in numbers:
            if num > largest:
                largest = num
            elif num < smallest:
                smallest = num

        print("Largest number:", largest)
        print("Smallest number:", smallest)
    else:
        print("list is empty")


numbers = []
find_largest_smallest(numbers)
