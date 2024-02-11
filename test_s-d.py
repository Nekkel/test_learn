from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
import time

from selenium import webdriver
from selenium.webdriver.common.keys import Keys


# Функция ожидания элементов
def wait_of_element_located(xpath, driver):
    element = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located(
            (By.XPATH, xpath)
        )
    )
    return element


def test_add_jacket_to_the_shopcart():
    options = webdriver.ChromeOptions()
    options.add_experimental_option("excludeSwitches", ["enable-logging"])
    driver = webdriver.Chrome(options=options)
    driver.get("https://shop.bbrfactory.com/")

    # Поиск и ожидание элементов и присваивание к переменным.
   # input_username = wait_of_element_located(xpath='//*[@id=\"user-name\"]', driver=driver)
    # input_password = wait_of_element_located(xpath='//*[@id=\"password\"]', driver=driver)
    # login_button = wait_of_element_located(xpath='//*[@id=\"login-button\"]', driver=driver)

    # Действия с формами
   # input_username.send_keys("standard_user")
  # input_password.send_keys("secret_sauce")
   # login_button.send_keys(Keys.RETURN)

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id="main-nav"]/ul/li[2]/a', driver=driver)
    item_name.click()

    # Поиск и ождиание прогрузки ссылки элемента товара магазина и клик по ссылке
    item_name = wait_of_element_located(xpath='//*[@id="main-nav"]/ul/li[2]/a', driver=driver)
    item_name.click()

    # Поиск и ожидание кнопки добавления товара и клик по этой кнопке
    item_add_button = wait_of_element_located(xpath='//*[@id=\"add-to-cart-sauce-labs-fleece-jacket\"]', driver=driver)
    item_add_button.click()

    # Ждем пока товар добавится в корзину, появится span(кол-во позиций в корзине) и кликаем по корзине чтобы перейти
    wait_of_element_located(xpath='//*[@id=\"shopping_cart_container\"]/a/span', driver=driver).click()

    # Еще один поиск ссылки элемента позиции магазина
    item_name = wait_of_element_located(xpath='//*[@id=\"item_5_title_link\"]/div', driver=driver)
    if item_name.text == "Sauce Labs Fleece Jacket":
        print("Товар пристутствует в корзине")
    else:
        print("Товар отсутствует")

    time.sleep(5)


if __name__ == '__main__':
    test_add_jacket_to_the_shopcart()
