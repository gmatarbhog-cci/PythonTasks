def sum_of_numbers(numbers, target):
    # Validations
    if len(numbers) < 2 or len(numbers) > 104:
        print("Numbers list cannot have less than 2 items or more than 104 items")
        return
    if any(i > 109 for i in numbers) or any(i < -109 for i in numbers):
        print("Any item in numbers list cannot be less than -109 or greater than 109")
        return
    if target > 109 or target < -109:
        print("Target cannot be less than -109 or greater than 109")
        return
    indexes = []
    for i in numbers:
        for k in numbers:
            if i + k == target:
                indexes.append(numbers.index(i))
                indexes.append(numbers.index(k))
                print(indexes)
                break
        if len(indexes) > 0:
            break


sum_of_numbers([11, 15, 2, 7], 9)
