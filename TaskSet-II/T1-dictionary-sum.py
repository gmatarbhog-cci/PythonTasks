def sum_dict(dict):
    sum = 0
    for item in dict.values():
        sum += item
    return sum


print(sum_dict({"a": 200, "b": 300, "c": 400}))
