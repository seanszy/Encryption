def to_binary(long_key):
    long_key_hex = hex(long_key)
    long_key_str = str(long_key_hex)

    sum = ""
    for item in long_key_str:
        current_char = ord(item)+100
        current_char = str(current_char)
        sum += current_char
    binary_of_sum = bin(int(sum))
    return binary_of_sum

def from_binary(long_key_binary):
    long_key_hex = ""
    long_key_int = int(long_key_binary, 2)
    range_variable = len(str(long_key_int))/3
    long_key_string = str(long_key_int)
    count = 0
    for value in range(int(range_variable)):
        int_triple = int(long_key_string[count:count+3])
        current_char = chr((int_triple)-100)
        long_key_hex += current_char
        count+=3
    long_key_int_original = int(long_key_hex, 16)
    return long_key_int_original

long_key_one = 123456
long_key_two = 654321
long_key_one_binary = to_binary(long_key_one)
long_key_two_binary = to_binary(long_key_two)
decoded_one = from_binary(long_key_one_binary)
decoded_two = from_binary(long_key_two_binary)
print("Origin One:", long_key_one)
print("Decode One:", decoded_one)
print("Origin Two:", long_key_two)
print("Decode Two:", decoded_two)
