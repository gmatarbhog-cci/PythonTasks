def create_right_triangle_pattern(rows):
    for i in range(1, rows+1):
        for k in range(1, i+1):
            print(i, end=' ')
        print('\r')


create_right_triangle_pattern(5)
