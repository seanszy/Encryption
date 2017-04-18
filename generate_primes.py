from Crypto.Util import number
from Crypto.PublicKey import RSA
import random

def main():
    length = 300
    p = number.getPrime(length)
    q = number.getPrime(length)
    return [int(p), int(q)]
