import os
from colorama import Fore, Back, Style
import requests
from bs4 import BeautifulSoup
import time
import random
import pyautogui
import keyboard
from datetime import datetime
import ctypes

from selenium import webdriver
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import Chrome, ChromeOptions
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver import Chrome
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.chrome.options import Options

from fake_useragent import UserAgent

from timeit import default_timer as timer
from datetime import timedelta

from faker import Faker



ua = UserAgent()
userAgent = ua.random

choice = int(input("""
1) Console - Black CMD Screen
SLOWER

2) Idle - Python Editing Application
FASTER
--> """))

#clear console
os.system('cls')

site = "https://kahoot.it/"

##SETTING CHROMEDRIVER
chrome_options = Options()
chrome_options.add_argument("--incognito")
#chrome_options.add_argument('headless')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('--disable-dev-shm-usage')
chrome_options.add_argument('--no-sandbox')
chrome_options.add_argument('disable-infobars')

#chrome_options.add_argument(f'user-agent={userAgent}')

chromepath = r"./chromedriver.exe"


pin = input("Game Pin: ")


choice2 = int(input("""
1) Custom Name
2) Random Name
--> """))
if choice2 == 1:
    user = input("Bot Username: ")



bots = int(input("How Many Bots: "))
while True:
    if bots >=201:
        print(Fore.RED + "MAXIMUM BOTS: 200")
        bots = int(input(Fore.WHITE + "How Many Bots: "))
    else:
        break


def chromebug():
    if i == 20:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
        
    elif i == 40:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 60:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 80:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 100:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 120:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 140:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 160:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 180:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    elif i == 200:
        #new driver to fix issues
        driver = webdriver.Chrome(chromepath, options=chrome_options)
        print("Loading new Chromedriver")
        time.sleep(2)
    

driver = webdriver.Chrome(options=chrome_options)
wait = WebDriverWait(driver, 10)


tstart = datetime.now()

starthead = timer()

faker = Faker()

for i in range(bots):
    
    #chromebug()    
    start = datetime.now()
    if choice2 == 1:
        username = user + str(i + 1)
    elif choice2 == 2:
        fname = faker.first_name()
        mname = faker.last_name()
        lname = faker.last_name()
        username = fname + " " + lname
        print(Fore.WHITE + f"USERNAME: {username}" + Fore.GREEN)
    driver.execute_script("window.open('');")
    driver.switch_to.window(driver.window_handles[i + 1])
    driver.get(site)
    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#game-input')))
    driver.find_element_by_id('game-input').send_keys(pin)
    driver.find_element_by_id('game-input').send_keys(Keys.ENTER)
    print(f"Entered Game Pin: {pin}")

    wait.until(expected_conditions.presence_of_element_located((By.CSS_SELECTOR, '#nickname')))
    driver.find_element_by_id('nickname').send_keys(username)
    driver.find_element_by_id('nickname').send_keys(Keys.ENTER)
    print(f"Entered Username: {username}")
    
    end1 = datetime.now()
    endtime = end1 - start
    print(Fore.BLUE + f"Sent Bot {username} In {endtime} Seconds" + Fore.GREEN)

time.sleep(2)
sstart = datetime.now()
completed = sstart - tstart
print(Fore.BLUE + f"""
    INFO
BOTS: {bots}
PIN: {pin}
TIME: {completed}
""" + Fore.GREEN + f"""PRESS ENTER TO EXIT THE APPLICATION TO REMOVE BOTS
""" + Fore.BLACK)
end = input()
driver.quit()
