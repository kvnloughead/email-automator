# comment

import sys
import getpass
import argparse

def get_args():
  print('Welcome to email_automator\n==========================')

  user_email = input("Your email\n>")
  password = getpass.getpass("Password\n>")

  contacts = input("Enter name of contacts file (.csv). This file must contain contact \nemail addresses and any other parameters for use in the emails\n> ")
  message = input("Enter name of text file message template\n> ")
  attachments = input("Enter names of attachments, separated by spaces.  If none, hit enter.\n> ")
  if attachments:
    attachments = attachments.split(" ")
  return user_email, password, contacts, message, attachments

def send_mail():
  print('======================')
  input('Are you ready to send?  Type yes or no\n> ')
  print('======================')




