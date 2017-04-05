import time
from fractions import gcd

def find_d(e, phi_public):
    correct_d = False
    n = 1
    while correct_d == False:
        n += 1
        a = phi_public*n+1
        b = a/e
        print(b, n)
        if b%1 == 0:
            correct_d = True
    return b

def generate_codes(private_key_1, private_key_2):
    public_key = private_key_1*private_key_2
    phi_1 = private_key_1-1
    phi_2 = private_key_2-1
    phi_public = phi_1*phi_2
    correct_e = False
    current_e = 1

    while correct_e == False:
        current_e = current_e + 2
        if gcd(phi_public, current_e)== 1:
            correct_e = True
    d_is_integer = True
    k = 1

    d = find_d(current_e, phi_public)
    #d = current_e.modInverse(private_key_1.multiply(private_key_2))

    print("K: ", k)
    print("Public Key: ", public_key)
    print("Phi_Public: ", phi_public)
    print("e: ", current_e)
    print("d: ", d)
    return [public_key, current_e, phi_1, phi_2, phi_public, private_key_1, private_key_2, d]

def encode(input, public_key, e):
    #print(input, e, "ex")
    exponent = input**e
    return ((input**e)%public_key)
def decode(input, public_key, e, phi_1, phi_2, phi_public, private_key_1, private_key_2, d):
    value = do_exponents_2(input, int(d), public_key)
    return value
    """
    print(input, int(d))
    code = input**int(d)
    #print(input, d)
    #print(code)
    return(code%public_key)
    """

def Represents_Int(string):
    try:
        int(string)
        return True
    except:
        return False

def char_encode(value, information):
    message_list = []
    for char in value:
        inputs = ord(char)
        encodes = encode(inputs, information[0], information[1])
        message_list.append(encodes)
    print("\nHere is your encrypted code: ", message_list)
        #print("Encrypted Message: ", encodes)

    return message_list

def int_encode(value, information):
    encodes = encode(int(value), information[0], information[1])
    #print("Encrypted Message: ", encodes)
    print("\nHere is your encrypted code: ", encodes)
    #print("message: ", message)
    return encodes

def do_exponents(base, exponent, public_key):
    #control = base**exponent
    control = 1
    #print("\nMessage: ", base)
    #print("d: ", exponent, "\n")
    binary_base = bin(exponent)
    #print(binary_base)
    binary_base = str(binary_base)
    binary_base = binary_base[2:]
    #print(binary_base)
    binary_base_list = list(binary_base)
    #print("Control: ", control%public_key, "\n", binary_base, "\n", binary_base_list)
    binary_values = [base]
    #print(binary_values)
    calculated_value = 1
    temp_base = 1
    count = len(binary_base_list)-1
    binary_with_0 = []
    #print(len(binary_base))
    count2 = 0
    for binary in binary_base_list:
        count2 += 1
        if int(binary) == 0:
            binary_with_0.append(count)
        #print(binary_with_0, "Count", count)
        count -= 1
        base = base*base%public_key
        #print("$", count2, "   $", base)
        #print(base, len(str(base)), count2)
        binary_values.append(base)
    binary_values = binary_values[0:len(binary_values)-1]
    binary_values_2 = binary_values
    #print(binary_values, "\n", count2, "COUNT2")
    #print(binary_with_0, "ZEROES")
    #print(binary_values, "BV")
    count4 = 0
    for items in binary_with_0:
        #print(items)
        binary_values.pop(items)
        #binary_values[items] = 1
        #print("$", count4, binary_values[items], " $$ ", binary_values_2[items])
    #print(binary_values)
    for items in range(len(binary_values)):
        count4 += 1
        #print("$", count4, binary_values[items], " $$ ", binary_values_2[items])

    count3 = 0
    for numbers in range(len(binary_values)):
        count3+=1
        #print(count3)
        calculated_value = calculated_value*binary_values[numbers]
    #print(calculated_value%public_key, "CALC")
    #print(calculated_value)
    #print("PUBLIC KEY", public_key)
    return calculated_value%public_key

def do_exponents_2(base, exponent, public_key):
    #control = base**int(exponent)
    control_binary = bin(exponent)
    control_binary_2 = control_binary[2:]
    control_binary_3 = list(reversed(control_binary_2))
    print(control_binary, "\n", control_binary_2, "\n", control_binary_3)
    full_binary_list = []
    binary_list_ones = []
    count = 0
    for item in control_binary_3:
        full_binary_list.append(base)
        if int(item) == 1:
            binary_list_ones.append(base)
        else:
            binary_list_ones.append(1)
        count += 1
        base = (base*base)
        print("CHECK ERROR: ", base)
        base = base%public_key

    #print(binary_list_ones)
    #print(full_binary_list)
    sums = 1
    for item in binary_list_ones:
        #print("Old Sum", sums, "Multiply", item)
        sums = item*sums
        #print("new sum", sums)
    sums = sums % public_key
    return(sums)



def main():
    information = generate_codes(110060893, 110060917) #correct
    #information = generate_codes(110060917, 110060921) #gives 1
    #information = generate_codes(110060921, 110060947) #gives wrong value
    #information = generate_codes(113, 127) #test
    p1 = 110060893
    p2 = 110060917
    p3 = 110060921
    p4 = 110060947
    print("TEST2", p3*p4)
    print("TEST1", p1*p2)
    print("TEST3", p3*p4 - p1*p2)
    #information2 = generate_codes(53, 59)
    value = input("What message do you want to send?\n")
    time.sleep(1)
    is_int = Represents_Int(value)
    message_list = ""
    if is_int == False:
        value = list(value)
        message_list = char_encode(value, information)
        message_list = letter_decrypt(message_list, information)
    else:
        message_list = int_encode(value, information)
        message_list = integer_decrypt(message_list, information)
    return message_list

def letter_decrypt(message_list, information):
    print("msg", message_list)
    decrypted_list = []
    for messages in message_list:
        message = decode(messages, information[0], information[1], information[2], information[3], information[4], information[5], information[6], information[7])
        #print("message: ", message)
        decrypted_list.append(message)
    decrypted_message = ""
    for char in decrypted_list:
        decrypted_message +=(chr(char))
    return decrypted_message

def integer_decrypt(encoded_integer, information):
    message = decode(encoded_integer, information[0], information[1], information[2], information[3], information[4], information[5], information[6], information[7])
    return message

def run_rsa():
    #do_exponents(2615385, 1873325)
    encoded_list = main()
    #time.sleep(1)
    #decrypted_message = letter_decrypt(encoded_list)
        #decrypted_message = integer_decrypt(encoded_list)
    print("\nDECRYPTING MESSAGE...")
    #time.sleep(1)
    print("\nYour message is:", encoded_list)

"""
if __name__ == '__main__':
    #do_exponents(2615385, 1873325)
    encoded_list = main()
    #time.sleep(1)
    #decrypted_message = letter_decrypt(encoded_list)
        #decrypted_message = integer_decrypt(encoded_list)
    print("\nDECRYPTING MESSAGE...")
    #time.sleep(1)
    print("\nYour message is:", encoded_list)
"""
