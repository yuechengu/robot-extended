import time
from selenium.webdriver.common.by import By
from selenium.webdriver.support.select import Select

from extend.common import *
from library.webui import *
from library.excelio import readFromExcel


# 套件的初始化
def suite_setup():
    driver = open_browser_Chrome()
    login_RobotSpareBin(driver)
    INFO('登入')


# 套件的清除
def suite_teardown():
    driver = get_global_webdriver()
    logout_RobotSpareBin(driver)
    driver.quit()
    INFO('登出')


class AutoSubmitSalesData:
    # 用例名
    name = '自动提交销售数据'

    # 用例步骤
    def teststeps(self):
        STEP(1, '驱动浏览器，进入主页登录')
        driver = get_global_webdriver()
        CHECK_POINT('是否登录成功',
                    isElementPresent(driver, 'id', 'logout'))

        STEP(2, '提交数据')
        # 读取excel
        table_list = readFromExcel('SalesData')

        for i in range(0, len(table_list)):
            # firstname
            driver.find_element(By.ID, 'firstname').send_keys(table_list[i][0])
            # lastname
            driver.find_element(By.ID, 'lastname').send_keys(table_list[i][1])
            # salestarget
            Select(driver.find_element(By.ID, 'salestarget')).select_by_value(str(table_list[i][3]))
            # salesresult
            driver.find_element(By.ID, 'salesresult').send_keys(table_list[i][2])
            # submit
            driver.find_element(By.XPATH, '//*[@id="sales-form"]/button').click()
            # 检查单条数据是否提交成功
            CHECK_POINT(f'第{i+1}条数据是否提交成功',
                        driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/span[2]').text == str(i+1))

        CHECK_POINT('是否全部提交成功',
                    driver.find_element(By.XPATH, '//*[@id="root"]/div/div/div/div[2]/div[1]/div[1]/span[2]').text == str(len(table_list)))
