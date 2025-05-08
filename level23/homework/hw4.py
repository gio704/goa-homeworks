def check_type_match(value, type_to_check):
    if isinstance(type_to_check, str):
        try:
            expected_type = eval(type_to_check)
        except NameError:
            raise ValueError(f"უცნობი ტიპი: {type_to_check}")
    elif isinstance(type_to_check, type):
        expected_type = type_to_check
    else:
        raise TypeError("მეორე არგუმენტი უნდა იყოს ტიპი ან ტიპის სახელი string-ად.")

    return isinstance(value, expected_type)