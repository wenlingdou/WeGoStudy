import datetime
from time import sleep
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver import Keys
from selenium.common.exceptions import NoSuchElementException
import WeGoStudy_locators as locators
from webdriver_manager.chrome import ChromeDriverManager

s=Service(ChromeDriverManager().install())
driver = webdriver.Chrome(service=s)

def setUp():
    print(f'Test starts at {datetime.datetime.now()}.')
    driver.maximize_window()
    driver.implicitly_wait(30)
    driver.get(locators.app_url)

    if driver.current_url == locators.app_url and locators.homepage_title in driver.title:
        print(f'{locators.app} website launched successfully!')
        print(f'{locators.app} Homepage URL: {driver.current_url}, Homepage title: {driver.title}')
        sleep(0.25)
    else:
        print(f'{locators.app} did not launch successfully, please check your code and launch again!')
        print(f'Current URL: {driver.current_url}, Current page title: {driver.title}.')
        driver.close()
        driver.quit()

def tearDown():
    if driver is not None:
        print(f'---------The test is passed.----------------')
        print(f'---------The test is completed on {datetime.datetime.now()}.-------------')
        sleep(0.5)
        driver.close()
        driver.quit()

def login():
    driver.find_element(By.XPATH, '//b[normalize-space()="LOGIN"]').click()
    sleep(0.25)
    driver.find_element(By.ID, 'user_email').send_keys(locators.admin_email)
    sleep(0.25)
    driver.find_element(By.ID, 'user_password').send_keys(locators.admin_password)
    sleep(0.25)
    driver.find_element(By.XPATH, '//input[@value="SIGN IN"]').click()
    sleep(3)

def create_new_student():
    if driver.current_url==locators.login_page_url:
        print(f'----------Current URL: {locators.login_page_url}--------')
    driver.find_element(By.XPATH, '//span[normalize-space()="My WeGoStudy"]').click()
    sleep(0.25)
    driver.find_element(By.XPATH, '//a[normalize-space()="Students"]').click()
    sleep(0.25)
    if driver.current_url==locators.student_page_url:
        print(f'-------------Create New Student----------------------')
    driver.find_element(By.XPATH, '//a[normalize-space()="Create New Student"]').click()
    sleep(0.25)
    breakpoint()
setUp()
login()
create_new_student()
tearDown()



