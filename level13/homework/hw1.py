number = int(input("Enter a three-digit number: "))

sum_of_digits = sum(int(digit) for digit in str(number))

remainder = number % sum_of_digits

print(remainder)