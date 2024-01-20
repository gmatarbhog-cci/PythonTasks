def check_num_exists_in_list(array_one, array_two, input_number):
    found_arr_one = 0
    found_arr_two = 0

    if input_number in array_one:
        found_arr_one = 1

    if input_number in array_two:
        found_arr_two = 1

    if found_arr_two > 0 and found_arr_one > 0:
        print("Number found in both arrays")
    elif found_arr_one > 0:
        print("Number found in array one")
    elif found_arr_two > 0:
        print("Number found in array two")
    else:
        print("Not found in both arrays")


check_num_exists_in_list([1, 5, 8, 9, 10], [5, 8, 9, 10, 12, 20, 40, 60, 70], 1)
