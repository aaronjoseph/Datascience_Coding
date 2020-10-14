import string

def find_max_letter_count(word):

    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1

    dictionary = sorted(dictionary.items(), 
                        reverse=True, 
                        key=lambda x: x[1])

    for position in range(0, 26):
        print(dictionary[position])
        if position != len(dictionary) - 1:
            if dictionary[position + 1][1] < dictionary[position][1]:
                break

find_max_letter_count("helloworld")
