import time

from selenium import webdriver
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait

from extend.common import GSTORE


def get_global_webdriver():
    return GSTORE['global_webdriver']


def open_browser_Chrome():
    driver = webdriver.Chrome()
    driver.implicitly_wait(6)
    GSTORE['global_webdriver'] = driver
    return driver


def login_RobotSpareBin(driver):
    driver.get('https://robotsparebinindustries.com/#/')
    driver.find_element(By.ID, 'username').send_keys('maria')
    driver.find_element(By.ID, 'password').send_keys('thoushallnotpass')
    driver.find_element(By.TAG_NAME, 'button').click()

def logout_RobotSpareBin(driver):
    driver.find_element(By.ID, 'logout').click()


def login_ziroom(driver):
    driver.maximize_window()
    driver.get('https://sh.ziroom.com/')
    driver.find_element(By.ID, 'zLogin').click()
    driver.find_element(By.ID, 'swichAccontHook').click()
    driver.find_element(By.ID, 'accontUserHook').send_keys('18101971080')
    driver.find_element(By.ID, 'accontPsdHook').send_keys('gyc228059')
    driver.find_element(By.ID, 'loginAccontSubmitHook').click()

def logout_ziroom(driver):
    driver.find_element(By.XPATH, '//div[@class="Z_container Z_header_main"]//div[2]//a[2]').click()


def login_douban(driver):
    wait = WebDriverWait(driver, 2)
    driver.get('https://www.douban.com/')
    # 要先切换到子框架
    driver.switch_to.frame(driver.find_elements_by_tag_name('iframe')[0])
    driver.find_element(By.XPATH, '//*[@class="tab-start"]/li[2]').click()
    driver.find_element(By.ID, 'username').send_keys('18101071080')
    driver.find_element(By.ID, 'password').send_keys('gyc228059')
    driver.find_element(By.XPATH, '//*[@class="account-form-field-submit "]/a').click()

def get_cookies_douban(driver):
    driver.get('https://www.douban.com/')
    # time.sleep(1)
    cookies = driver.get_cookies()
    print(cookies)


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
