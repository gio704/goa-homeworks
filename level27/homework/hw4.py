def sum_of_numbers():
    numbers = []

    for i in range(5):
        num = int(input(f"Enter number {i+1}: "))
        numbers.append(num)

    total = sum(numbers)
    print("The sum of the numbers is:", total)