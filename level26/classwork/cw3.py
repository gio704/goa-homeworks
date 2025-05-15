def multiply(number):
    digits = len(str(abs(number)))
    return number * (5 ** digits)