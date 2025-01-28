from twilio.rest import Client
from django.conf import settings

def send_whatsapp_message(phone_number, message_body):
  
    formatted_phone_number = f"whatsapp:+{phone_number.lstrip('+')}"  

    client = Client(settings.TWILIO_ACCOUNT_SID, settings.TWILIO_AUTH_TOKEN)

    message = client.messages.create(
        body=message_body,
        from_='whatsapp:+14155238886',  
        to=formatted_phone_number  
    )
    
    return message
