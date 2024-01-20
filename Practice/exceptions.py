count = 0

# if count != 2:

    # assert(count != 0)
    # raise Exception('Count not matching')

try:
    with open('test.txt', 'r') as file:
        file.read()
except Exception as e:
    print()
    print(e)
finally:
    print('in finally')
