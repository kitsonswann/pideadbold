from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
account_sid = "#####"
auth_token  = "#####"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello Kitson - This is Pi",
    to="+16045068519",    # Replace with your phone number
    from_="+1999999999") # Replace with your Twilio number
print message.sid
