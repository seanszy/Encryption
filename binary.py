def to_binary(long_key):
    """This function converts an integer to a binary number. To make the
    numbers longer in order to make a longer key for XOR encryption, the
    number is converted to hex, which is then converted to a different number,
    and that number is converted to binary"""

    long_key_hex = hex(long_key) #convert to hex
    long_key_str = str(long_key_hex)

    sum = "" #sum is used to combine the numeric values of the hex chars
    for item in long_key_str: #This loop converts the hex to an integer
        current_char = ord(item)+100 #100 is added, so all chars give 3 digit ints
        current_char = str(current_char)
        sum += current_char
    binary_of_sum = bin(int(sum)) #convert to binary
    return binary_of_sum

def from_binary(long_key_binary):
    """This function does the opposite of the above function. It converts binary
    numbers back to integers. This is used in the process to decode the encypher"""

    long_key_hex = ""
    long_key_int = int(long_key_binary, 2) #convert to a number from binary

    range_variable = len(str(long_key_int))/3 #The chars are represented by
    #3 dgit ints, so running it the length/3 is the right number
    long_key_string = str(long_key_int)
    count = 0
    for value in range(int(range_variable)): #for loop converts each int to char
        int_triple = int(long_key_string[count:count+3]) #finds next 3 numbers
        current_char = chr((int_triple)-100) #converts to char
        long_key_hex += current_char #adds to list of chars
        count+=3
    long_key_int_original = int(long_key_hex, 16) #converts to number
    return long_key_int_original
