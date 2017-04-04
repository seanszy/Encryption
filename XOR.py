def XOR(b1, b2):
    """This function is used to conduct XOR logic. We use XOR as a way to
    encrypt our private keys. This function runs XOR on two binary numbers that
    are passed in"""
    
    b1 = str(b1)
    b2 = str(b2)

    #binary numbers can start with "0b", which throws an error. To prevent this
    #those letters were removed if they existed
    if b1[0:2] == '0b':
        b1 = b1[2:]
    if b2[0:2] == '0b':
        b2 = b2[2:]

    #converts strings into list of integers
    b1 = [int(x) for x in str(b1)]
    b2 = [int(x) for x in str(b2)]
    b3 = []

    #does XOR logic
    if len(b1) > len(b2): #data will be lost if b1 > b2, so we print ERROR. This should never occur
        print("ERROR")
    else:
        for i, bit in enumerate(b1): #moves through each item in list
            if bit + b2[i] is 1: #XOR is 1 if they add to 1
                b3.append(1)
            else: #It is 0 if they do not
                b3.append(0)
    b3 = ''.join(map(str, b3)) #combine them into a string
    return(b3)
