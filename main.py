## step 1:- install required libraries
from twilio.rest import Client
from datetime import datetime, timedelta
import time

## step 2:- twilio crediantials
account_sid = '' ## add your twilio credentials
auth_token = '' ## add your twilio credentials

client = Client(account_sid,auth_token)

## step 3:- design send message function

def send_whatsapp_message(recipient_number, message_body):
    try:
        message = client.messages.create(
            from_='whatsapp:+',## add your twilio whatsapp number
            body=message_body,
            to=f'whatsapp:{recipient_number}'
        )

        print(f'Message sent successfully! Message SID: {message.sid}')

    except Exception as e:
        print("An error occurred:", e)

## step 4:- user input
name = input("enter the receipent name: ")
recepient_number = input("enter the receipent whatsapp number with country code(eg +123): ")
message_body = input(f'enter the message you want to send to {name}: ')

## step 5:- parse date/time and calculate delay
date_str = input('enter the date to send the message (YYYY-MM-DD): ')
time_str = input('enter the time to send the message (HH:MM in 24hour format): ')

## Datetime

schedule_datetime = datetime.strptime(f'{date_str} {time_str}', "%Y-%m-%d %H:%M")
current_datetime = datetime.now()

## Calculate delay
time_difference = schedule_datetime - current_datetime
delay_seconds = time_difference.total_seconds()

if delay_seconds <=0:
    print('the specified time is in the past. Please enter a future date and time: ')
else: 
    print(f'Message scheduled to be sent to {name} at {schedule_datetime}.')

## wait until the scheduled time
    time.sleep(delay_seconds)
## send the message
    send_whatsapp_message(recepient_number,message_body)