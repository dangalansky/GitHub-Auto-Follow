import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import ElementNotInteractableException, NoSuchElementException
import random

#your login information
USERNAME = YOUR USERNAME
PASSWORD = YOUR PASSWORD

# who do you want to target for followers?
target_user = USERNAME

# webdriver init
ser = Service('/Users/dangalansky/Dropbox/Developer Tools/chromedriver')
driver = webdriver.Chrome(service=ser)
driver.get('https://github.com/login')

# identify elements/selectors for login
login = driver.find_element_by_css_selector('#login_field')
password = driver.find_element_by_css_selector('#password')
submit = driver.find_element_by_name('commit')

# execute GitHub Login
login.send_keys(USERNAME)
password.send_keys(PASSWORD)
submit.send_keys(Keys.ENTER)

# go to followers page of target user
driver.get(f'https://github.com/{target_user}?tab=followers')
time.sleep(5)

while True:
    time.sleep(2)
    for n in range(50):
        n = n + 1
        try:
            button = driver.find_element_by_xpath(
                f'//*[@id="js-pjax-container"]/div[2]/div/div[2]/div[2]/div/div[{n}]/div[3]/span/form[1]/input[2]')
            button.click()
            time.sleep(1)
        except NoSuchElementException:
            pass
        except ElementNotInteractableException:
            pass
    next = driver.find_element_by_link_text('Next')
    next.click()
