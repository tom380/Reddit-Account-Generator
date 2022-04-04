from os.path import dirname
from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import random
import time
import re
import string
import secrets
import os
driver = webdriver.Chrome(ChromeDriverManager().install()) # USES CHROMEDRIVERMANAGER TO AUTO UPDATE CHROMEDRIVER


# GENERATE PASSWORD
alphabet = string.ascii_letters + string.digits
password = ''.join(secrets.choice(alphabet) for i in range(16))
# PASSWORD GENERATION FINISHED

# NAME GENERATION
driver.get('https://en.wikipedia.org/wiki/Special:Random')
temp = driver.find_element_by_class_name("firstHeading").text
for char in string.punctuation:
    temp = temp.replace(char, '') #REMOVES ALL PUNCTUATION
for char in string.digits:
    temp = temp.replace(char, '') #REMOVES SPACES
temp = "".join(filter(lambda char: char in string.printable, temp)) #REMOVES NON ASCII CHARACTERS
name = ''.join(temp.split())
name = name[:random.randint(5,7)] #KEEPS 5 TO 7 LETTERS OF THE ORIGINAL STRING


randomNumber = random.randint(10000,99999)
finalName = name+str(randomNumber)
time.sleep(1)
# NAME GENERATION FINISHED

# REDDIT ACCOUNT CREATION
driver.get('https://www.reddit.com/register/')
driver.find_element_by_id('regEmail').send_keys('mail@mail.mail')
time.sleep(1)
driver.find_element_by_xpath ("//button[contains(text(),'Continue')]").click()
time.sleep(3)
driver.find_element_by_id('regUsername').send_keys(finalName)
driver.find_element_by_id('regPassword').send_keys(password)

# CAPTCHA SOLVER
#time.sleep(20)
#wait = WebDriverWait(driver,300)
#wait.until(EC.url_changes("https://www.reddit.com/register/"))
bt_submit = driver.find_element_by_css_selector("[type=submit]")
#bt_submit = driver.find_elements_by_xpath('//button[normalize-space()="Sign Up"]')
WebDriverWait(driver, timeout=1000, poll_frequency=1) \
  .until(EC.staleness_of(bt_submit))

dirname = os.path.dirname(__file__)
text_file_path = os.path.join(dirname, 'namesforreddit.txt')
text_file = open(text_file_path, "a")
#text_file.write("USR: " + name + str(randomNumber) + " PWD: " + password) #OUTPUTS NAME AND NUMBER
text_file.write("        \"" + name + str(randomNumber) + "\": {\n            \"password\": \"" + password + "\",\n            \"start_coords\": [0, 0]\n        },")
text_file.write("\n")
text_file.close()

# driver.close()