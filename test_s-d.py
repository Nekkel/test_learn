
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

    # Устанавливаем удобное нам разрешение экрана
    driver.set_window_size(1920, 1080)


    # Поиск и ождиание прогрузки ссылки категории магазина и клик по ссылке

    item_name = wait_of_element_located(xpath='//*[@id="main-nav"]/ul/li[2]/a', driver=driver)
    item_name.click()
    time.sleep(5)
    # Поиск и ождиание прогрузки элемента категории магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id="categories-wrapper"]/ul/li[5]/a', driver=driver)
    item_name.click()
    time.sleep(5)
    # Поиск и ождиание прогрузки товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@title="Джим Вернулся 254"]', driver=driver)
    item_name.click()
    time.sleep(5)
    # Поиск и ождиание прогрузки корзины магазина и клик по корзине
    item_name = wait_of_element_located(xpath='//*[@id="button-cart"]', driver=driver)
    item_name.click()
    time.sleep(5)
    # Поиск и ождиание прогрузки субссылки корзины магазина и клик по ссылке

    actions = ActionChains (driver)
    actions.move_by_offset(900, 147).perform()
    actions.click().perform()

    time.sleep(5)
    # Проверка элемента

    item_name = wait_of_element_located( xpath='//*[@id="simplecheckout_form_0"]/div/div[1]/div[1]/h1', driver=driver)

    if item_name.text == "Оформление заказа":
        print ("Оформление заказа находится в заголовке")
    else:
        print ("Оформление заказа не находится в заголовке")

        # Проверка стоимости товара

    item_name = wait_of_element_located( xpath='//*[@id="simplecheckout_cart"]/div[2]/div[2]/span[2]', driver=driver)

    if item_name.text == "Итого: 18 500р.":
        print ("Стоимость соответствует")
    else:
        print ("Стоимость не соответствует")

    # Увеличиваем количество элементов

    item_name = wait_of_element_located(xpath='//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/span[2]/button[1]/img', driver=driver)
    item_name.click()
    time.sleep(5)

    # Проверка стоимости товаров

    item_name = wait_of_element_located(xpath='//*[@id="simplecheckout_cart"]/div[2]/div[2]/span[2]', driver=driver)

    if item_name.text == "Итого: 37 000р.":
        print ("Стоимость соответствует")
    else:
        print ("Стоимость не соответствует")


    # Проверка количества товаров

    item_name = wait_of_element_located( xpath='//*[@id="simplecheckout_cart"]/div[1]/table/tbody/tr/td[4]/div/input', driver=driver)

    if item_name.get_attribute("value") == "2":

        print("Количество соответствует")
    else:
        print("Количество не соответствует")

    # листаем до конца страницы

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")

    # нажимаем кнопку "Оплатить заказ"

    item_name = wait_of_element_located(xpath='//*[@id="simplecheckout_button_confirm"]', driver=driver)
    item_name.click()
    time.sleep(5)

    # проверяем наличие ошибки под полем e-mail

    item_name = wait_of_element_located( xpath='//*[@id="simplecheckout_customer"]/div[2]/fieldset/div[1]/div/div/div[2]', driver=driver)

    if item_name.text == "Некорректный адрес электронной почты!":

        print("Ошибка подтвердилась")
    else:
        print("Ошибка не подтвердилась")

    # Проверка цвета ошибки

    item_name = wait_of_element_located( xpath='//*[@id="simplecheckout_customer"]/div[2]/fieldset/div[1]/div/div/div[2]', driver=driver)

    if item_name.get_attribute("color") == "#FF0000":

        print("Цвет ошибки соответствует")
    else:
        print("Цвет ошибки не соответствует")

if __name__ == '__main__':
    test_add_bbrfactory_com()


