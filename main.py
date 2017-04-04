import random
import binary
import XOR
import passwordToKey
import csv

password = "yolos"
long_key_password_int = passwordToKey.passwordToKey(password)
print(long_key_password_int)
long_key_password = binary.to_binary(long_key_password_int)

p = random.randint(1000000, 10000000)
q = random.randint(1000000, 10000000)
print(" Origin P:", p, "\n", "Origin Q:", q)

long_key_one = p
long_key_two = q
long_key_one_binary = binary.to_binary(long_key_one)
long_key_two_binary = binary.to_binary(long_key_two)
Xored_p = XOR.XOR(long_key_one_binary, long_key_password)
Xored_q = XOR.XOR(long_key_two_binary, long_key_password)

print("Encypher:", Xored_p + "Z" + Xored_q)


deXore_p = XOR.XOR(Xored_p, long_key_password)
deXore_q = XOR.XOR(Xored_q, long_key_password)
decoded_one = binary.from_binary(deXore_p)
decoded_two = binary.from_binary(deXore_q)
print(" Decode P:", decoded_one)
print(" Decode Q:", decoded_two)
