from twilio.rest import Client

account_sid = 'ACb1d6418e2849e91bd8724a91d1d83b3c'
auth_token = 'a54a988ec4a6d9678aef298c07074931'
client = Client(account_sid, auth_token)

message = client.messages.create(
  from_='+15739952652',
  body='please, work',
  to='+201007049467'
)

print(message.sid)