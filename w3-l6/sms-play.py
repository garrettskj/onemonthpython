#!/usr/bin/python3

import getpass
from twilio.rest import Client

def get_number():
	
	# Get the number
	number = input("Enter your 10-digit number: ")

	# pass back the number
	return number

def get_msg():
	
	# Get the message
	msg = input("Type the message you want to send: ")

	# pass back the message
	return msg

def send_text(msg, number):

	# define account credentials
        # 
        # This key is invalid as of 20190316
        # it exists purely as a reference.
        #
	account_sid = "AC928c4aabbb739945a8923d78423d3918"
	account_token = "19159916a877dfed02d7e0b56f1b32f7"

	# define the Twilio client connection
	client = Client(account_sid, account_token)

	# create the US number + area code.
	ten_digit = "+1" + number

	# define and send the message
	message = client.messages.create(to=ten_digit, from_="+19712590512", body=msg)



number = get_number()
msg = get_msg()

send_text(msg, number)
