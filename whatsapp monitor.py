import time
from ping3 import ping, verbose_ping
from twilio.rest import Client

# Twilio settings
account_sid = 'AC2950e73b2503bfb46988ccd23c762aea'  # replace with your Twilio Account SID
auth_token = '6f3d0def860d319a8f4492a2e4e45d91'    # replace with your Twilio Auth Token
twilio_number = 'whatsapp:+14155238886'  # replace with your Twilio number. The format is 'whatsapp:' followed by your Twilio number
to_number = 'whatsapp:+256707068533'  # replace with your phone number. The format is 'whatsapp:' followed by the phone number

client = Client(account_sid, auth_token)

# List of IP addresses to monitor
ip_addresses = ['102.217.133.86', '8.8.8.8', '102.217.133.90', '102.217.133.94', '102.217.133.132','102.217.133.98']

while True:
    for ip in ip_addresses:
        try:
            # Ping the IP address
            if ping(ip) is None:
                # If the IP is not reachable, send a WhatsApp message
                message = client.messages.create(
                    body=f'IP address {ip} is down!',
                    from_=twilio_number,
                    to=to_number
                )
                print(f'WhatsApp message sent: {message.sid}')
        except Exception as e:
            print(f'Error: {e}')
        finally:
            time.sleep(1)  # Sleep for 1 second before next ping
