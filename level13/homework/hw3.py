number = int(input("enter a whole number: ")) 

if number % 2 == 0:
    number += 5
else:
    number *= 3

total = number + number

remainder = total % 5

print("The remainder of dividing the sum of numbers by 5:", remainder)