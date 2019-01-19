from twilio.rest import Client
import schedule
import time


def text_message():
    account_sid = 'AC7646b2570b49b7e7153ba34b566b1c04'
    auth_token = '870fc4e44ce8dae45f7500daca3b55d8'
    client = Client(account_sid, auth_token)

    message = client.messages.create(
        body="GO TO THE GYM!!!",
        from_='+12892784078',
        to='+19059221865'
    )

    print(message.sid)


schedule.every().day.at("20:00").do(text_message)

while True:
    schedule.run_pending()
    time.sleep(60) # wait one minute
