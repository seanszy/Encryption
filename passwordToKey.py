import random

def passwordToKey(password):
    """This function converts the passwords to a number. It iterates through
    each char and converts that to an int then adds them together"""

    #empty list
    sum_char = ""

    #Iterates through chars
    for char in password:
        char = ord(char) + 100 #adds 100 to make all values 3 digits
        char = str(char)
        sum_char += char
    return(int(sum_char))
