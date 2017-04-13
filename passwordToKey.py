import random

def passwordToKey(password):
    sum_char = ""
    for char in password:
        char = ord(char) + 100
        char = str(char)
        sum_char += char
    return(int(sum_char))
