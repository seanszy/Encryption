from Crypto.Util import number
def main():
    length = 300
    p = number.getPrime(length)
    q = number.getPrime(length)
    return [int(p), int(q)]
