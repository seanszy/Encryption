import random
import smtplib

def send_2_factor(toaddrs):
    """This function is used for two-factor authentication. The program
    sends a random authentication key to an email that is passed in. the
    user then uses this key as an authentication password. This program was
    created by combining several online resources on sending gmails."""


    two_factor = random.randint(1000, 9999) #generate authentication key
    #The email that we are currently using is a gmail that was made for
    #this project. It sends emails for authentication.

    fromaddr = 'pythontest57@gmail.com'
    password = 'PythonTest5'
    message = "Subject: Two-Factor Authentication\r\n" + "\r\nTo: " + toaddrs + "\r\nYour Authentication Code is: " + str(two_factor) #adds authentication code to email

    server = smtplib.SMTP('smtp.gmail.com:587') #sets up a server to send it on
    server.ehlo()
    server.starttls()
    server.login(fromaddr,password) #uses email information to login.
    server.sendmail(fromaddr, toaddrs, message) #sends teh email
    server.quit()
    return two_factor #returns the authentication key so it can be compared to
    #what the user enters

send_2_factor("seanszy57@gmail.com")
