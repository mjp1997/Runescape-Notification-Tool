import smtplib, ssl
import getpass

port = 465  # For SSL

# retrieve recipient's e-mail and sender's pass
senderEmail = "mjp970501@gmail.com"
sendTo = "perez15@live.missouristate.edu"
userMessage = input("Please type your e-mail that you wish to send: ")
password = input("Please type your e-mail's password: ")

# Create a secure SSL context
context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
try:
    server.login(senderEmail, password)
    server.sendmail(senderEmail, sendTo, userMessage)
    # TODO: Send email here
except:
    print("Error, e-mail could not be sent. Please check the e-mail/pass you entered")
