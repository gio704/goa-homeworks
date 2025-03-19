numbers = 30678
user_numbers = int(input("enter a 4 numbers: "))

while user_numbers != numbers:
    if len(str(user_numbers)) != len(str(numbers)):
     print("the sequence consits of 4 numbers and  must not exceed")


    user_numbers = int(input("the sequence is incorrect try again"))


print("you guessed the sequence correctly")    