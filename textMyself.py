#! python3
# textMyself.py - Defines the textMyself() function that texts a message
# passed to it as a string.

# Preset values:
accountSID = 'yourTwilioAccountSID'
authToken = 'yourTwilioAuthToken'
myNumber = 'yourMobileNumber'
twilioNumber = 'yourTwilioNumber'

from twilio.rest import Client

def textMyself(message):
    twilioCli = Client(accountSID, authToken)
    twilioCli.messages.create(body=message, from_=twilioNumber, to=myNumber)
