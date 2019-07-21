# import necessary libraries
import datetime
import smtplib, ssl
import getpass
from email.message import EmailMessage
from email.mime.image import MIMEImage
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText

# open/read textfile generated from the scraper
with open("osrsOutput.txt", "r") as fileOutput:
    osrsOutput = MIMEText(fileOutput.read())
    fileOutput.close()

# specify e-mail content/information fields
senderEmail = "mjp970501@gmail.com"
sendTo = "perez15@live.missouristate.edu"
sentMsg = """Update alert, hope it's a good one :) """
osrsOutput["Subject"] = "Old School Runescape Update Notifier: "
osrsOutput["From"] = senderEmail
osrsOutput["To"] = sendTo

# #retrieve current timestamp
# myDate = datetime.datetime.now()
# formatDate = myDate.strftime('%m-%d-%y %H:%M')
# print(formatDate)

# server info
port = 465  # For SSL
smtp_server_name = "smtp.gmail.com"
server = smtplib.SMTP_SSL(smtp_server_name, port)


password = input("Please type your e-mail's password: ")

# error handling
server.login(senderEmail, password)
try:
    server.send_message(osrsOutput)
except:
    print("Error, e-mail could not be sent. Please check the e-mail/pass you entered.")

