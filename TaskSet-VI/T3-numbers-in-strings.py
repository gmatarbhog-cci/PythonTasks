def numInStr(arr):
    matches = []
    for element in arr:
        if any(char.isdigit() for char in element):
            matches.append(element)
    print(matches)


numInStr(["1a", "a", "2b", "b"])
