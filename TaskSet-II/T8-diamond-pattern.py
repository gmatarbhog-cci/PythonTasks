def create_diamond_pattern(rows):
    for i in range(rows):
        print('-'*(rows-i-1) + '*-'*(i+1))
    for i in range(rows):
        print('-'*(i+1) + '*-'*(rows-i-1))


create_diamond_pattern(5)
