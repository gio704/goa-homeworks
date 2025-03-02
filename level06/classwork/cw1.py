num = int(input("enter a number: "))
is_prime = True
for i in range(2, num):
    if num % i == 0:
        is_prime = False
        break
if is_prime and num > 1:
    print("Your number is a prime.")
else:
    print("Your number is not a prime.")




            


