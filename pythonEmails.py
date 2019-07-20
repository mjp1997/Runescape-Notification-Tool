import smtplib, ssl
import getpass

port = 465  # For SSL
senderEmail = "mjp970501@gmail.com"
password = getpass.getpass(prompt="Please enter your email's password: ", stream=None)
userMessage = input("Please type your e-mail that you wish to send: ")

# Create a secure SSL context
context = ssl.create_default_context()

with smtplib.SMTP_SSL("smtp.gmail.com", port, context=context) as server:
    server.login(senderEmail, password)
    server.sendmail(senderEmail, "perez15@live.missouristate.edu", userMessage)
    # TODO: testing testing
