def remove_divisible_by_3(numbers):
    result = []
    for num in numbers:
        if num % 3 != 0:
            result.append(num)
    return result