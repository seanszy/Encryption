import math
import random

def isprime(n):
    '''check if integer n is a prime. This check prime function was modified
    from an online source.'''
    # make sure n is a positive integer
    n = abs(int(n))
    # 0 and 1 are not primes
    if n < 2:
        return False
    # 2 is the only even prime number
    if n == 2:
        return True
    # all other even numbers are not primes
    if not n & 1:
        return False
    # range starts with 3 and only needs to go up the squareroot of n
    # for all odd numbers
    for x in range(3, int(n**0.5)+1, 2):
        if n % x == 0:
            return False
    return True

def generate_prime():
    is_prime = False
    while is_prime == False:
        potential_prime = random.randint(1000, 20000)
        #print(potential_prime)
        is_prime = isprime(potential_prime)
    return potential_prime

#p = generate_prime("hey")
#print(p)
#q = generate_prime()
#print("P is: ", p)
#print("Q is: ", q)
#return [p, q]

def main():
    p = generate_prime()
    q = generate_prime()
    print("P is: ", p)
    print("Q is: ", q)
    return [p, q]
