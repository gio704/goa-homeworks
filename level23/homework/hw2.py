def divide_larger_by_smaller(a, b):
    def to_number(value):
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, str):
            try:
                return float(value)
            except ValueError:
                raise ValueError(f"სტრინგი '{value}' არ წარმოადგენს რიცხვს.")
        if isinstance(value, (int, float)):
            return float(value)
        raise TypeError(f"მიუღებელი ტიპი: {type(value)}")

    num1 = to_number(a)
    num2 = to_number(b)
    larger = max(num1, num2)
    smaller = min(num1, num2)

    if smaller == 0:
        raise ZeroDivisionError("გამყოფი არ შეიძლება იყოს 0")

    return larger / smaller