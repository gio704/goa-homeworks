print('password must contain more than 8 char, must contain A')
password = input('enter a password: ')

mcdeloba = 0

while len(password) < 8 or "A" not in password:
    mcdeloba += 1
    if mcdeloba == 3:
        print("you can not try again")
    password = input('enter a password: ')    
print("correct")



