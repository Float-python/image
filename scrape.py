from selenium import webdriver
import time
from selenium.webdriver.chrome.options import Options
import sys
import os



# log in
def login():
    options = Options()
    option = webdriver.ChromeOptions()
    option.add_experimental_option("excludeSwitches", ["enable-automation"])
    option.add_experimental_option('useAutomationExtension', False)
    option.add_argument('--disable-blink-features=AutomationControlled')
    options.add_argument('--ignore-certificate-errors')
    driver = webdriver.Chrome('C:\\chromedriver.exe',options=option)
    driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")
    driver.get('https://aternos.org/server')
    text_area = driver.find_element_by_id('user')
    text_area.send_keys("ajinomoto114514")
    time.sleep(3)
    text_area = driver.find_element_by_id('password')
    text_area.send_keys("hyugo1116")
    time.sleep(3)
    login = driver.find_element_by_xpath('/html/body/div[3]/div/div/div[4]/div[3]/div[4]')
    login.click()
    time.sleep(3)
    driver.get('https://aternos.org/server')
    time.sleep(3)
    return driver

# accept cookie privacy prompt


# select server
def select_server():
    driver = login()
    select = driver.find_element_by_xpath('/html/body/div/main/section/div/div[2]/div/div[1]')
    select.click()

# wait for the page to load
    time.sleep(5)
    return driver

# click start button
def start():
    driver = select_server()
    start = driver.find_element_by_xpath('/html/body/div[2]/main/section/div[3]/div[4]/div[1]')
    start.click()

    time.sleep(5)

# click cancel
    cancel = driver.find_element_by_xpath('/html/body/div[2]/main/div/div/div/main/div/a[2]')
    cancel.click()

    time.sleep(3)
    kill(driver)
    return driver

def get_status():
    driver = select_server()
    status = driver.find_element_by_xpath('//*[@id="read-our-tos"]/main/section/div[3]/div[3]/div[1]/div/span[2]/span').text()
    kill(driver)
    return status
    
    

#close chromium and python
def kill(driver):
    driver.close()

