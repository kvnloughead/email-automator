# Program to send off multiple emails 
# Walkthrough at https://www.freecodecamp.org/news/send-emails-using-code-4fcea9df63f/

import sys
import csv
import email
import smtplib
import argparse
from string import Template
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText    
from email.mime.application import MIMEApplication

import interface


user_email, password, contacts, message, attachments = interface.get_args()

def get_contacts(contacts):
    """Function to read contacts from a given file
    and return a list of names and email addresses"""
    # open file and establish headers
    f = open(contacts, 'r')
    reader = csv.reader(f)
    headers = next(reader, None)
    # build dictionary of contact info
    columns = {}
    for h in headers:
        columns[h] = []
    for row in reader:
        for h, v in zip(headers, row):
            columns[h].append(v)
    return columns

def read_template(message):
    """Reads text file into Template object"""
    with open(message, 'r', encoding='utf-8') as template_file:
        template_file_content = template_file.read()
    return Template(template_file_content)


# setup SMTP server - use PORT 587 if 25 is blocked
s = smtplib.SMTP(host='smtp-mail.outlook.com', port=587)
s.starttls()
s.login(user_email, password)

# build the data and templates
contacts = get_contacts(contacts)
message_template = read_template(message)

# TODO generalize this into a function with all template fields as parameters
# for each contact, send the email
for first_name, last_name, email, fav_lang in zip(contacts['first_name'], contacts['last_name'], contacts['email'], contacts['fav_lang']):
    # create a message
    msg = MIMEMultipart()
    
    # fill in template fields
    message = message_template.substitute(first_name=first_name.title(), last_name=last_name.title(), fav_lang=fav_lang.title())
    # setup email parameters
    msg['From']=user_email
    msg['To']=email
    msg['Subject']="Enter subject here"

    # add in message body
    msg.attach(MIMEText(message, 'plain'))

    # attach files
    if attachments:
        for filename in attachments:
            part = MIMEApplication(open(filename, 'rb').read())
            part.add_header('Content-Disposition', 'attachment', filename=filename)
            msg.attach(part)

    # send message via server that was set up above
    try:
        s.send_message(msg)
    except:
        print(f"Couldn't send email to {email}")

    del msg

# Terminates the SMTP session and closes connection
s.quit()