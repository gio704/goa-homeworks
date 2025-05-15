def operation_type():
    expr = input("შეიყვანე მათემატიკური გამოსახულება: ")
    try:
        result = eval(expr)
        print("შედეგის ტიპია:", type(result).__name__)
    except:
        print("შეცდომა: არასწორი გამოსახულება")