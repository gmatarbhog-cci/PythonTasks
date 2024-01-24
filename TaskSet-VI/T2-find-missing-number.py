def FindMissingNumber(arr, n):
    i = 0
    # sort the array
    while i < n and i <= len(arr)-1:
        correctindex = arr[i] - 1  # since difference between numbers is 1
        if arr[i] < n and arr[i] != arr[correctindex]:
            arr[i], arr[correctindex] = arr[correctindex], arr[i]
        else:
            i += 1

    # loop the sorted array and find the missing element
    for index in range(n):
        if arr[index] != index + 1:
            return index + 1

    return n


print(FindMissingNumber([6, 1, 2, 8, 3, 4, 7, 10, 9], 10))
