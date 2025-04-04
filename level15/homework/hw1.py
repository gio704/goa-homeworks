numbers = [1, 4, 3, 6, 9, 11, 17, 13, 26, 30]

even_sum = 0
odd_count = 0

for num in numbers:
    if num % 2 == 0:
        even_sum += num
    else:
        odd_count += 1

print("ლუწი რიცხვების ჯამი:", even_sum)
print("კენტი რიცხვების რაოდენობა:", odd_count)