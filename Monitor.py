import pyautogui
import schedule
import time
from twilio.rest import Client

# Twilio Configuration - replace with your actual Twilio details
account_sid = 'your_account_sid'
auth_token = 'your_auth_token'
from_whatsapp_number = 'whatsapp:your_twilio_whatsapp_number'
to_whatsapp_number = 'whatsapp:your_personal_whatsapp_number'

client = Client(account_sid, auth_token)

def take_screenshot():
    # Take a screenshot
    screenshot = pyautogui.screenshot()
    screenshot_path = "screenshot.png"
    screenshot.save(screenshot_path)
    
    # Send the screenshot to WhatsApp
    message = client.messages.create(
        body='Here is your screenshot.',
        media_url=['file://' + screenshot_path],
        from_=from_whatsapp_number,
        to=to_whatsapp_number
    )
    print(message.sid)
take_screenshot()

# Schedule the screenshot function to run every hour
schedule.every(1).hours.do(take_screenshot)

while True:
    schedule.run_pending()
    time.sleep(1)
