from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.by import By

from extend.common import GSTORE


def get_global_webdriver():
    return GSTORE['global_webdriver']


def open_browser_Chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(3)
    GSTORE['global_webdriver'] = driver
    return driver


def login_RobotSpareBin(driver):
    driver.get('https://robotsparebinindustries.com/#/')
    driver.find_element(By.ID, 'username').send_keys('maria')
    driver.find_element(By.ID, 'password').send_keys('thoushallnotpass')
    driver.find_element(By.TAG_NAME, 'button').click()


def logout_RobotSpareBin(driver):
    driver.find_element(By.ID, 'logout').click()


def login_BaiduNewPneumonia(driver):
    driver.get('https://voice.baidu.com/act/newpneumonia/newpneumonia/?from=osari_aladin_banner')


def isElementPresent(driver, by, value):
    try:
        driver.find_element(by=by, value=value)
    except NoSuchElementException:
        print(NoSuchElementException)
        return False
    else:
        return True
