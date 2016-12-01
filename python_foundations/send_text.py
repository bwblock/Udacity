#! /usr/bin/env python

from twilio import rest

account_sid = "AC9ab531246c1adebf51310166d405fe45" # Your Account SID from www.twilio.com/console
auth_token  = "057334c6e90165f5f307750670d8fd5d"  # Your Auth Token from www.twilio.com/console

client = rest.TwilioRestClient(account_sid, auth_token)

message = client.messages.create(body="Hello my name is Ron Burgandy?",
    to="+13037095009",    # Replace with your phone number
    from_="+17205525086") # Replace with your Twilio number

print(message.sid)