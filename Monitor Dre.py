import time
import pyautogui
import pywhatkit
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Function to take a screenshot of the webpage
def take_screenshot(url, save_path):
    driver = webdriver.Chrome(executable_path='path/to/chromedriver')  # Specify the path to your Chrome WebDriver
    driver.get(url)
    driver.save_screenshot(save_path)
    driver.quit()

# Function to refresh the webpage
def refresh_webpage():
    pyautogui.hotkey('ctrl', 'r')  # Send Ctrl+R to refresh the webpage

# Function to send the screenshot via WhatsApp Web
def send_screenshot_to_whatsapp(contact, screenshot_path):
    pywhatkit.sendwhats_image(phone_num=contact, img_path=screenshot_path)

if _name_ == "_main_":
    website_url = "https://example.com"  # Replace with the URL of the webpage you want to capture
    screenshot_path = "screenshot.png"  # Specify where to save the screenshot
    whatsapp_contact = "your_contact_number"  # Replace with the recipient's WhatsApp number

    while True:
        take_screenshot(website_url, screenshot_path)
        send_screenshot_to_whatsapp(whatsapp_contact, screenshot_path)
        refresh_webpage()
        time.sleep(900)  # Sleep for 15 minutes (900 seconds) before repeating the process
