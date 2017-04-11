import math
import numpy


def msg_to_int(msg):
    msg_int = []
    for char in msg:
        msg_int.append(ord(char) + 100)
    msg_int = int(''.join(map(str, msg_int)))
    return(msg_int)

def int_to_msg(long_int):
    long_int = str(long_int)
    msg = [long_int[i:i+3] for i in range(0, len(long_int), 3)]
    msg = list(map(int, msg))
    msg[:] = [x - 100 for x in msg]
    final_string = ''.join(chr(i) for i in msg)
    return(final_string)

def find_e(phi):
    non_primes = set(j for i in range(2, 8) for j in range(i*2, 200, i))
    primes = [x for x in range(2, 200) if x not in non_primes]
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
    if g != 1:
        print('No modular inverse.')
    else:
        d = (x % phi)
        return(d)


def main():
    p = 12131072439211271897323671531612440428472427633701410925634549312301964373042085619324197365322416866541017057361365214171711713797974299334871062829803541
    q = 12027524255478748885956220793734512128733387803682075433653899983955179850988797899869146900809131611153346817050832096022160146366346391812470987105415233
    n = p * q
    phi = (p - 1) * (q - 1)

    msg = input("Enter Message:")
    msg_int = msg_to_int(msg)
    e = find_e(phi)
    d = mod_inv(e, phi)
    encrypted = pow(msg_int, e, n)
    decrypted = pow(encrypted, d, n)
    msg_decrypted = int_to_msg(decrypted)
    print("Your message was:", msg_decrypted)


if __name__ == '__main__':
    main()
