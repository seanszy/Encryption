import random

def passwordToKey(password):
    sum_char = ""
    for char in password:
        char = ord(char) + 100
        char = str(char)
        sum_char += char

    random.seed(sum_char)
    key_short = random.randint(10000, 20000)
    return(key_short)
