def sum_numbers(a, b):
    def to_int(value):
        if isinstance(value, bool):
            return int(value)
        if isinstance(value, str):
            try:
                return int(float(value))
            except ValueError:
                raise ValueError(f"სტრინგი '{value}' არ შეიცავს ვალიდურ რიცხვს.")
        if isinstance(value, float):
            return int(value)
        if isinstance(value, int):
            return value
        raise TypeError(f"მიუღებელი ტიპი: {type(value)}")

    return to_int(a) + to_int(b)
