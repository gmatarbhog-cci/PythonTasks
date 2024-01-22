import string


# calculate total sentence value
def calculate_sentence_value(sentence):
    total_value = 0
    for letter in sentence:
        letter_value = get_alphabet_value(letter)
        total_value += letter_value
    return total_value


# get numeric letter value
def get_alphabet_value(letter):
    ascii_difference = 86
    for alphabet in list(string.ascii_lowercase):
        if letter.lower() == alphabet:
            num_value = ord(alphabet) - ascii_difference
            return num_value


print(calculate_sentence_value("Test"))
