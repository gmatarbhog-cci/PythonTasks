def sum_of_numbers(numbers, target):
    # Validations
    if len(numbers) < 2 or len(numbers) > 104:
        raise Exception("Numbers list cannot have less than 2 items or more than 104 items")
    if any(i > 109 for i in numbers) or any(i < -109 for i in numbers):
        raise Exception("Any item in numbers list cannot be less than -109 or greater than 109")
    if target > 109 or target < -109:
        raise Exception("Target cannot be less than -109 or greater than 109")
    indexes = []
    for i in numbers:
        for k in numbers:
            if i + k == target:
                indexes.append(numbers.index(i))
                indexes.append(numbers.index(k))
                return indexes


print(sum_of_numbers([11, 15, 2, 7], 9))
