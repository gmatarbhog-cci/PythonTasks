def check_if_palindrome_number(number):
    reversed_num = str(number)[::-1]
    print('{} is a palindrome number'.format(number)) if str(number) == reversed_num else print('{} is not a palindrome number'.format(number))


check_if_palindrome_number(154451)
