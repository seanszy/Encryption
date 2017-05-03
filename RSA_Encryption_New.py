import math
import numpy


def msg_to_int(msg):
    """This function converts the message to an integer. It does so for each
    char, but adds 100 to each char in order to make each integer 3 digits long.
    This makes parsing significantly easier"""

    msg_int = []

    #Loops through each char
    for char in msg:
        msg_int.append(ord(char) + 100)
    msg_int = int(''.join(map(str, msg_int))) #combines list to integer
    return(msg_int)

def int_to_msg(long_int):
    """This function converts an integer back into a message. It does so by
    taking blocks of 3 digit integers and converting them to chars"""

    long_int = str(long_int)

    #Converts large integer into many 3 digit integers
    msg = [long_int[i:i+3] for i in range(0, len(long_int), 3)]
    msg = list(map(int, msg))
    msg[:] = [x - 100 for x in msg]
    final_string = ''.join(chr(i) for i in msg)
    return(final_string)

def find_e(phi):
    """The e value is used in RSA encryption. This functions finds the value.
    e is a number that is coprime with phi_q*phi_p"""

    # Generate Primes
    non_primes = set(j for i in range(2, 8) for j in range(i*2, 200, i))
    primes = [x for x in range(2, 200) if x not in non_primes]
    # Check if prime
    for prime in primes:
        if math.gcd(phi, prime) is 1:
            return(prime)
            break


# d = gcd(a,b)
# d = ax + by
def EEA(a, b):
    if a == 0:
        return (b, 0, 1)
    else:
        g, y, x = EEA(b % a, a)
        return (g, x - (b // a) * y, y)


# ex-phi*q = 1
def mod_inv(e, phi):
    g, x, y = EEA(e, phi)
    if g = 1:
        d = (x % phi)
        return(d)

def decrypt(p, q, message):
    """This function decrypts the user-stored passwords. It takes the stored int representation of their saved password
    and converts it to a string and returns it."""
    n = p * q
    phi = (p - 1) * (q - 1)
    msg = int(message)
    e = find_e(phi)
    d = mod_inv(e, phi)
    decrypted = pow(msg, d, n)
    msg_decrypted = int_to_msg(decrypted) #Convert int to string
    return(msg_decrypted)

def encrypt(p, q, message):
    """This function encrypts a password that a user wishes to store. It converts the string to an int and then excrypts it."""
    n = p * q
    phi = (p - 1) * (q - 1)
    msg = message
    msg_int = msg_to_int(msg) #Convert message to int
    e = find_e(phi)
    encrypted = pow(msg_int, e, n)
    return(encrypted)

def main(p, q, message):
    """The main function for this process. It handles calling other functions to encrypt and decrypt as needed."""
    n = p * q
    phi = (p - 1) * (q - 1)
    msg = message
    msg_int = msg_to_int(msg) #Convert message to int
    e = find_e(phi)
    d = mod_inv(e, phi)
    encrypted = pow(msg_int, e, n) #Formula to encrypt
    decrypted = pow(encrypted, d, n) #Formula to decrypt
    msg_decrypted = int_to_msg(decrypted)
