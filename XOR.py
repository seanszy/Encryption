def XOR(b1, b2):
    b1 = str(b1)
    b2 = str(b2)
    if b1[0:2] == '0b':
        b1 = b1[2:]
    if b2[0:2] == '0b':
        b2 = b2[2:]
    b1 = [int(x) for x in str(b1)]
    b2 = [int(x) for x in str(b2)]
    b3 = []

    if len(b1) > len(b2):
        print("ERROR")
    else:
        for i, bit in enumerate(b1):
            if bit + b2[i] is 1:
                b3.append(1)
            else:
                b3.append(0)
    b3 = ''.join(map(str, b3))
    return(b3)
