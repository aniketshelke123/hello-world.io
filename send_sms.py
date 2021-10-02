import os
from forgot_password.rest import Client


AC637c30642ae5835c32fec20938064650 = os.environ['TWILIO_ACCOUNT_SID']
f67e0fd99943a14bcdf8a99c9b3c1c79 = os.environ['TWILIO_AUTH_TOKEN']
client = Client("account_sid, auth_token")

message = client.messages \
    .create(
         body='This is a reminder from library, kindly return your book within 2 days',
         from_='+13367153420',
         to='+919423873496'
     )

print(message.sid)

