from twilio.rest import Client

# Your Account SID from twilio.com/console
account_sid = "AC3fb16a915c7473d0ed7fed12baf0262f"
# Your Auth Token from twilio.com/console
auth_token  = "1d5933333a4a5a32adf2cbded7a609c1"

client = Client(account_sid, auth_token)

message = client.messages.create(
    to="+17868731231", 
    from_="+13059306403",
    body="I see you YAZ OO")

print(message.sid)

