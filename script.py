from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.keys import Keys
from model.htmlElements import HTMLElements
from config.userData import WorkingHours, UserData
import time

def configDriver():
    driver = webdriver.Chrome(UserData.driverPath)
    driver.maximize_window()
    driver.get(UserData.url)
    driver.set_page_load_timeout(3)

    return driver

def findByXPathClickElement(nameOfElement, htmlElement: str, driver: WebDriver):
    forceWait(1)
    print("\nFinding and clicking on element: ", nameOfElement)

    try:
        htmlElement = driver.find_element_by_xpath(htmlElement)
    except:
        print(f'\n\nError trying to find element {nameOfElement}')
        return


    try:
        htmlElement.click()
    except:
        print(f'\n\nError trying to click element: {nameOfElement}')
        return



    return htmlElement

def forceWait(timeSleep :int):
    print(f'\nFORCE WAIT/SLEEP FOR {str(timeSleep)} SECONDS\n')
    time.sleep(timeSleep)


def runDriver(driver: WebDriver): 

    # navigation
    loginToDashboard(driver)
    fillWorkingHours(driver)


    # wait to not close driver
    forceWait(20)

def loginToDashboard(driver: WebDriver ):
    print('\n=================================================')
    print(' STARTING TO LOGIN')    
    print('=================================================')

    username = findByXPathClickElement('Login - Form - Input Field - Username', HTMLElements.inputLogin, driver)
    username.send_keys(UserData.username)

    password = findByXPathClickElement('Login - Form - Input Field - Password', HTMLElements.inputPwd, driver)
    password.send_keys(Keys.TAB)
    password.send_keys(UserData.password)

    findByXPathClickElement('Login - Form - Btn Login ', HTMLElements.btnLoginButton, driver)

    driver.implicitly_wait(40)
    findByXPathClickElement('Login - Form - Btn Clock Dashboard', HTMLElements.btnClockDashboard, driver)



def fillWorkingHours(driver: WebDriver):
    print('\n=================================================')
    print(' STARTING TO FILL SHEET WITH WORKING HOURS')    
    print('=================================================')

    forceWait(3)
    # yesterday = findByXPathClickElement(HTMLElements.yesterday, driver)
    # yesterday.click()

    findByXPathClickElement('Clock Sheet - Today Date', HTMLElements.today, driver)
    # today.click()
    # forceWait(3)

    findByXPathClickElement('Clock Sheet - Btn Insert Hour', HTMLElements.btnInsertHour, driver)
    
    hour = findByXPathClickElement('Clock Sheet - Form - Input Hour', HTMLElements.inputHour, driver)
    hour.send_keys(WorkingHours.firstHour)

    message = findByXPathClickElement(HTMLElements.inputMessage, driver)
    message.send_keys(UserData.inputMessage)

    driver.implicitly_wait(40)


runDriver(configDriver())
