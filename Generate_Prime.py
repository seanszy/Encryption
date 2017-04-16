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

def generate_prime(input):
    random.seed(input)
    lower_bound = random.randint(20000, 20000000)
    upper_bound = lower_bound +100
    non_primes = set(j for i in range(2, 8) for j in range(i*2, upper_bound, i))
    primes = [x for x in range(lower_bound, upper_bound) if x not in non_primes]

    count = 0
    while True:
        count += 1
        found_prime = isprime(primes[count])
        if found_prime:
            return primes[count]


def main(input):
    random.seed(input)
    lower_bound = random.randint(20000, 20000000)
    p = generate_prime(lower_bound)
    random.seed(lower_bound)
    lower_bound2 = random.randint(20000, 20000000)
    q = generate_prime(lower_bound2)
    return[p, q]
