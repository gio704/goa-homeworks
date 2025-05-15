def check_password():
    password = input("შეიყვანე პაროლი: ")
    if len(password) < 8:
        print("პაროლი ძალიან მოკლეა")
    else:
        print("პაროლი მიღებულია")