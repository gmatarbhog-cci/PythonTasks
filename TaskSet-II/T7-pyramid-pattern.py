def create_pyramid_pattern(rows):
    num_spaces = rows
    for i in range(rows):
        # print spaces
        for j in range(num_spaces):
            print(end=' ')
        num_spaces = num_spaces - 1
        for k in range(i+1):
            print('*', end=' ')
        print('')


create_pyramid_pattern(5)
