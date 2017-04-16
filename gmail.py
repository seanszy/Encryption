username = 'pythontest57@gmail.com'
password = 'PythonTest5'
import random
import smtplib

def send_2_factor(toaddrs):
    two_factor = random.randint(1000, 9999)

    fromaddr = 'pythontest57@gmail.com'
    toaddrs  = toaddrs
    msg = "\r\n".join([
      "From: PythonTest57@gmail.com",
      "To: " + toaddrs,
      "Subject: Authentication",
      "",
      "Your Authentication Code is: " + str(two_factor)
      ])
    server = smtplib.SMTP('smtp.gmail.com:587')
    server.ehlo()
    server.starttls()
    server.login(username,password)
    server.sendmail(fromaddr, toaddrs, msg)
    server.quit()
    return two_factor

send_2_factor("seanszy57@gmail.com")
