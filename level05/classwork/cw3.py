correct_password =  "gio"
user_password = input("password: ")

while user_password != correct_password:
    print("password is incorrect")
    user_password = input("password: ")

print("password is correct")