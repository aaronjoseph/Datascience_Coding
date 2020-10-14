import string

def find_max_letter_count(word):
    alphabet = string.ascii_lowercase
    dictionary = {}

    for letters in alphabet:
        dictionary[letters] = 0

    for letters in word:
        dictionary[letters] += 1
    
    max = 0 
    max_val = ''
    for key,value in dictionary.items():
        if max < value:
            max = value
            max_val = key 
    return(max_val,max)
    
