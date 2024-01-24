def sort_array(arr):
    # loop on the array
    for idx in range(len(arr)):
        min = idx
        # sort the array
        for element in range(idx + 1, len(arr)):
            if arr[min] > arr[element]:
                min = element

        arr[idx], arr[min] = arr[min], arr[idx]
    return arr


print(sort_array([12, 79, 34, 12, 22, 8, 1]))
