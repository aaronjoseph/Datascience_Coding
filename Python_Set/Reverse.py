sentence = "The quick b +rown fox jumps "

import re
sentence = re.sub(' +', ' ', sentence.strip())

sentence[::-1]

" ".join(sentence.strip().split(" ")[::-1])

def reverse_word(sentence):
    sentence = sentence.split()
    str_len = len(sentence)

