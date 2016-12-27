from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "AC494595b37f8a8a903d4fe4bb3f9a46b0"
auth_token  = "a0e519a5d6bea59418b265f5abb82b2f"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello Kitson - This is Pi",
    to="+16045068519",    # Replace with your phone number
    from_="+16042106375") # Replace with your Twilio number
print message.sid
