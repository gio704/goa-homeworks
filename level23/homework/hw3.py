def combine_strings(*args):
    strings = []
    numbers = []

    for arg in args:
        if isinstance(arg, str):
            strings.append(arg)
        elif isinstance(arg, int):
            numbers.append(str(arg))
        else:
            raise TypeError(f"მხოლოდ string და integer არგუმენტებია დასაშვები. მიღებულია: {type(arg)}")

    sentence = " ".join(strings)
    if numbers:
        sentence += " " + " ".join(numbers)

    return sentence