def create_left_triangle_pattern(rows):
    num_spaces = rows * 2
    for i in range(1, rows+1):
        # print initial spaces
        for j in range(num_spaces):
            print(end=' ')
        num_spaces = num_spaces - 2
        for k in range(i):
            print(i, end=' ')
        print('')


create_left_triangle_pattern(5)
