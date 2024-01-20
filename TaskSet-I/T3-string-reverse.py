def reverse_string(string):
    str = ""
    for i in range(len(string)-1, -1, -1):
        str = str + string[i]
    return str


print(reverse_string("hello"))
print(reverse_string("goa"))
print(reverse_string("India"))
