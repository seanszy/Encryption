username = 'pythontest57@gmail.com'
password = 'PythonTest5'

import smtplib
fromaddr = 'pythontest57@gmail.com'
toaddrs  = 'kathyszy@comcast.net'
msg = "\r\n".join([
  "From: PythonTest57@gmail.com",
  "To: kathyszy@comcast.net",
  "Subject: Hi",
  "",
  "Kathy is dumb."
  ])
server = smtplib.SMTP('smtp.gmail.com:587')
server.ehlo()
server.starttls()
server.login(username,password)
server.sendmail(fromaddr, toaddrs, msg)
server.quit()
