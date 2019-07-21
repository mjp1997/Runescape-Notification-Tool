# #import necessary libraries
import datetime
import smtplib, ssl
import getpass
from email.message import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart

with open(osrsOutput) as tfile:
    message = EmailMessage()
    message.set_content(tfile.read())

message["Subject"] = "The contects of %s" % cms_scrape.csv
message["From"] = "mjp970501@gmail.com"
messge["To"] = "perez15@live.missouristate.edu"

# #retrieve current timestamp
# myDate = datetime.datetime.now()
# formatDate = myDate.strftime('%m-%d-%y %H:%M')
# print(formatDate)

# # msg = MIMEMultipart()
# # msg['Subject'] = 'Runescape Update Tracker'
port = 465  # For SSL

# retrieve recipient's e-mail and sender's pass
senderEmail = "mjp970501@gmail.com"
sendTo = "perez15@live.missouristate.edu"
Template = """Update alert, hope it's a good one :) """
# print(userMessage)
password = input("Please type your e-mail's password: ")

# # # Create a secure SSL contex
context = ssl.create_default_context()

server = smtplib.SMTP_SSL("smtp.gmail.com", port, context=context)
try:

    server.send_message(message)
#      # TODO: Send email
except:
    print("Error, e-mail could not be sent. Please check the e-mail/pass you entered.")

