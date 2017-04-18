"""This is the main function of the document...WRITE MORE WHEN IM NOT LAZY AF"""

#Import all the other python files that we want to run
import random
import binary
import XOR
import passwordToKey
import Generate_Prime
import RSA_Encryption_New
import generate_primes


def create_encypher(password):
    if len(password) > 7:
        long_key_password_int = passwordToKey.passwordToKey(password) #converts the user password to an integer
        long_key_password = binary.to_binary(long_key_password_int) #converts users password to a binary



        primes = generate_primes.main()
        p = primes[0]
        q = primes[1]
        print(" P: ", p, "\n", "Q: ", q)
        #long_key_one_binary = bin(p)
        #long_key_two_binary = bin(q)
        #convert P and Q to binary
        long_key_one = p
        long_key_two = q
        long_key_one_binary = binary.to_binary(long_key_one)
        long_key_two_binary = binary.to_binary(long_key_two)

        #XOR P and Q
        Xored_p = XOR.XOR(long_key_one_binary, long_key_password)
        Xored_q = XOR.XOR(long_key_two_binary, long_key_password)

        #This is the encypher which we store on the computer
        #print("Encypher:", Xored_p + "Z" + Xored_q)
        Encypher = Xored_p + "Z" + Xored_q
        print("Encypher:", Encypher)
        return Encypher
    else:
        print("I am sorrry, your password is too short. Try a password with 8 or more characters")


def decode_encypher(password, Encypher):
    long_key_password_int = passwordToKey.passwordToKey(password) #converts the user password to an integer
    long_key_password = binary.to_binary(long_key_password_int) #converts users password to a binary
    index = Encypher.find("Z")
    Xored_p_from_cypher = Encypher[0:index]
    Xored_q_from_cypher = Encypher[index+1:]

    #XOR the password again. Used to decrypt Encypher
    deXore_p = XOR.XOR(Xored_p_from_cypher, long_key_password)
    deXore_q = XOR.XOR(Xored_q_from_cypher, long_key_password)

    #Convert from binary back to original int
    decoded_one = binary.from_binary(deXore_p)
    decoded_two = binary.from_binary(deXore_q)
    print(" Decode P:", decoded_one)
    print(" Decode Q:", decoded_two)
    return[decoded_one, decoded_two]
    #RSA_Encryption.run_rsa()

"""
password = input("Input Password \n")
password = password + "Add extra information to this password"
encypher = create_encypher(password)
password = input("Input Password \n")
password = password + "Add extra information to this password"
p_q = decode_encypher(password, encypher)
RSA_Encryption_New.main(p_q[0], p_q[1], "hooray this is cool I can type a lot lets see exactlyh")
decode_encypher(password, encypher)
"""
