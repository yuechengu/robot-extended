import time

from selenium.common.exceptions import StaleElementReferenceException

from extend.common import INFO, STEP, CHECK_POINT
from library.calculator import calculate_synthesis
from library.excelio import writeToExcel
from library.webui import *
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


# 套件的初始化
def suite_setup():
    driver = open_browser_Chrome()
    time.sleep(2)
    login_ziroom(driver)
    INFO('登入')


# 套件的清除
def suite_teardown():
    driver = get_global_webdriver()
    driver.quit()
    INFO('登出')


class AutoCollectRoomsData:
    # 用例名
    name = '自动获得租房信息'

    # 用例步骤
    def teststeps(self):
        driver = get_global_webdriver()
        wait = WebDriverWait(driver, 3)

        for _ in range(3):
            try:
                rent_house_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '//*[@id="Z_layout_head"]/div/div/ul/li[2]/a'))
                )
                rent_house_button.click()
                break
            except StaleElementReferenceException:
                time.sleep(1)
                INFO('try to find element click after another 1s')

        for _ in range(3):
            try:
                map_button = wait.until(
                    EC.element_to_be_clickable((By.XPATH, '/html/body/section/div[1]/div/a[2]'))
                )
                map_button.click()
                break
            except StaleElementReferenceException:
                time.sleep(1)
                INFO('try to find element click after another 1s')

        # select box
        select_box_items = driver.find_elements(By.XPATH, '//*[@id="selectBox"]/dl')
        whole_rent = select_box_items[0]
        price_range = select_box_items[1]
        orientation = select_box_items[2]
        area = select_box_items[3]
        more_info = select_box_items[4]
        # 是否整租
        whole_rent.click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="J_typeList"]/div[2]/a[2]').click()
        driver.find_element(By.XPATH, '//*[@id="J_typeList"]/div[3]/a[2]').click()
        driver.find_element(By.XPATH, '//*[@id="J_typeConfirm"]').click()
        # 面积
        area.click()
        time.sleep(0.5)
        driver.find_element(By.XPATH, '//*[@id="J_areaList"]/a[3]/span').click()
        # 关键词
        outter_break = False
        while not outter_break:
            driver.find_element(By.ID, 'J_MyKeywords').send_keys('曲阳公园办公楼')  # 鲁迅公园
            time.sleep(1)
            ajax_items = driver.find_elements(By.XPATH, '//*[@id="ajaxBox"]/ul/li')
            for ajax_item in ajax_items:
                if ajax_item.text == '曲阳公园办公楼':  # 鲁迅公园
                    ajax_item.click()
                    outter_break = True
                    break
            else:
                driver.find_element(By.ID, 'J_MyKeywords').clear()

        # 存储二维list
        title_list = ['房源名', '小区名', '建筑面积㎡', '楼层', '电梯', '年代', '小区指数', '综合得分']
        table_list = [[] for i in range(0, 50)]

        # 所有符合的房源
        iniWindow = driver.current_window_handle
        satisfied_communities = driver.find_elements(By.XPATH, '//*[@onclick="houseMarkersClick(this)"]')

        count_previous = 0
        for i in range(len(satisfied_communities)):
            satisfied_communities[i].click()
            time.sleep(5)
            satisfied_houses = driver.find_elements(By.XPATH, '//*[@id="J_houseList"]/li')

            for j in range(len(satisfied_houses)):
                satisfied_houses[j].click()
                time.sleep(5)
                # 切换页面
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    if 'ziroom.com/x/' in driver.current_url:
                        break

                # 房源名
                house_name_text = driver.find_element(By.XPATH, '//aside[@class="Z_info_aside"]/h1').text
                table_list[count_previous + j].append(house_name_text)
                # 小区名
                community_name_text = driver.find_element(By.XPATH, '//*[@id="villageinfo"]/div/div/div/h3').text
                table_list[count_previous + j].append(community_name_text)
                # 建筑面积
                arch_area_text = driver.find_element(By.XPATH, '//div[@class="Z_home_b clearfix"]/dl[1]/dd').text
                table_list[count_previous + j].append(arch_area_text)
                # 楼层
                floor_text = driver.find_element(By.XPATH, '//ul[@class="Z_home_o"]/li[2]/span[2]').text
                table_list[count_previous + j].append(floor_text)
                # 电梯
                has_elevator_text = driver.find_element(By.XPATH, '//ul[@class="Z_home_o"]/li[3]/span[2]').text
                table_list[count_previous + j].append(has_elevator_text)
                # 年代
                built_year_text = driver.find_element(By.XPATH, '//ul[@class="Z_home_o"]/li[4]/span[2]').text
                table_list[count_previous + j].append(built_year_text)

                # 进入小区简介页面
                driver.find_element(By.XPATH, '//div[@id="villageinfo"]/a[1]').click()
                time.sleep(2)
                # 切换页面
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    if 'ziroom.com/xiaoqu/' in driver.current_url:
                        break
                # 小区指数
                community_index_text = driver.find_element(By.XPATH, '//div[@class="Z_village_num"]/p').text
                table_list[count_previous + j].append(community_index_text)

                # 综合得分
                synthesis = calculate_synthesis(arch_area_text, floor_text, has_elevator_text, built_year_text,
                                                community_index_text)
                print(synthesis)
                table_list[count_previous + j].append(synthesis)
                print(table_list)

                # 关闭新窗口
                driver.close()
                # 切回页面
                for handle in driver.window_handles:
                    driver.switch_to.window(handle)
                    if 'ziroom.com/map/' in driver.current_url:
                        break

            # 过去总计数
            count_previous += len(satisfied_houses)

        while [] in table_list:
            table_list.remove([])

        print(table_list)

        writeToExcel(title_list, table_list, 'Zirooms')



