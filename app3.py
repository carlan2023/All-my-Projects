import time
from ping3 import ping
from twilio.rest import Client


account_sid = 'AC2950e73b2503bfb46988ccd23c762aea'  
auth_token = '6f3d0def860d319a8f4492a2e4e45d91'    
twilio_number = '+13156693232'  
phone_numbers = ['+256707068533', '+256704089642','+256757714351',]  #  phone numbers
client = Client(account_sid, auth_token)
ip_addresses = ['102.217.133.132','102.217.133.98','102.217.133.130',]

# Create a dictionary to store the ping failure count for each IP
ping_failures = {ip: 0 for ip in ip_addresses}

while True:
    for ip in ip_addresses:
        try:
            # Ping the IP address
            if ping(ip) is None:
                # If the IP is not reachable, increment the failure count
                ping_failures[ip] += 1
                # If the IP has failed to respond to 30 pings, send an SMS
                if ping_failures[ip] >= 30:
                    for number in phone_numbers:
                        message = client.messages.create(
                            body=f'IP address {ip} has been down for 60 seconds!',
                            from_=twilio_number,
                            to=number
                        )
                        print(f'SMS sent to {number}: {message.sid}')
                        ping_failures[ip] = 0
            else:
                # If the IP is reachable, reset the failure count
                ping_failures[ip] = 0
        except Exception as e:
            print(f'Error: {e}')
        finally:
            time.sleep(1)  # Sleep for 1 second before next ping
