import time
import pytest

from selenium.webdriver.common.keys import Keys
from selenium import webdriver

from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

data = ['Java википедия', 'Python википедия', 'SWIFT википедия']

service = Service

def return_text_element(driver, xpath):
    element = driver.find_element(By.XPATH, xpath)
    return element.text

@pytest.fixture(scope='function')
def driver():
    options = webdriver.ChromeOptions()
    driver = webdriver.Chrome(options=options)
    driver.get("https://www.google.com/")
    yield driver
    driver.quit()


@pytest.mark.parametrize("search_text", data)
def test_google_search_list(driver, search_text):
    # Поиск элементов и присваивание к переменным.


    input_text = driver.find_element(By.XPATH, "//*[@id=\"APjFqb\"]")
    input_text.send_keys(search_text)

    search_btn = driver.find_element(By.XPATH, "//input[@value='Поиск в Google']")
    search_btn.send_keys(Keys.RETURN)

    item_add_button = driver.find_element(By.XPATH,"//div[@id='search']/div//h3")
    item_add_button.click()

    title_text = return_text_element(driver, '//span[@class="mw-page-title-main"]')

    assert title_text == search_text.replace(' википедия', '')





    ###### цикл WHILE
    # n = 0
    # while n < len(data):
    #     input_text.send_keys(data[n])
    #     n = n + 1
    # time.sleep(1)

    # input_text.send_keys(Keys.RETURN) # TODO запонить как работает