import time
from auth_data import log, pas
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys


chrome_driver_path = ChromeDriverManager().install()
browser_service = Service(executable_path=chrome_driver_path)
browser = webdriver.Chrome(service=browser_service)

def auth_yandex(login, passw):
    browser.get('https://passport.yandex.ru/auth/list')
    time.sleep(3)

    email_input = browser.find_element(by='id', value='passp-field-login')
    email_input.clear()
    email_input.send_keys(login)
    time.sleep(1)
    email_input.send_keys(Keys.ENTER)
    time.sleep(3)


    passw_input = browser.find_element(by='id', value='passp-field-passwd')
    passw_input.send_keys(passw)
    time.sleep(1)
    passw_input.send_keys(Keys.ENTER)
    time.sleep(5)

    return browser.find_element(by='class', value='Card_label__AG2MY')

    browser.close()
    browser.quit()








