def calculator(x, y, op):
    if int == type(x) and  int == type(y):
        if op == '+':
            return x + y
        elif op == '-':
            return x -y
        elif op == '*':
            return x * y
        elif op == '/':
            return x / y
        else:
            return "unknown value"
    else:
        return    "unknown value"