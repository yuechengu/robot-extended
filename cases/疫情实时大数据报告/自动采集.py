import os
import time
from selenium.webdriver.common.by import By
from extend.common import *
from library.webui import *
from library.excelio import writeToExcel


def suite_setup():
    driver = open_browser_Chrome()
    login_BaiduNewPneumonia(driver)


def suite_teardown():
    log_path = os.path.abspath(os.path.dirname(__file__)) + r'\..\reports\log.html'
    driver = get_global_webdriver()
    driver.quit()
    os.system(log_path)


class AutoCollectCovidNews:
    # 用例名
    name = '自动采集疫情速报'

    # 用例步骤，即本用例的正式脚本
    def teststeps(self):
        STEP(1, '进入页面')
        driver = get_global_webdriver()
        CHECK_POINT('是否进入成功',
                    isElementPresent(driver, 'id', 'viewport'))

        STEP(2, '展开全部')
        driver.find_element(By.XPATH, '//*[@id="ptab-0"]/div[2]/div[2]/div[3]/div/span').click()
        CHECK_POINT('点击展开全部是否成功',
                    len(driver.find_elements(By.XPATH,
                                             '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[1]')) > 5)

        STEP(3, '爬取国内疫情速报写入excel')
        title_list = driver.find_element(By.XPATH, '//*[@id="ptab-0"]/div[2]/div[2]/div[1]').text.split()
        title_list.insert(0, '省份')
        INFO(title_list)

        provinces = driver.find_elements(By.XPATH,
                                         '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div/div/div[1]/div/span[2]')
        cities = driver.find_elements(By.XPATH,
                                      '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div[1]/div/div/div/span[1]')
        new_locals = driver.find_elements(By.XPATH,
                                          '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div[1]/div/div[2]')
        new_no_symptoms = driver.find_elements(By.XPATH,
                                               '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div[1]/div/div[3]')
        risk_areas = driver.find_elements(By.XPATH,
                                          '//*[@id="ptab-0"]/div[2]/div[2]/div[2]/div/div[1]/div/div[4]')

        length = len(cities)
        table_list = [[] for i in range(length)]

        for i in range(0, length):
            table_list[i].append(provinces[i].text if provinces[i].text != '' else '-')
            table_list[i].append(cities[i].text)
            table_list[i].append(new_locals[i].text)
            table_list[i].append(new_no_symptoms[i].text)
            table_list[i].append(risk_areas[i].text)
            INFO(table_list[i])

        writeToExcel(title_list, table_list, 'CovidNews')


class AutoCollectCovidData:
    # 用例名
    name = '自动采集疫情数据'

    # 用例步骤，即本用例的正式脚本
    def teststeps(self):
        STEP(1, '进入页面')
        driver = get_global_webdriver()
        CHECK_POINT('是否进入成功',
                    isElementPresent(driver, 'id', 'viewport'))

        STEP(2, '展开全部')
        driver.find_element(By.XPATH, '//*[@id="nationTable"]/div/span').click()
        CHECK_POINT('点击展开全部是否成功',
                    len(driver.find_elements(By.XPATH, '//*[@id="nationTable"]/table/tbody/tr')) > 5)

        STEP(3, '爬取国内疫情数据写入excel')
        titles = driver.find_element(By.XPATH, '//*[@id="nationTable"]/table/thead/tr').text.split()
        title_list = []
        for i in range(0, len(titles), 2):
            title_list.append(titles[i] + titles[i+1])
        INFO(title_list)

        table_elements = driver.find_elements(By.XPATH, '//*[@id="nationTable"]/table/tbody/tr')
        table_list = []
        for table_element in table_elements:
            INFO(table_element.text.split())
            table_list.append(table_element.text.split())

        writeToExcel(title_list, table_list, 'CovidStatus')
