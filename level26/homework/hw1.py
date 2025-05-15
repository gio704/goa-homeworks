def check_type(value):
    if isinstance(value, str):
        print("Literature")
    elif isinstance(value, (int, float)):
        print("Math")
    elif isinstance(value, bool):
        print("Science")
    else:
        print("Unknown type")