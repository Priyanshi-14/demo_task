from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time
import gspread
from google.oauth2.service_account import Credentials

SCOPES = [
    'https://www.googleapis.com/auth/drive',
    'https://www.googleapis.com/auth/spreadsheets'
]
# Load the credentials from the JSON key file
credentials = Credentials.from_service_account_file('micro-eye-387806-cfb9590680e5.json', scopes=SCOPES)

# Authorize the client using the credentials
client = gspread.authorize(credentials)

# Open the spreadsheet by its title or URL
spreadsheet = client.open_by_url('https://docs.google.com/spreadsheets/d/1N0Uf-zul0jYFMfDMrA415jVpBW1mrkka4TB6SS6q6Ns/edit#gid=0')

worksheet = spreadsheet.sheet1

# Fetch all values from the worksheet
values = worksheet.get_all_values()
header_row = values[0]
number_index = header_row.index('Number')
name_index = header_row.index('Name')
message_index = header_row.index('Message')
number_values = [row[number_index] for row in values]
name_values = [row[name_index] for row in values]
message_values = [row[message_index] for row in values]


def send_msg_recursive(numbers, names, messages, index):
    if index >= len(numbers):
        return

    number = numbers[index]
    name = names[index]
    message = messages[index]

    if number == "Number" and name == "Name" and message == "Message":
        send_msg_recursive(numbers, names, messages, index + 1)
    else:
        num = number
        msg = "Hey " + name + " \n" + message
        msg = quote(msg)
        driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        link = 'https://web.whatsapp.com'
        driver.get(link)
        time.sleep(20)

        link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
        driver.get(link2)
        print(driver)
        time.sleep(20)
        action = ActionChains(driver)
        action.send_keys(Keys.ENTER)
        action.perform()
        time.sleep(50)

    
        driver.quit()
        time.sleep(5)
        send_msg_recursive(numbers, names, messages, index + 1)

send_msg_recursive(number_values, name_values, message_values, 0)
