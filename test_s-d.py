
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time
from selenium.webdriver import ActionChains

from selenium import webdriver
#from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def test_add_bbrfactory_com():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://shop.bbrfactory.com/")

    # Setup chrome driver
    driver.set_window_size(1920, 1080)


    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке

    item_name = wait_of_element_located(xpath='//*[@id="main-nav"]/ul/li[2]/a', driver=driver)
    item_name.click()

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id="categories-wrapper"]/ul/li[5]/a', driver=driver)
    item_name.click()

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@title="Джим Вернулся 254"]', driver=driver)
    item_name.click()

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id="button-cart"]', driver=driver)
    item_name.click()

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке

    actions = ActionChains (driver)
    actions.move_by_offset(900, 147).perform()
    actions.click().perform()


    time.sleep(5)


if __name__ == '__main__':
    test_add_bbrfactory_com()