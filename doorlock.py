from twilio.rest import TwilioRestClient
 
# Your Account Sid and Auth Token from twilio.com/user/account
"""account_sid = "#############"
auth_token  = "############"
client = TwilioRestClient(account_sid, auth_token)
 
message = client.messages.create(body="Hello Kitson - This is Pi",
    to="+18888888888",    # Replace with your phone number
    from_="+19999999999") # Replace with your Twilio number
print message.sid"""

from flask import Flask, request, redirect
import twilio.twiml
import RPi.GPIO as GPIO
import time
 
app = Flask(__name__)

# Try adding your own number to this list!
callers = {
    "+16045068519": "John",
    "+16043767388": "Billy",
    "+16042501029": "Bob",
}
 
@app.route("/", methods=['GET', 'POST'])
def hello_monkey():
    
    sms = request.values.get('Body', None)
    from_number = request.values.get('From', None)
        
    if (from_number in callers and sms == 'unlock'):
        
        """Move The Servo Motor To Open Position"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        pwm = GPIO.PWM(18, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        pwm.stop()
        GPIO.cleanup()
        message = callers[from_number] + ", the door is now open!"
    elif (from_number in callers and sms == 'lock'):
        
        """Move The Servo Motor"""
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(18, GPIO.OUT)
        pwm = GPIO.PWM(18, 50)
        pwm.start(0)
        pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        pwm.stop()
        GPIO.cleanup()
        message = callers[from_number] + ", the door is now locked!"
    else:
        message = "Access Denied Bitch!"

    resp = twilio.twiml.Response()
    resp.message(message)

    return str(resp)
 
if __name__ == "__main__":
    app.run(host='0.0.0.0')

