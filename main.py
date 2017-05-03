"""This is the main function of the document...WRITE MORE WHEN IM NOT LAZY AF"""

#Import all the other python files that we want to run
import random
import binary
import XOR
import passwordToKey
import RSA_Encryption_New
import generate_primes


def create_encypher(password):
    """This function is used to do all of the conversion from the user password
    to binary and then takes that information and creates an encypher key by
    referencing our other programs to do XOR encrytion"""


    if len(password) > 7: #make sure the password is longer
        password = password + password + password + password
        long_key_password_int = passwordToKey.passwordToKey(password) #converts the user password to an integer
        long_key_password = binary.to_binary(long_key_password_int) #converts users password to a binary

        #use the generate primes file to generate primes
        primes = generate_primes.main()
        #pull p and q from the returned value
        p = primes[0]
        q = primes[1]


        #converts p and q to binary using our program
        long_key_one_binary = binary.to_binary(p)
        long_key_two_binary = binary.to_binary(q)

        #XOR P and Q with the password using XOR file
        Xored_p = XOR.XOR(long_key_one_binary, long_key_password)
        Xored_q = XOR.XOR(long_key_two_binary, long_key_password)

        #This is the encypher which we store on the computer
        #The p and q are separated by a Z so they can be distinguished from
        #one another
        Encypher = Xored_p + "Z" + Xored_q
        return Encypher
    else: #if password is too short, this occurs
        print("I am sorry, your password is too short. Try a password with 8 or more characters")


def decode_encypher(password, Encypher):
    """This function is used to decode the encipher and retrieve the prime numbers. If references the XOR file and the binary file to do this."""
    password = password + password + password + password
    long_key_password_int = passwordToKey.passwordToKey(password) #converts the user password to an integer
    long_key_password = binary.to_binary(long_key_password_int) #converts users password to a binary
    index = Encypher.find("Z") #finds the index of Z

    #Breaks it up and finds the encyphered versions of p and q
    Xored_p_from_cypher = Encypher[0:index]
    Xored_q_from_cypher = Encypher[index+1:]

    #XOR the password again. Used to decrypt Encypher
    deXore_p = XOR.XOR(Xored_p_from_cypher, long_key_password)
    deXore_q = XOR.XOR(Xored_q_from_cypher, long_key_password)

    #Convert from binary back to original int
    decoded_one = binary.from_binary(deXore_p)
    decoded_two = binary.from_binary(deXore_q)
    return[decoded_one, decoded_two]
    #RSA_Encryption.run_rsa()

"""
password = input("Input Password \n")
encypher = create_encypher(password)
password = input("Input Password \n")
p_q = decode_encypher(password, encypher)
message = input("Type your message to encode\n")
RSA_Encryption_New.main(p_q[0], p_q[1], message)
decode_encypher(password, encypher)
"""
