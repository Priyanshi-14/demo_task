from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.keys import Keys
from urllib.parse import quote
import time

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#time.sleep(10)

link = 'https://web.whatsapp.com'
driver.get(link)
time.sleep(30)


for num in numbers:
    link2 = f'https://web.whatsapp.com/send/?phone=91{num}&text={msg}'
    driver.get(link2)
    print(driver)
    time.sleep(5)
    action = ActionChains(driver)
    action.send_keys(Keys.ENTER)
    action.perform()
    time.sleep(5)
    
time.sleep(300)